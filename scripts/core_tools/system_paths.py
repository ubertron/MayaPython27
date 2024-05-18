import os
import logging

from core_tools import system_utils
from core_tools.environment_utils import get_env_value

if system_utils.is_using_maya_python():
    from pymel.core import Path
else:
    from pathlib import Path

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


PROJECT_ROOT = Path(__file__).parent.parent.parent
ICON_FOLDER = PROJECT_ROOT.joinpath('icons')
MODELS_FOLDER = PROJECT_ROOT.joinpath('models')
REQUIREMENTS = PROJECT_ROOT.joinpath(PROJECT_ROOT, 'requirements.txt')
SCENES_FOLDER = PROJECT_ROOT.joinpath('scenes')
SITE_PACKAGES = PROJECT_ROOT.joinpath(PROJECT_ROOT, 'site-packages')
ENGINE_ROOT_KEY = 'ENGINE_ROOT'
ENGINE_ROOT = Path(get_env_value(ENGINE_ROOT_KEY))


def inspect_path(path):
    """
    Log info about a path
    @param path:
    """
    logging.info("{}: Exists? {}".format(path, path.exists()))


def icon_path(icon_file):
    """
    Returns an absolute path for an icon file
    @param icon_file:
    @return:
    """
    return ICON_FOLDER.joinpath(icon_file)


if __name__ == '__main__':
    inspect_path(PROJECT_ROOT)
    inspect_path(REQUIREMENTS)
    inspect_path(SITE_PACKAGES)
