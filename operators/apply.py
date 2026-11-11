import bpy
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
        context_tags = get_context_tags(context)
        env_tags = get_env_tags()
        scene_tags = get_scene_tags(context.scene)

        for obj in context.selected_objects:
            # Object specific tags
            type_tag = get_type_tag(obj)
            parent_tags = get_parent_tags(obj)
            object_name_tag = get_object_name_tag(obj)
            object_user_tags = get_object_user_tags(obj)

            # Mesh specific tags
            if obj.type == "MESH":
                material_tags = get_material_tags(obj)
                subdivision_tag = get_subdivision_tag(obj)

            # Treating the tags
            all_tags = (
                context_tags + env_tags + scene_tags + [type_tag]
                + material_tags + [subdivision_tag] + parent_tags
                + [object_name_tag] + object_user_tags
            )

            all_tags = sort_tags(all_tags)

            # Apply the tags to the object
            if not obj.get(TAG_PROP, None):
                obj[TAG_PROP] = ""
                obj.property_overridable_library_set(TAG_PROP, False)

            obj[TAG_PROP] = ",".join(all_tags)

        return {'FINISHED'}
