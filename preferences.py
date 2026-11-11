import bpy


PREFS_ICONS = {
    "use_materials": "MATERIAL",
    "use_type": "COPY_ID",
    "use_subdivision": "MOD_SUBSURF",
    "use_parents": "LINKED",
    "use_object_name": "OBJECT_DATA",
    "use_context_tags": "VIEW3D",
    "use_env_tags": "MEMORY",
    "use_object_user_tags": "TAG",
    "use_scene_tags": "SCENE"
}


class ST_Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    use_materials: bpy.props.BoolProperty(  # type: ignore
        name="Use Materials",
        description="Include materials in the tags (e.g. MAT=DefaultMaterial)",
        default=True,
    )

    use_type: bpy.props.BoolProperty(  # type: ignore
        name="Use Object Type",
        description="Include object type in the tags (e.g. TYPE=Mesh)",
        default=True
    )

    use_subdivision: bpy.props.BoolProperty(  # type: ignore
        name="Use Subdivision",
        description="Include subdivision sum level in the tags (e.g. SUBDIV=2+1, SUBDIV=3)",
        default=True
    )

    use_parents: bpy.props.BoolProperty(  # type: ignore
        name="Use Parents",
        description="Include parent objects in the tags (e.g. PARENT=ParentObjectName)",
        default=True
    )

    use_object_name: bpy.props.BoolProperty(  # type: ignore
        name="Use Object Name",
        description="Include object name in the tags (e.g. OBJECT=ObjectName)",
        default=True
    )

    use_context_tags: bpy.props.BoolProperty(  # type: ignore
        name="Use Context Tags",
        description="Include context tags in the tags (e.g. CONTEXT=EditMode)",
        default=True
    )

    use_env_tags: bpy.props.BoolProperty(  # type: ignore
        name="Use Environment Tags",
        description="Include environment tags in the tags (e.g. BlenderVersion=3.5.0, OS=Windows)",
        default=True
    )

    use_object_user_tags: bpy.props.BoolProperty(  # type: ignore
        name="Use Object User Tags",
        description="Include user-defined tags for the object (e.g. USER=MyCustomTag)",
        default=True
    )

    use_scene_tags: bpy.props.BoolProperty(  # type: ignore
        name="Use Scene Tags",
        description="Include scene tags in the tags (e.g. SCENE=MySceneTag)",
        default=True
    )

    def icon(self, key: str) -> str:
        """ Returns the icon for a given preference key. """
        return PREFS_ICONS.get(key, "QUESTION_LARGE")


def preferences() -> ST_Preferences:
    """ Returns the addon preferences. """
    return bpy.context.preferences.addons[__package__].preferences
