import pymel.core as pm
import logging

from maya_tools.mirror_utils import slice_geometry, mirror_geometry
from maya_tools.paths import icon_path
from maya_tools.shelf_manager import ShelfManager, build_shelf_command, message_script

ROBOTOOLS_SHELF_NAME = 'Robotools'
ROBOTOOLS_SHELF_VERSION = '1.0'
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

    base_male_cmd = build_shelf_command(function=import_base_character, script='import_base_character("male")')
    base_female_cmd = build_shelf_command(function=import_base_character, script='import_base_character("female")')
    slice_cmd = build_shelf_command(function=slice_geometry, script='slice_geometry()',
                                    imports='from core_tools.enums import Axis\n'
                                            'from maya_tools.mirror_utils import slice_geometry')
    mirror_cmd = build_shelf_command(function=mirror_geometry, script='mirror_geometry()',
                                     imports='from core_tools.enums import Axis\n'
                                             'from maya_tools.mirror_utils import mirror_geometry')
    version_info = 'Robotools Shelf Version {}: {}'.format(ROBOTOOLS_SHELF_VERSION, ROBOTOOLS_SHELF_PLUG_IN_PATH)
    robonobo_icon = icon_path('robonobo_32.png')

    sm.add_shelf_button(label='About Robotools', icon=robonobo_icon, command=message_script(version_info))
    sm.add_separator()
    sm.add_shelf_button(label='Import Base Male', icon=icon_path('base_male.png'), command=base_male_cmd)
    sm.add_shelf_button(label='Import Base Female', icon=icon_path('base_female.png'), command=base_female_cmd)
    sm.add_separator()
    sm.add_shelf_button(label='Slice', icon=icon_path('slice.png'), command=slice_cmd)
    sm.add_shelf_button(label='Mirror', icon=icon_path('mirror.png'), command=mirror_cmd)


def import_base_character(gender):
    """
    Import a base character
    @param gender:
    """
    import pymel.core as pm

    from maya_tools.scene_utils import import_model
    from maya_tools.paths import MODELS_FOLDER

    import_path = MODELS_FOLDER.joinpath('base_mesh_male.fbx' if gender == 'male' else 'base_mesh_female.fbx')
    result = import_model(import_path=import_path)
    transform = next(x for x in result if type(x) is pm.nodetypes.Transform)
    pm.select(transform)
    pm.viewFit()
    return transform


def delete_robotools_shelf():
    """
    Remove the shelf
    """
    logging.info('>>>>>>>>>>>>>>> Removing Robotools Shelf')
    ShelfManager(ROBOTOOLS_SHELF_NAME).delete()
