# https://help.autodesk.com/view/MAYAUL/2023/ENU/?guid=Maya_SDK_A_First_Plugin_Python_HelloWorldAPI2_html
import os
import sys
import maya.api.OpenMaya as om
import logging
import pymel.util
import platform

from maya import mel


ROBOTOOLS_FOLDER = os.path.join(os.path.expanduser('~'), 'Dropbox/Technology/Python2/MayaPython27')
ROBOTOOLS_SCRIPTS = os.path.join(ROBOTOOLS_FOLDER, 'scripts')
SITE_PACKAGES = os.path.join(ROBOTOOLS_FOLDER, 'site-packages')
ROBOTOOLS_PLUG_INS = os.path.join(ROBOTOOLS_FOLDER, 'plug-ins')
ENVIRONMENT_PATHS = {
    'PYTHONPATH': [ROBOTOOLS_SCRIPTS, SITE_PACKAGES],
    'MAYA_PLUG_IN_PATH': [ROBOTOOLS_PLUG_INS],
}
PLATFORM_SEPARATOR = ':' if platform.system() == 'Darwin' else ';'


def maya_useNewAPI():
    """
    The presence of this function tells Maya that the plugin produces, and
    expects to be passed, objects created using the Maya Python API 2.0.
    """
    pass


# command
class RoboToolsInitializeCmd(om.MPxCommand):
    kPluginCmdName = 'RoboToolsInitialize'

    def __init__(self):
        om.MPxCommand.__init__(self)

    @staticmethod
    def cmdCreator():
        return RoboToolsInitializeCmd()

    def doIt(self, args):
        raise Exception('Plugin not supposed to be invoked - only loaded or unloaded.')


def initializePlugin(plugin):
    """
    Initialize the plug-in
    @param plugin:
    """
    vendor = 'Robonobo'
    version = '1.0.0'
    pluginFn = om.MFnPlugin(plugin, vendor, version)
    try:
        bootstrap()
        pluginFn.registerCommand(RoboToolsInitializeCmd.kPluginCmdName, RoboToolsInitializeCmd.cmdCreator)
    except RuntimeError:
        raise RuntimeError('Failed to register command: %s\n' % RoboToolsInitializeCmd.kPluginCmdName)


def uninitializePlugin(plugin):
    """
    Uninitialize the plugin
    @param plugin:
    """
    pluginFn = om.MFnPlugin(plugin)
    try:
        teardown()
        pluginFn.deregisterCommand(RoboToolsInitializeCmd.kPluginCmdName)
    except RuntimeError:
        raise RuntimeError('Failed to unregister command: %s\n' % RoboToolsInitializeCmd.kPluginCmdName)


def bootstrap():
    """
    Set up Robotools
    """
    logging.info('-------- Robotools Bootstrapping --------')

    for path in ENVIRONMENT_PATHS['PYTHONPATH']:
        if path not in sys.path:
            sys.path.append(path)
            logging.info('Tools path added: %s' % path)

    for env_key in ENVIRONMENT_PATHS.keys():
        environment_values = get_environment_variable(env_key)
        environment_values.extend(ENVIRONMENT_PATHS[env_key])
        environment_values = list(set(environment_values))
        environment_values.sort(key=lambda x: x.lower())
        set_environment_variable(env_key, environment_values)


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


def teardown():
    """
    Reverse the bootstrapping to unload the plug-in
    """
    for path in ENVIRONMENT_PATHS['PYTHONPATH']:
        if path in sys.path:
            sys.path.remove(path)

    for env_key in ENVIRONMENT_PATHS.keys():
        environment_values = get_environment_variable(env_key)
        reduced = [path for path in environment_values if path not in ENVIRONMENT_PATHS[env_key]]
        set_environment_variable(env_key, reduced)
