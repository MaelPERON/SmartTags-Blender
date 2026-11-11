import bpy


class ST_Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__


def preferences() -> ST_Preferences:
    """ Returns the addon preferences. """
    return bpy.context.preferences.addons[__package__].preferences
