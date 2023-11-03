import pymel.core as pm
import os

from core_tools.enums import FileExtension, Gender
from maya_tools import MODELS_FOLDER, SCENES_FOLDER
from maya_tools.scene_utils import import_model, load_scene


BASE_MESH_MALE = 'base_mesh_male'
BASE_MESH_FEMALE = 'base_mesh_female'


def import_base_character(gender):
    """
    Import a base character
    @param gender:
    """
    file_name = '{}{}'.format(BASE_MESH_MALE if gender == 'male' else BASE_MESH_FEMALE, FileExtension.fbx)
    import_path = MODELS_FOLDER.joinpath(file_name)
    result = import_model(import_path=import_path)
    transform = next(x for x in result if type(x) is pm.nodetypes.Transform)
    pm.select(transform)
    pm.viewFit()
    return transform


def load_base_character(gender, latest=True):
    """
    Load a base character scene
    @param gender:
    @param latest:
    """
    scene_name = BASE_MESH_MALE if gender == Gender.male else BASE_MESH_FEMALE

    if latest:
        # find all the scenes
        scenes = SCENES_FOLDER.glob('{}*'.format(scene_name))
        # discount the non-versioned file
        scenes = [x for x in scenes if len(str(x).split('.')) == 3]

        if not scenes:
            pm.warning('No scenes found for {}'.format(scene_name))
            return

        # find the latest version
        scenes.sort(key=lambda x: x.split(os.sep)[-1].split('.')[1])
        scene_path = scenes[-1]
    else:
        scene_path = SCENES_FOLDER.joinpath('{}{}'.format(scene_name, FileExtension.mb))

    result = load_scene(scene_path)
    transform = next(x for x in result if type(x) is pm.nodetypes.Transform)
    pm.select(transform)
    pm.viewFit()
    return transform
