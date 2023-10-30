import os
import sys
import subprocess
import platform

from maya_tools.paths import MAYA_REQUIREMENTS, SITE_PACKAGES
from maya import mel


def get_maya_python_interpreter_path():
    return os.path.join(os.path.dirname(sys.executable), 'mayapy.exe')


MAYA_INTERPRETER_PATH = get_maya_python_interpreter_path()
PLATFORM_SEPARATOR = ':' if platform.system() == 'Darwin' else ';'


def install_maya_requirements(output=True):
    """
    pip installs Maya modules from a requirements file
    n.b. pip install won't work with Python 2.7 because the wheels have been discontinued
    @param output:
    """
    cmds = [MAYA_INTERPRETER_PATH, '-m', 'pip', 'install', '-r', MAYA_REQUIREMENTS, '-t',
            SITE_PACKAGES]

    CREATE_NO_WINDOW = 0x08000000
    subprocess.run(cmds, text=True, creationflags=CREATE_NO_WINDOW)
    requirements = [x.strip() for x in open(MAYA_REQUIREMENTS, 'r').readlines()]

    if output:
        requirements_string = ", ".join(x for x in requirements)
        logging.info('Requirements installed: %s' % requirements_string)
    return requirements


def get_environment_variable(variable_name):
    """
    Get a list of the values for an environment variable
    @param variable_name:
    @return:
    """
    result = mel.eval('getenv "%s"' % variable_name).split(PLATFORM_SEPARATOR)
    return [x for x in result if x != '']


def set_environment_variable(variable_name, value_list):
    """
    Set an environment variable with a list of values
    @param variable_name:
    @param value_list:
    """
    mel.eval('putenv "%s" "%s"' % (variable_name, PLATFORM_SEPARATOR.join(value_list)))
