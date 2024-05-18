# Version 1.0 - initial release
# Version 1.1 - removed local character import script, put invocation in the command
# Version 1.2 - added labels, tinted the separator and set button spacing

import pymel.core as pm
import logging

from core_tools.system_paths import PROJECT_ROOT, icon_path
from maya_tools import hotkey_utils
from maya_tools.utilities import shelf_manager
from maya_tools.scene_utils import message_script

ROBOTOOLS_TITLE = 'RobotoolsHotkeys'
ROBOTOOLS_HOTKEYS = PROJECT_ROOT.joinpath('scripts', 'startup', '{}.mhk'.format(ROBOTOOLS_TITLE))
ROBOTOOLS_SHELF_NAME = 'Robotools'
ROBOTOOLS_SHELF_VERSION = '1.2'
ROBOTOOLS_SHELF_PLUG_IN = 'robotools_shelf'
ROBOTOOLS_SHELF_PLUG_IN_PATH = str(pm.pluginInfo(ROBOTOOLS_SHELF_PLUG_IN, query=True, path=True))


def setup_robotools_shelf():
    """
    Sets up the Robotools shelf
    """
    logging.info('>>> Loading Robotools Shelf')
    sm = shelf_manager.ShelfManager(ROBOTOOLS_SHELF_NAME)
    sm.delete()
    sm.create(select=True)
    sm.delete_buttons()

    version_info = 'Robotools Shelf Version {}: {}'.format(ROBOTOOLS_SHELF_VERSION, ROBOTOOLS_SHELF_PLUG_IN_PATH)
    robonobo_icon = icon_path('robonobo_32.png')
    script_icon = icon_path('script.png')
    base_male_cmd = 'from maya_tools.character_utils import import_base_character\nimport_base_character("male")'
    load_base_male = 'from maya_tools.character_utils import load_base_character\nload_base_character("male")'
    base_female_cmd = 'from maya_tools.character_utils import import_base_character\nimport_base_character("female")'
    load_base_female = 'from maya_tools.character_utils import load_base_character\nload_base_character("female")'
    create_cube = 'import pymel.core as pm; pm.polyCube(w=1, h=1, d=1, sx=1, sy=1, sz=1)'
    slice_cmd = 'from maya_tools.mirror_utils import slice_geometry\nslice_geometry()'
    mirror_cmd = 'from maya_tools.mirror_utils import mirror_geometry\nmirror_geometry()'
    quadrangulate = 'import pymel.core as pm\npm.runtime.Quadrangulate()'
    merge_vertices = 'from maya_tools.geometry_utils import merge_vertices\nmerge_vertices'
    select_triangles = 'from maya_tools import geometry_utils; geometry_utils.get_triangular_faces(select=True)'
    select_ngons = 'from maya_tools import geometry_utils; geometry_utils.get_ngons(select=True)'
    super_reset = 'from maya_tools import node_utils; node_utils.super_reset()'
    pivot_base = 'from maya_tools import node_utils; node_utils.pivot_to_base()'
    pivot_center = 'from maya_tools import node_utils; node_utils.pivot_to_center()'
    pivot_origin = 'from maya_tools import node_utils; node_utils.pivot_to_origin()'
    move_to_origin = 'from maya_tools import node_utils; node_utils.move_to_origin()'

    sm.add_label('Robotools v{}'.format(ROBOTOOLS_SHELF_VERSION), bold=True)
    sm.add_shelf_button(label='About Robotools', icon=robonobo_icon, command=message_script(version_info))
    sm.add_separator()
    sm.add_label('Characters')
    sm.add_shelf_button(label='Import Base Male', icon=icon_path('base_male.png'), command=base_male_cmd)
    sm.add_shelf_button(label='Load Base Male', icon=script_icon, command=load_base_male, overlay_label='loadM')
    sm.add_shelf_button(label='Import Base Female', icon=icon_path('base_female.png'), command=base_female_cmd)
    sm.add_shelf_button(label='Load Base Female', icon=script_icon, command=load_base_female, overlay_label='loadF')
    sm.add_separator()
    sm.add_label('Geometry')
    sm.add_shelf_button(label='Create Cube', overlay_label='Cube', icon=script_icon, command=create_cube)
    sm.add_shelf_button(label='Slice', icon=icon_path('slice.png'), command=slice_cmd)
    sm.add_shelf_button(label='Mirror', icon=icon_path('mirror.png'), command=mirror_cmd)
    sm.add_shelf_button(label='Quadrangulate', overlay_label='Quad', icon=script_icon, command=quadrangulate)
    sm.add_shelf_button(label='Merge Vertices', overlay_label='Merge', icon=script_icon, command=merge_vertices)
    sm.add_shelf_button(label='Select Triangles', overlay_label='Tris', icon=script_icon, command=select_triangles)
    sm.add_shelf_button(label='Select Ngons', overlay_label='Ngons', icon=script_icon, command=select_ngons)
    sm.add_separator()
    sm.add_label('Nodes')
    sm.add_shelf_button(label='Super Reset', overlay_label='SpRst', icon=script_icon, command=super_reset)
    sm.add_shelf_button(label='Pivot To Base', overlay_label='Pv->B', icon=script_icon, command=pivot_base)
    sm.add_shelf_button(label='Pivot To Center', overlay_label='Pv->C', icon=script_icon, command=pivot_center)
    sm.add_shelf_button(label='Pivot To Origin', overlay_label='Pv->O', icon=script_icon, command=pivot_origin)
    sm.add_shelf_button(label='Move To Origin', overlay_label='>Orig', icon=script_icon, command=move_to_origin)


def delete_robotools_shelf():
    """
    Remove the shelf
    """
    shelf_manager.ShelfManager(ROBOTOOLS_SHELF_NAME).delete()


def rebuild_robotools_shelf():
    """
    Delete and rebuild the robotools shelf
    """
    delete_robotools_shelf()
    setup_robotools_shelf()


class RobotoolsHotkeyManager(hotkey_utils.HotkeyManager):
    def __init__(self):
        super(RobotoolsHotkeyManager, self).__init__(name=ROBOTOOLS_TITLE, path=ROBOTOOLS_HOTKEYS)

    def init_hotkeys(self):
        """
        Set up the hotkeys
        """
        self.set_hotkey('hotkeyPrefs', annotation='Mirror Geometry', mel_command='HotkeyPreferencesWindow',
                        key='H', cmd=True, ctrl=True, overwrite=True)
        self.set_hotkey('appendToPoly', annotation='Append To Poly', mel_command='AppendToPolygonTool',
                        key='A', cmd=True, overwrite=True)
        self.set_hotkey('createPoly', annotation='Create Polygon Tool', mel_command='CreatePolygonTool',
                        key='C', cmd=True, overwrite=True)
        self.set_hotkey('combine', annotation='Combine', mel_command='CombinePolygons',
                        key='A', ctrl=True, alt=True, overwrite=True)
        self.set_hotkey('mergeVertices', annotation='Merge Vertices', mel_command='PolyMergeVertices',
                        key='W', cmd=True, overwrite=True)
