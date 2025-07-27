import gc
import os
import tempfile
import threading
import time

import psutil

from src.config import settings

if not settings.test:
    import pythoncom
    import win32com.client as win32

# Глобальный лок для синхронизации доступа к Excel
_excel_lock = threading.Lock()


def _kill_excel_processes():
    """Принудительно завершает все зависшие процессы Excel"""
    try:
        for proc in psutil.process_iter(["pid", "name"]):
            if proc.info["name"] and "excel" in proc.info["name"].lower():
                try:
                    proc.kill()
                    proc.wait(timeout=2)  # Ждем завершения процесса
                except (
                    psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.TimeoutExpired,
                ):
                    pass
    except Exception:
        pass


def _ensure_com_initialized():
    """Безопасная инициализация COM"""
    try:
        pythoncom.CoInitialize()
    except Exception:
        # COM уже инициализирован в этом потоке
        pass


def _cleanup_com():
    """Безопасная очистка COM"""
    try:
        # Принудительная сборка мусора для освобождения COM объектов
        gc.collect()
        pythoncom.CoUninitialize()
    except Exception:
        pass


def _release_com_object(obj):
    """Безопасное освобождение COM-объекта"""
    if obj is not None:
        try:
            # Используем Marshal для правильного освобождения COM объекта
            pythoncom._univgw.IUnknown_QueryInterface(obj, pythoncom.IID_IUnknown)
            del obj
        except Exception:
            pass


def fill_cells(cells: dict[str, str | int | float], file_content: bytes) -> bytes:
    if settings.test:
        return b""  # Возвращаем пустые байты вместо None

    # Используем лок с timeout для предотвращения бесконечных блокировок
    if not _excel_lock.acquire(timeout=30):  # Максимум 30 секунд ожидания
        raise Exception("Не удалось получить доступ к Excel - возможно процесс завис")

    try:
        # Инициализируем COM
        _ensure_com_initialized()

        # Создаем временный файл для входного Excel
        with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as temp_input:
            temp_input.write(file_content)
            temp_input_path = temp_input.name

        # Создаем временный файл для выходного Excel
        temp_output_path = tempfile.mktemp(suffix=".xlsx")

        xlApp = None
        workbook = None

        try:
            # Очищаем зависшие процессы перед созданием нового
            _kill_excel_processes()
            time.sleep(0.5)  # Увеличиваем время ожидания

            xlApp = win32.Dispatch("Excel.Application")
            xlApp.Visible = False
            xlApp.DisplayAlerts = False  # Отключаем диалоги
            xlApp.ScreenUpdating = (
                False  # Отключаем обновление экрана для производительности
            )
            xlApp.EnableEvents = False  # Отключаем события
            xlApp.Interactive = False  # Отключаем пользовательский ввод

            # Открываем файл из временного пути
            workbook = xlApp.Workbooks.Open(
                temp_input_path, ReadOnly=False, UpdateLinks=False
            )
            sheet = workbook.ActiveSheet

            # Заполняем ячейки
            for cell_address, value in cells.items():
                if isinstance(value, (int, float)):
                    sheet.Range(cell_address).Value = value
                else:
                    sheet.Range(cell_address).Value = str(value)

            # Сохраняем в новый временный файл
            workbook.SaveAs(temp_output_path, FileFormat=51)  # 51 = xlsx format

            # Читаем сохраненный файл в байты ДО закрытия
            with open(temp_output_path, "rb") as output_file:
                result = output_file.read()

            return result

        except Exception as e:
            # В случае ошибки принудительно очищаем процессы
            _kill_excel_processes()
            raise e

        finally:
            # Правильное закрытие COM объектов в обратном порядке
            try:
                if workbook is not None:
                    try:
                        workbook.Close(SaveChanges=False)
                    except Exception:
                        pass
                    _release_com_object(workbook)
                    workbook = None

                if xlApp is not None:
                    try:
                        xlApp.EnableEvents = True
                        xlApp.ScreenUpdating = True
                        xlApp.Interactive = True
                        xlApp.Quit()
                    except Exception:
                        pass
                    _release_com_object(xlApp)
                    xlApp = None

                # Принудительная сборка мусора
                gc.collect()

                # Увеличиваем задержку для завершения процесса Excel
                time.sleep(1.0)

                # Дополнительная проверка и очистка процессов
                _kill_excel_processes()

            except Exception:
                # Если обычное закрытие не сработало, принудительно убиваем процессы
                _kill_excel_processes()

            finally:
                # Очищаем временные файлы с повторными попытками
                max_attempts = 10
                for attempt in range(max_attempts):
                    try:
                        if os.path.exists(temp_input_path):
                            os.unlink(temp_input_path)
                        break
                    except (PermissionError, OSError):
                        if attempt < max_attempts - 1:
                            time.sleep(0.5)

                for attempt in range(max_attempts):
                    try:
                        if os.path.exists(temp_output_path):
                            os.unlink(temp_output_path)
                        break
                    except (PermissionError, OSError):
                        if attempt < max_attempts - 1:
                            time.sleep(0.5)

                # Очищаем COM после завершения всех операций
                _cleanup_com()

    finally:
        # Обязательно освобождаем лок
        _excel_lock.release()
