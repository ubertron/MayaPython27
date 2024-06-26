import os
import shutil
import maya.api.OpenMaya as om
import logging
import platform

# from core_tools.system_paths import SITE_PACKAGES, REQUIREMENTS
from maya_tools import MAYA_INTERPRETER_PATH, SITE_PACKAGES, REQUIREMENTS

DARWIN = 'Darwin'
PLATFORM_SEPARATOR = ':' if platform.system() == DARWIN else ';'


def maya_useNewAPI():
    """
    The presence of this function tells Maya that the plugin produces, and
    expects to be passed, objects created using the Maya Python API 2.0.
    """
    pass


# command
class RobotoolsShelfInitializeCmd(om.MPxCommand):
    kPluginCmdName = 'RobotoolsShelfInitialize'

    def __init__(self):
        om.MPxCommand.__init__(self)

    @staticmethod
    def cmdCreator():
        return RobotoolsShelfInitializeCmd()

    def doIt(self, args):
        raise Exception('Plugin not supposed to be invoked - only loaded or unloaded.')


def initializePlugin(plugin):
    """
    Initialize the plug-in
    @param plugin:
    """
    vendor = 'Robonobo'
    version = '1.1'
    pluginFn = om.MFnPlugin(plugin, vendor, version)

    try:
        bootstrap()
        pluginFn.registerCommand(RobotoolsShelfInitializeCmd.kPluginCmdName, RobotoolsShelfInitializeCmd.cmdCreator)
    except RuntimeError:
        raise RuntimeError('Failed to register command: %s\n' % RobotoolsShelfInitializeCmd.kPluginCmdName)


def uninitializePlugin(plugin):
    """
    Uninitialize the plugin
    @param plugin:
    """
    pluginFn = om.MFnPlugin(plugin)

    try:
        teardown()
        pluginFn.deregisterCommand(RobotoolsShelfInitializeCmd.kPluginCmdName)
    except RuntimeError:
        raise RuntimeError('Failed to unregister command: {}\n'.format(RobotoolsShelfInitializeCmd.kPluginCmdName))


def bootstrap():
    """
    Set up Robotools
    """
    requirements = install_requirements()
    logging.info('>>> Requirements installed: {}'.format(', '.join(requirements)))

    from maya_tools import robotools_utils

    robotools_utils.setup_robotools_shelf()
    hotkey_manager = robotools_utils.RobotoolsHotkeyManager()

    if hotkey_manager.exists:
        logging.info('>>> Hotkeys imported')
        hotkey_manager.import_set()
    else:
        logging.info('>>> Hotkey preferences file created')
        hotkey_manager.init_hotkeys()
        hotkey_manager.export_set()


def install_requirements():
    """
    Install requirements to the site-packages directory
    @return:
    """
    if not SITE_PACKAGES.exists():
        os.mkdir(SITE_PACKAGES)

    cmd = '{} -m pip install -r {} -t {} --upgrade'.format(MAYA_INTERPRETER_PATH, REQUIREMENTS, SITE_PACKAGES)
    print('Terminal command: {}'.format(cmd))
    os.system(cmd)

    return [x.strip() for x in open(REQUIREMENTS, 'r').readlines()]


def uninstall_requirements():
    """
    Uninstall requirements and delete site-packages directory
    """
    cmd = '{} -m pip uninstall -r {}'.format(MAYA_INTERPRETER_PATH, REQUIREMENTS)
    os.system(cmd)
    shutil.rmtree(SITE_PACKAGES)


def teardown():
    """
    Reverse the bootstrapping to unload the plug-in
    """
    from maya_tools import robotools_utils

    robotools_utils.delete_robotools_shelf()
    logging.info('>>> Removing Robotools Shelf')
    robotools_utils.RobotoolsHotkeyManager().delete_set()
    logging.info('>>> Deleting Robotools Hotkeys')
    # uninstall_requirements()
    # logging.info('>>> Uninstalling packages')
