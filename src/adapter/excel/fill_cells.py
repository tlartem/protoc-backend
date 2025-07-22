from io import BytesIO
from typing import Any

from openpyxl import load_workbook


def fill_cells(cells: dict[str, Any], file_content: bytes) -> bytes:
    """
    Заполняет ячейки Excel файла новыми значениями.

    Args:
        cells: Словарь {адрес_ячейки: значение} для обновления
        file_content: Содержимое Excel файла в байтах

    Returns:
        bytes: Обновленное содержимое Excel файла
    """
    # Создаем BytesIO объект из байтов файла
    file_stream = BytesIO(file_content)
    workbook = load_workbook(file_stream)
    sheet = workbook.active

    # Обновляем ячейки
    for cell_address, value in cells.items():
        # Конвертируем значение в строку если это число
        if isinstance(value, (int, float)):
            sheet[cell_address].value = value
        else:
            sheet[cell_address].value = str(value)

    # Сохраняем изменения в BytesIO
    output_stream = BytesIO()
    workbook.save(output_stream)
    output_stream.seek(0)

    return output_stream.getvalue()
