import os
import tempfile

# import pythoncom
import win32com.client as win32


def fill_cells(cells: dict[str, str | int | float], file_content: bytes) -> bytes:
    # pythoncom.CoInitialize()

    # Создаем временный файл для входного Excel
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as temp_input:
        temp_input.write(file_content)
        temp_input_path = temp_input.name

    # Создаем временный файл для выходного Excel
    temp_output_path = tempfile.mktemp(suffix=".xlsx")

    try:
        xlApp = win32.Dispatch("Excel.Application")
        xlApp.Visible = False
        xlApp.DisplayAlerts = False  # Отключаем диалоги

        # Открываем файл из временного пути
        workbook = xlApp.Workbooks.Open(temp_input_path)
        sheet = workbook.ActiveSheet

        # Заполняем ячейки
        for cell_address, value in cells.items():
            if isinstance(value, (int, float)):
                sheet.Range(cell_address).Value = value
            else:
                sheet.Range(cell_address).Value = str(value)

        # Сохраняем в новый временный файл
        workbook.SaveAs(temp_output_path)
        workbook.Close()
        xlApp.Quit()

        # Читаем сохраненный файл в байты
        with open(temp_output_path, "rb") as output_file:
            result = output_file.read()

        return result

    finally:
        # Очищаем временные файлы
        if os.path.exists(temp_input_path):
            os.unlink(temp_input_path)
        if os.path.exists(temp_output_path):
            os.unlink(temp_output_path)
