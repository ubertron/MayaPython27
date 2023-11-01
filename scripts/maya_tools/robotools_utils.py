# Version 1.0 - initial release
# Version 1.1 - removed local character import script, put invocation in the command

import pymel.core as pm
import logging

from pymel.core.system import Path

from maya_tools.paths import icon_path
from maya_tools.shelf_manager import ShelfManager, message_script

ROBOTOOLS_SHELF_NAME = 'Robotools'
ROBOTOOLS_SHELF_VERSION = '1.1'
ROBOTOOLS_SHELF_PLUG_IN = 'robotools_shelf'
ROBOTOOLS_SHELF_PLUG_IN_PATH = str(pm.pluginInfo(ROBOTOOLS_SHELF_PLUG_IN, query=True, path=True))


def setup_robotools_shelf():
    """
    Sets up the Robotools shelf
    """
    logging.info('>>>>>>>>>>>>>>> Loading Robotools Shelf')
    sm = ShelfManager(ROBOTOOLS_SHELF_NAME)
    sm.delete()
    sm.create(select=True)
    sm.delete_buttons()

    version_info = 'Robotools Shelf Version {}: {}'.format(ROBOTOOLS_SHELF_VERSION, ROBOTOOLS_SHELF_PLUG_IN_PATH)
    robonobo_icon = icon_path('robonobo_32.png')
    base_male_cmd = 'from maya_tools.character_utils import import_base_character\nimport_base_character("male")'
    base_female_cmd = 'from maya_tools.character_utils import import_base_character\nimport_base_character("female")'
    slice_cmd = 'from maya_tools.mirror_utils import slice_geometry\nslice_geometry()'
    mirror_cmd = 'from maya_tools.mirror_utils import mirror_geometry\nmirror_geometry()'
    quadrangulate = 'import pymel.core as pm\npm.runtime.Quadrangulate()'
    merge_vertices = 'from maya_tools.geometry_utils import merge_vertices\nmerge_vertices'

    sm.add_shelf_button(label='About Robotools', icon=robonobo_icon, command=message_script(version_info))
    sm.add_separator()
    sm.add_shelf_button(label='Import Base Male', icon=icon_path('base_male.png'), command=base_male_cmd)
    sm.add_shelf_button(label='Import Base Female', icon=icon_path('base_female.png'), command=base_female_cmd)
    sm.add_separator()
    sm.add_shelf_button(label='Slice', icon=icon_path('slice.png'), command=slice_cmd)
    sm.add_shelf_button(label='Mirror', icon=icon_path('mirror.png'), command=mirror_cmd)
    sm.add_shelf_button(label='Quadrangulate', overlay_label='Quad', icon=robonobo_icon, command=quadrangulate)
    sm.add_shelf_button(label='Merge Vertices', overlay_label='Merge', icon=robonobo_icon, command=merge_vertices)


def delete_robotools_shelf():
    """
    Remove the shelf
    """
    logging.info('>>>>>>>>>>>>>>> Removing Robotools Shelf')
    ShelfManager(ROBOTOOLS_SHELF_NAME).delete()
