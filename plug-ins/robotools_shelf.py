import os
import sys
import maya.api.OpenMaya as om
import logging
import pymel.util
import platform

from maya import mel
from pymel.core import Path

import maya_tools.robotools_utils

PLATFORM_SEPARATOR = ':' if platform.system() == 'Darwin' else ';'


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
    version = '1.0.1'
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
        raise RuntimeError('Failed to unregister command: %s\n' % RobotoolsShelfInitializeCmd.kPluginCmdName)


def bootstrap():
    """
    Set up Robotools
    """
    from maya_tools import robotools_utils

    robotools_utils.setup_robotools_shelf()
    hotkey_manager = robotools_utils.RobotoolsHotkeyManager()

    if hotkey_manager.exists:
        logging.info('>>>> Hotkeys imported')
        hotkey_manager.import_set()
    else:
        logging.info('>>>> Hotkey preferences file created')
        hotkey_manager.init_hotkeys()
        hotkey_manager.export_set()


def teardown():
    """
    Reverse the bootstrapping to unload the plug-in
    """
    from maya_tools import shelf_manager, robotools_utils

    robotools_utils.delete_robotools_shelf()
    logging.info('>>>> Removing Robotools Shelf')
    robotools_utils.RobotoolsHotkeyManager().delete_set()
    logging.info('>>>> Deleting Robotools Hotkeys')

