import bpy
import os


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


def get_object_name_tag(object: bpy.types.Object) -> str:
    """ Returns the object name tag of the given object. """
    prefix = "OBJECT="
    return f"{prefix}{object.name}" if prefix else object.name


def get_object_user_tags(object: bpy.types.Object) -> list[str]:
    """ Returns a list of user-defined tags for the given object. """
    tags = []

    tag_string = getattr(object, "st_objectTags", "")
    tags.extend(read_tags_string(tag_string))

    return tags


def get_context_tags(context: bpy.types.Context) -> list[str]:
    """ Returns a list of tags for the given context. """
    tags = []

    scene = context.scene
    view_layer = context.view_layer
    workspace = context.workspace
    world = context.world

    if scene:
        tags.append(f"SCENE={scene.name}")

    if view_layer:
        tags.append(f"VIEW_LAYER={view_layer.name}")

    if workspace:
        tags.append(f"WORKSPACE={workspace.name}")

    if world:
        tags.append(f"WORLD={world.name}")

    return tags


def _env_filter_func(key: str) -> bool:
    """ Default filter function for environment variables. """
    return False


def get_env_tags(filter_func: callable = _env_filter_func) -> list[str]:
    """ Returns a list of environment tags. """
    tags = []

    prefix = "ENV="

    # Add environment variables as tags
    keys = os.environ.copy().keys()

    if filter_func:
        keys = filter(filter_func, keys)

    for key in keys:
        value = os.environ.get(key)

        if value is None:
            continue

        tag = f"{prefix}{key}={value}"
        tags.append(tag)

    return tags


def get_scene_tags(scene: bpy.types.Scene) -> list[str]:
    """ Returns a list of tags for the given scene. """
    tags = []

    tag_string = getattr(scene, "st_sceneTags", "")
    tags.extend(read_tags_string(tag_string))

    return tags


def register():
    bpy.types.Scene.st_sceneTags = bpy.props.StringProperty(
        name="Scene Tags",
        description="Comma-separated tags for the scene",
        default=""
    )
    bpy.types.Object.st_objectTags = bpy.props.StringProperty(
        name="Object Tags",
        description="Comma-separated tags for the object",
        default=""
    )


def unregister():
    del bpy.types.Scene.st_sceneTags
    del bpy.types.Object.st_objectTags
