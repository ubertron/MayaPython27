import platform
import sys
import os

from maya.OpenMayaUI import MQtUtil
from shiboken2 import wrapInstance, getCppPointer
from PySide2.QtWidgets import QWidget
from pymel.core import Path


PROJECT_ROOT = Path(__file__).parent.parent.parent
SITE_PACKAGES = PROJECT_ROOT.joinpath('site-packages')
REQUIREMENTS = PROJECT_ROOT.joinpath('requirements.txt')


MAYA_MAIN_WINDOW = wrapInstance(int(MQtUtil.mainWindow()), QWidget)


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
