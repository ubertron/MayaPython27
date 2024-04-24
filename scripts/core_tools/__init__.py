import os
import sys
import platform

from pymel.core import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
REQUIREMENTS = PROJECT_ROOT.joinpath('requirements.txt')
SITE_PACKAGES = PROJECT_ROOT.joinpath('site-packages')


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
