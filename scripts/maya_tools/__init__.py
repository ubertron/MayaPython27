from pymel.core import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
MAYA_REQUIREMENTS = PROJECT_ROOT.joinpath('requirements.txt')
SITE_PACKAGES = PROJECT_ROOT.joinpath('site-packages')
MODELS_FOLDER = PROJECT_ROOT.joinpath('models')
SCENES_FOLDER = PROJECT_ROOT.joinpath('scenes')
ICON_FOLDER = PROJECT_ROOT.joinpath('icons')


def icon_path(icon_file):
    return ICON_FOLDER.joinpath(icon_file)
