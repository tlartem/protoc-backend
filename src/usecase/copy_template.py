import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src import dto, model
from src.adapter import postgres


async def copy_template(
    _input: dto.CopyTemplateInput, session: AsyncSession
) -> dto.CopyTemplateOutput:
    original_template = await postgres.template.get(session, _input.template_id)
    if not original_template:
        raise ValueError(f"Template {_input.template_id} not found")

    updated_elements = _update_element_ids(original_template.elements)
    new_template = model.Template(
        name=_input.new_name,
        description=_input.new_description,
        elements=updated_elements,
    )
    new_template = await postgres.template.create(session, new_template)

    original_files = await postgres.file.get_by_template(session, _input.template_id)
    for original_file in original_files:
        new_file = model.File(
            name=original_file.name,
            content=original_file.content,
            cells=original_file.cells,
            template_id=new_template.id,
        )
        await postgres.file.create(session, new_file)

    original_sheets = await postgres.sheet.get_by_template(session, _input.template_id)
    for original_sheet in original_sheets:
        new_sheet = model.Sheet(
            name=original_sheet.name,
            cells=original_sheet.cells,
            template_id=new_template.id,
        )
        await postgres.sheet.create(session, new_sheet)

    if _input.new_attributes:
        for attr_input in _input.new_attributes:
            template_attribute = model.TemplateAttribute(
                template_id=new_template.id,
                attribute_id=attr_input.attribute_id,
                value=attr_input.value,
            )
            await postgres.template_attribute.create(session, template_attribute)
    else:
        original_attributes = await postgres.template_attribute.get_by_template_id(
            session, _input.template_id
        )
        for original_attr in original_attributes:
            template_attribute = model.TemplateAttribute(
                template_id=new_template.id,
                attribute_id=original_attr.attribute_id,
                value=original_attr.value,
            )
            await postgres.template_attribute.create(session, template_attribute)

    return dto.CopyTemplateOutput(new_template_id=new_template.id)


def _update_element_ids(elements: dict) -> dict:
    """Обновляет ID элементов при копировании, генерируя новые UUID"""
    if not elements:
        return elements

    new_elements = {}

    for _, element_data in elements.items():
        new_id = str(uuid.uuid4())

        new_element_data = (
            element_data.copy() if isinstance(element_data, dict) else element_data
        )
        if isinstance(new_element_data, dict) and "id" in new_element_data:
            new_element_data["id"] = new_id

        new_elements[new_id] = new_element_data

    return new_elements
