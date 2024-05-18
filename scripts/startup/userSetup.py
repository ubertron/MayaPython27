import logging
import pymel.core as pm


def main():
    logging.info('>>> Git userSetup.py script')
    logging.info('>>> Installing plug-ins')
    plug_ins = ['robotools_shelf']

    for plug_in in plug_ins:
        if not pm.pluginInfo(plug_in, query=True, loaded=True):
            pm.loadPlugin(plug_in, quiet=True)
            pm.pluginInfo(plug_in, edit=True, autoload=True)


pm.evalDeferred(main)
