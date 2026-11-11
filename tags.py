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

