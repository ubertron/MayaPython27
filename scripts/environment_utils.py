import os
import sys
import subprocess
from resource_paths import MAYA_REQUIREMENTS, SITE_PACKAGES


def get_maya_python_interpreter_path():
    return os.path.join(os.path.dirname(sys.executable), 'mayapy.exe')


MAYA_INTERPRETER_PATH = get_maya_python_interpreter_path()


def install_maya_requirements(output=True):
    """
    pip installs Maya modules from a requirements file
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
