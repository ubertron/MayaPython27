import os.path

from widgets import generic_widget
from PySide2.QtWidgets import QSizePolicy, QTabWidget

from core_tools.system_utils import is_using_maya_python
from core_tools.enums import AssetType
from ams.asset import Asset
from core_tools.system_paths import ENGINE_ROOT


if is_using_maya_python():
    from pymel.core import Path
else:
    from pathlib import Path

HOME_DIR = os.path.expanduser('~')


class ExportManager(generic_widget.GenericWidget):
    def __init__(self, engine_root=ENGINE_ROOT):
        super(ExportManager, self).__init__(title='Export Manager')
        button_bar = self.add_widget(generic_widget.GenericWidget(vertical=False))
        button_bar.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.project_label = button_bar.add_label()
        button_bar.add_stretch()
        self.set_project_button = button_bar.add_button('Set Project')
        self.set_project_button.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        self.tab_bar = self.add_widget(QTabWidget())
        self.character_exporter = CharacterExporter(self)
        self.environment_exporter = EnvironmentExporter(self)
        self.tab_bar.addTab(self.character_exporter, 'Characters')
        self.tab_bar.addTab(self.environment_exporter, 'Environments')

        self.engine_root = engine_root
        self.resize(480, 240)

    @property
    def engine_root(self):
        return self._project_root

    @engine_root.setter
    def engine_root(self, path):
        self._project_root = path
        self.project_label.setText("Project: {}".format(os.path.basename(path)))


class CharacterExporter(generic_widget.GenericWidget):
    def __init__(self, parent=None):
        super(CharacterExporter, self).__init__('Character Exporter')
        self.parent_widget = parent
        top_bar = self.add_widget(generic_widget.GenericWidget(vertical=False))
        top_bar.add_button('Refresh', tool_tip='Update status info', event=self.collect_asset_data)
        top_bar.add_button('Browse...', tool_tip='Open assets in a Finder window')
        top_bar.add_stretch()
        top_bar.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.label = self.add_label('Character data...', align_center=False)
        self.label.setWordWrap(True)

    @property
    def project_root(self):
        return ENGINE_ROOT if self.parent_widget is None else self.parent_widget.engine_root

    @property
    def source_art(self):
        return ENGINE_ROOT.joinpath('SourceArt')

    @property
    def character_folder(self):
        return self.source_art.joinpath('Characters')

    @property
    def exports(self):
        return ENGINE_ROOT.joinpath('Assets/Models')

    @property
    def character_asset_folders(self):
        if is_using_maya_python():
            result = [x for x in os.listdir(self.character_folder)
                      if os.path.isdir(os.path.join(self.character_folder, x))]
        else:
            result = [x.name for x in self.character_folder.iterdir() if x.is_dir()]

        result.sort(key=lambda x: x.lower())

        return [x for x in result if not x.startswith('_')]

    def collect_asset_data(self):
        characters = []
        print(self.character_asset_folders)
        # browse all the scene folders for Maya files and export data
        for folder in self.character_asset_folders:
            asset = Asset(source_folder=self.character_folder.joinpath(folder), asset_type=AssetType.character)
            if asset.scene_file_exists:
                characters.append(asset)

        # check the export folder
        info = 'Characters ({} found):\n'.format(len(characters))
        info += '\n'.join(str(x) for x in characters)
        self.label.setText(info)


class EnvironmentExporter(generic_widget.GenericWidget):
    def __init__(self, parent=None):
        super(EnvironmentExporter, self).__init__('Environment Exporter')
        self.parent_widget = parent
        self.add_label('Environment Exporter coming soon...')


if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication

    app = QApplication()
    export_manager = ExportManager(ENGINE_ROOT)
    export_manager.show()
    app.exec_()

