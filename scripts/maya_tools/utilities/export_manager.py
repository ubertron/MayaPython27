import os.path

from widgets import generic_widget
from PySide2.QtWidgets import QSizePolicy, QTabWidget
from core_tools.system_utils import is_using_maya_python


if is_using_maya_python():
    from pymel.core import Path
else:
    from pathlib import Path

HOME_DIR = os.path.expanduser('~')
PROJECT_ROOT = Path(HOME_DIR).joinpath('Dropbox/Projects/Unity/AnimationManager')
MAYA_EXTENSION = '.mb'


class ExportManager(generic_widget.GenericWidget):
    def __init__(self, project_root=PROJECT_ROOT):
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

        self.project_root = project_root
        self.resize(480, 240)

    @property
    def project_root(self):
        return self._project_root

    @project_root.setter
    def project_root(self, path):
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
        return PROJECT_ROOT if self.parent_widget is None else self.parent_widget.project_root

    @property
    def source_art(self):
        return PROJECT_ROOT.joinpath('SourceArt')

    @property
    def exports(self):
        return PROJECT_ROOT.joinpath('Assets/Models')

    @property
    def asset_folders(self):
        if is_using_maya_python():
            return [x for x in os.listdir(self.source_art)
                    if os.path.isdir(os.path.join(self.source_art, x))]
        else:
            return [x.name for x in self.source_art.iterdir() if x.is_dir()]

    def check_asset_folder(self, folder_name):
        abs_path = self.source_art.joinpath(folder_name)

        if is_using_maya_python():
            scene_files = [x for x in os.listdir(abs_path) if os.path.isfile(os.path.join(abs_path, x))]
        else:
            scene_files = [x.name for x in abs_path.iterdir() if x.is_file and x.suffix == MAYA_EXTENSION]

        print(scene_files)

    def collect_asset_data(self):
        characters = {}

        # browse all the scene folders for Maya files and export data
        for folder in self.asset_folders:
            self.check_asset_folder(folder)

        # check the export folder
        info = 'Project root: {}\nAsset folders:\n'.format(self.project_root)
        info += '\n'.join(self.asset_folders)
        self.label.setText(info)


class EnvironmentExporter(generic_widget.GenericWidget):
    def __init__(self, parent=None):
        super(EnvironmentExporter, self).__init__('Environment Exporter')
        self.parent_widget = parent
        self.add_label('Environment Exporter coming soon...')


if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication

    app = QApplication()
    export_manager = ExportManager(PROJECT_ROOT)
    export_manager.show()
    app.exec_()

