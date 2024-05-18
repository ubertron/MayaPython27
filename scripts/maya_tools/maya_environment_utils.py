import platform
import subprocess

from core_tools.system_paths import REQUIREMENTS, SITE_PACKAGES
from maya_tools import MAYA_INTERPRETER_PATH


def install_maya_requirements(output=True):
    """
    pip installs Maya modules from a requirements file
    n.b. pip install won't work with Python 2.7 because the wheels have been discontinued
    @param output:
    """
    cmds = [MAYA_INTERPRETER_PATH, '-m', 'pip', 'install', '-r', REQUIREMENTS, '-t',
            SITE_PACKAGES]

    CREATE_NO_WINDOW = 0x08000000
    subprocess.run(cmds, text=True, creationflags=CREATE_NO_WINDOW)
    requirements = [x.strip() for x in open(REQUIREMENTS, 'r').readlines()]

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


PLATFORM_SEPARATOR = ':' if platform.system() == 'Darwin' else ';'
