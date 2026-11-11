import bpy
from ..preferences import preferences
from ..tags import (
    get_context_tags,
    get_env_tags,
    get_scene_tags,
    get_type_tag,
    get_material_tags,
    get_subdivision_tag,
    get_parent_tags,
    get_object_name_tag,
    get_object_user_tags,
    sort_tags,
)

TAG_PROP = "st_tags"


class ST_ApplyTags(bpy.types.Operator):
    """Apply tags for selected objects"""
    bl_idname = "object.apply_tags"
    bl_label = "Apply Tags"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # General tags
        prefs = preferences()

        if prefs.use_context_tags:
            context_tags = get_context_tags(context)

        if prefs.use_env_tags:
            env_tags = get_env_tags()

        if prefs.use_scene_tags:
            scene_tags = get_scene_tags(context.scene)

        for obj in context.selected_objects:
            # Object specific tags
            if prefs.use_type:
                type_tag = [get_type_tag(obj)]
            if prefs.use_parents:
                parent_tags = get_parent_tags(obj)
            if prefs.use_object_name:
                object_name_tag = [get_object_name_tag(obj)]
            if prefs.use_object_user_tags:
                object_user_tags = get_object_user_tags(obj)

            # Mesh specific tags
            if obj.type == "MESH":
                if prefs.use_materials:
                    material_tags = get_material_tags(obj)
                if prefs.use_subdivision:
                    subdivision_tag = [get_subdivision_tag(obj)]

            # Treating the tags
            all_tags = []
            for local, value in locals().copy().items():
                if local.endswith("_tags") or local.endswith("_tag"):
                    if not value:
                        continue

                    if not isinstance(value, list):
                        continue

                    all_tags.extend(value)

            # Apply the tags to the object
            if not obj.get(TAG_PROP, None):
                obj[TAG_PROP] = ""
                obj.property_overridable_library_set(TAG_PROP, False)

            obj[TAG_PROP] = ",".join(all_tags)

        return {'FINISHED'}
