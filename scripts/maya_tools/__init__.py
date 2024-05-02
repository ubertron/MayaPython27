import platform
import sys
import os

from pymel.core import Path
from maya.OpenMayaUI import MQtUtil
from shiboken2 import wrapInstance, getCppPointer
from PySide2.QtWidgets import QWidget

PROJECT_ROOT = Path(__file__).parent.parent.parent
MAYA_REQUIREMENTS = PROJECT_ROOT.joinpath('requirements.txt')
SITE_PACKAGES = PROJECT_ROOT.joinpath('site-packages')
MODELS_FOLDER = PROJECT_ROOT.joinpath('models')
SCENES_FOLDER = PROJECT_ROOT.joinpath('scenes')
ICON_FOLDER = PROJECT_ROOT.joinpath('icons')
MAYA_MAIN_WINDOW = wrapInstance(int(MQtUtil.mainWindow()), QWidget)


def icon_path(icon_file):
    return ICON_FOLDER.joinpath(icon_file)


def get_maya_python_interpreter_path():
    """
    Get the path to the Maya interpreter
    @return:
    """
    if platform.system() == 'Darwin':
        return Path(sys.executable).parent.parent.parent.joinpath('Contents', 'bin', 'mayapy')
    else:
        return Path(Path(sys.executable), 'maya.exe')


MAYA_INTERPRETER_PATH = get_maya_python_interpreter_path()