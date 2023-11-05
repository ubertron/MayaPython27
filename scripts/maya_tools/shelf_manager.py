import pymel.core as pm
import inspect
import logging

from maya import mel

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

_DEBUG_MODE = False


class ShelfManager:
    TOP_LEVEL_SHELF = mel.eval('$tmpVar=$gShelfTopLevel')

    def __init__(self, name):
        self.name = name

    @property
    def shelf_names(self):
        return pm.tabLayout(self.TOP_LEVEL_SHELF, query=True, childArray=True)

    @property
    def current_button_labels(self):
        return [pm.shelfButton(x, query=True, label=True) for x in self.current_buttons]

    @property
    def current_buttons(self):
        shelf_contents = pm.shelfLayout(self.name, query=True, childArray=True)
        return [] if shelf_contents is None else [x for x in shelf_contents if 'shelfButton' in x]

    @property
    def tab_index(self):
        return self.shelf_names.index(self.name) + 1 if self.name in self.shelf_names else None

    def create(self, select=False):
        """
        Add the shelf to the ui
        :param select:
        """
        if self.name not in self.shelf_names:
            pm.shelfLayout(self.name, parent=self.TOP_LEVEL_SHELF)
            if select:
                self.select_tab_index()

    def delete(self):
        """
        Remove the shelf from the ui
        """
        if self.name in self.shelf_names:
            pm.deleteUI(self.name)

    def select_tab_index(self, tab_index=None):
        """
        Set the currently selected shelf tab
        :param tab_index:
        """
        if tab_index is not None:
            assert tab_index <= len(self.shelf_names), 'Invalid index'
        pm.shelfTabLayout(self.TOP_LEVEL_SHELF, edit=True, selectTabIndex=tab_index if tab_index else self.tab_index)

    def select_tab_name(self, name=None):
        """
        Select the current tab by name
        :param name: str
        """
        if name is not None:
            assert name in self.shelf_names, 'Invalid shelf name'
        pm.shelfTabLayout(self.TOP_LEVEL_SHELF, edit=True, selectTab=name if name else self.name)

    def add_shelf_button(self, label, icon, command='', overlay_label=None, overwrite=True):
        """
        Add a button to the current shelf
        :param label: str
        :param icon: Path
        :param command: str
        :param overlay_label: str
        :param overwrite: bool
        """
        if label in self.current_button_labels and overwrite:
            self.delete_button(label=label)

        button = pm.shelfButton(label=label, image1=icon, parent=self.name, command=command,
                                overlayLabelBackColor=(0, 0, 0, 0))
        if overlay_label:
            button.setImageOverlayLabel(overlay_label)

    def add_separator(self):
        """
        Add a separator to the current shelf
        """
        pm.setParent(self.name)
        pm.separator(width=12, height=35, horizontal=False)

    def delete_button(self, label):
        """
        Delete a button by label
        :param label:
        """
        button = next((x for x in self.current_buttons if pm.shelfButton(x, query=True, label=True) == label), None)
        if button:
            pm.deleteUI(button)

    def delete_buttons(self):
        """
        Delete all buttons in shelf
        """
        for button in self.buttons:
            pm.deleteUI(button)

    @property
    def buttons(self):
        buttons = pm.shelfLayout(self.name, query=True, childArray=True)
        return buttons if buttons is not None else []


def build_shelf_command(function, script, imports=None):
    """
    Creates a text script incorporating a function, a function call and an optional import header
    The command can be executed by Maya shelf buttons
    :param function:
    :param script:
    :param imports:
    :return:
    """
    import_string = '{}\n\n'.format(imports) if imports else ''
    return '{}{}\n\n{}'.format(import_string, inspect.getsource(function), script)


