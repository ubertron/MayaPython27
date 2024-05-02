import sys
import os


PYTHON_397 = "3.9.7"
PYTHON_PLATFORM = "python"
MAYA_PLATFORM = "maya"
UNREAL_PLATFORM = "unrealeditor"


def get_python_version():
    """
    Finds the version of Python as a string
    :return: str
    """
    version = sys.version_info
    return "{}.{}.{}".format(version.major, version.minor, version.micro)


def get_platform():
    """
    Finds the platform of Python as a string
    :return: str
    """
    return os.path.splitext(os.path.basename(sys.executable))[0].lower()


def is_using_maya_python():
    """
    Determine if code is being used in a Maya environment
    :return: bool
    """
    return get_platform() == MAYA_PLATFORM


def is_using_standalone_python():
    """
    Determine if code is being used in a standalone environment
    :return: bool
    """
    return get_platform() == PYTHON_PLATFORM


def is_using_unreal_editor_python():
    """
    Determine if code is being used in an Unreal environment
    :return: bool
    """
    return get_platform() == UNREAL_PLATFORM
