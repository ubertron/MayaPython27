import os
import logging
import pymel.core as pm
import maya.mel as mel


logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


CURRENT_PATH = os.path.realpath(__file__)
USER_DIRECTORY = os.path.expanduser('~')
FBX_FACTORY_PRESET_FOLDER = '/Applications/Autodesk/maya2018/plug-ins/fbx/plug-ins/FBX/Presets/export'
FBX_CUSTOM_PRESET_FOLDER = os.path.join(USER_DIRECTORY, 'Library/Preferences/Autodesk/maya/FBX/Presets/2018.1.1/export')
FBX_FACTORY_PRESETS = [preset for preset in os.listdir(FBX_FACTORY_PRESET_FOLDER) if preset.endswith('.fbxexportpreset')]
FBX_LOCAL_PRESET_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'resources/fbx_presets')
DEFAULT_FBX_PRESET_PATH = os.path.join(FBX_LOCAL_PRESET_FOLDER, 'default.fbxexportpreset')
FBX_PRESET_CHARACTER_ANIMATION = os.path.join(FBX_LOCAL_PRESET_FOLDER, 'character_animation.fbxexportpreset')
FBX_PRESET_CHARACTER_RIG = os.path.join(FBX_LOCAL_PRESET_FOLDER, 'character_rig.fbxexportpreset')


class FbxPresetDefinition:
    character_animation = FBX_PRESET_CHARACTER_ANIMATION
    character_rig = FBX_PRESET_CHARACTER_RIG


def fbx_path_info():
    logging.info(DEFAULT_FBX_PRESET_PATH, os.path.isfile(DEFAULT_FBX_PRESET_PATH))
    logging.info(FBX_FACTORY_PRESET_FOLDER, os.path.isdir(FBX_FACTORY_PRESET_FOLDER))


class FBXProperty:
    FBXExportAnimationOnly = "FBXExportAnimationOnly"  # bool
    FBXExportApplyConstantKeyReducer = "FBXExportApplyConstantKeyReducer"  # bool
    FBXExportAxisConversionMethod = "FBXExportAxisConversionMethod"  # [none|convertAnimation|addFbxRoot]
    FBXExportBakeComplexAnimation = "FBXExportBakeComplexAnimation"  # bool
    FBXExportBakeComplexEnd = "FBXExportBakeComplexEnd"  # int
    FBXExportBakeComplexStart = "FBXExportBakeComplexStart"  # int
    FBXExportBakeComplexStep = "FBXExportBakeComplexStep"  # int
    FBXExportBakeResampleAnimation = "FBXExportBakeResampleAnimation"  # bool
    FBXExportCacheFile = "FBXExportCacheFile"  # bool
    FBXExportCameras = "FBXExportCameras"  # bool
    FBXExportColladaFrameRate = "FBXExportColladaFrameRate"  # float
    FBXExportColladaSingleMatrix = "FBXExportColladaSingleMatrix"  # bool
    FBXExportColladaTriangulate = "FBXExportColladaTriangulate"  # bool
    FBXExportConstraints = "FBXExportConstraints"  # bool
    FBXExportConvertUnitString = "FBXExportConvertUnitString"  # [mm|dm|cm|m|km|In|ft|yd|mi]
    FBXExportDxfTriangulate = "FBXExportDxfTriangulate"  # bool
    FBXExportDxfDeformation = "FBXExportDxfDeformation"  # bool
    FBXExportEmbeddedTextures = "FBXExportEmbeddedTextures"  # bool
    FBXExportFileVersion = "FBXExportFileVersion"  # -v [version]
    FBXExportGenerateLog = "FBXExportGenerateLog"  # bool
    FBXExportHardEdges = "FBXExportHardEdges"  # bool
    FBXExportInAscii = "FBXExportInAscii"  # bool
    FBXExportIncludeChildren = "FBXExportIncludeChildren"  # bool
    FBXExportInputConnections = "FBXExportInputConnections"  # bool
    FBXExportInstances = "FBXExportInstances"  # bool
    FBXExportLights = "FBXExportLights"  # bool
    FBXExportQuaternion = "FBXExportQuaternion"  # bool
    FBXExportQuickSelectSetAsCache = "FBXExportQuickSelectSetAsCache" # -v "setName"
    FBXExportReferencedAssetsContent = "FBXExportReferencedAssetsContent"  # bool
    FBXExportScaleFactor = "FBXExportScaleFactor"  # float
    FBXExportShapes = "FBXExportShapes"  # bool
    FBXExportSkeletonDefinitions = "FBXExportSkeletonDefinitions"  # bool
    FBXExportSkins = "FBXExportSkins"  # bool
    FBXExportSmoothingGroups = "FBXExportSmoothingGroups"  # bool
    FBXExportSmoothMesh = "FBXExportSmoothMesh"  # bool
    FBXExportSplitAnimationIntoTakes = "FBXExportSplitAnimationIntoTakes"  # -v \"take_name\" 1 5 (see documentation)
    FBXExportTangents = "FBXExportTangents"  # bool
    FBXExportTriangulate = "FBXExportTriangulate"  # bool
    FBXExportUpAxis = "FBXExportUpAxis"  # [y|z]
    FBXExportUseSceneName = "FBXExportUseSceneName"  # bool


def formatFBXProperties():
    logging.info(pm.other.FBXProperties())


def fbxResetExport():
    mel.eval("FBXResetExport")


def fbxFileVersion():
    mel.eval("FBXExportFileVersion")


def list_fbx_factory_presets():
    logging.info("FBX Presets:\n- " + "\n- ".join(FBX_FACTORY_PRESETS))


def load_fbx_preset(preset_path):
    """
    Loads an FBX preset file
    """
    assert os.path.isfile(preset_path), "Cannot find preset: {}".format(preset_path)
    command = "FBXLoadExportPresetFile -f \"{}\";".format(preset_path)
    logging.info(command)

    try:
        pm.mel.eval(command)
    except RuntimeError as err:
        pm.warning("Failed to load FBX preset: {}".format(err))


def exportFBX(export_path, selected=True, verbose=False):
    try:
        pm.mel.FBXExport(s=selected, f=export_path)
        if verbose:
            logging.info("Export success: {}".format(export_path))

    except RuntimeError as err:
        logging.error("Export failed: {}".format(err))


def load_fbx_preset_character_rig():
    load_fbx_preset(FBX_PRESET_CHARACTER_RIG)


def load_fbx_preset_character_animation(start=0, end=150):
    load_fbx_preset(FBX_PRESET_CHARACTER_ANIMATION)
    logging.info('Setting range to {}, {}'.format(start, end))


if __name__ == '__main__':
    logging.info(FBX_PRESET_CHARACTER_RIG, os.path.isfile(FBX_PRESET_CHARACTER_RIG))
    logging.info(FBX_PRESET_CHARACTER_ANIMATION, os.path.isfile(FBX_PRESET_CHARACTER_ANIMATION))
