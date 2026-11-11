import bpy


def read_tags_string(tag_string: str) -> list:
    """ Read a string of tags and return a list of tags.

    Args:
        tag_string (str): Comma-separated string of tags.

    Returns:
        list: A list of tags.
    """

    return [tag.strip() for tag in tag_string.split(",") if tag.strip()]


def get_type_tag(object: bpy.types.Object) -> str:
    """ Returns the type tag of the given object. """
    prefix = "TYPE="
    return f"{prefix}{object.type}" if prefix else object.type


def get_material_tags(
        object: bpy.types.Object,
        filter_func: callable = None) -> list[str]:
    """ Returns a list of material tags for the given object. """
    prefix = "MAT="

    materials = [slot.material.name for slot in object.material_slots
                 if slot.material]

    if filter_func:
        materials = list(filter(filter_func, materials))

    return [f"{prefix}{mat}" for mat in materials]


def get_subdivision_tag(object: bpy.types.Object) -> str:
    """ Returns the subdivision tag of the given object. """
    prefix = "SUBDIV="

    level_count = 0

    if object.modifiers:
        for modifier in object.modifiers:
            if modifier.type == 'SUBSURF':
                modifier: bpy.types.SubsurfModifier
                level_count += modifier.levels
                break

    return f"{prefix}{level_count}"


def get_parent_tags(object: bpy.types.Object,
                    filter_func: callable = None) -> list[str]:
    """ Returns a list of parent tags for the given object. """
    prefix = "PARENT="

    parents = []
    current_parent = object.parent

    while current_parent:
        parents.append(current_parent.name)
        current_parent = current_parent.parent

    if filter_func:
        parents = list(filter(filter_func, parents))

    return [f"{prefix}{parent}" for parent in parents]

