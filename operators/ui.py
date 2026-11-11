""" UI operators for the SmartTags addon """
import bpy


class ST_OpenPreferences(bpy.types.Operator):
    """Open the addon preferences"""
    bl_idname = "wm.open_smarttags_preferences"
    bl_label = "Open SmartTags Preferences"

    def execute(self, context):
        bpy.ops.screen.userpref_show('INVOKE_DEFAULT')

        context.preferences.active_section = 'ADDONS'
        try:
            bpy.data.window_managers["WinMan"].addon_search = "SmartTags"
        except Exception:
            print("SmartTags: Could not set addon search term in preferences.")

        return {'FINISHED'}
