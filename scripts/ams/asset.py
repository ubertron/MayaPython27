import os
from core_tools.enums import FileExtension
from core_tools import system_utils

if system_utils.is_using_maya_python():
    from pymel.core import Path
else:
    from pathlib import Path


class Asset:
    def __init__(self, source_folder, asset_type):
        self.source_folder = source_folder
        self.asset_type = asset_type

    def __repr__(self):
        assert self.source_folder.exists(), '{} does not exist.'.format(str(self.source_folder))
        if self.scene_file_exists:
            if len(self.animations):
                return 'Scene: {} | Animations: {}'.format(self.scene_file, ', '.join(self.animations))
            else:
                return 'Scene: {}'.format(self.scene_file)
        else:
            return '{}: no assets found'.format(self.name)

    @property
    def info(self):
        assert self.source_folder.exists(), '{} does not exist.'.format(str(self.source_folder))

        info = 'Name: {} [{}]\nPath: {}'.format(self.name, self.asset_type, self.source_folder)
        info += '\nScene File: {} Exists? {}\nAnimations: '.format(self.scene_file, self.scene_file_exists)

        if len(self.animations):
            info += '\n' + '\n'.join([str(x) for x in self.animations])
        else:
            info += 'None'

        return info

    @property
    def source_folder_exists(self):
        return self.source_folder.exists()

    @property
    def name(self):
        return self.source_folder.name

    @property
    def scene_file(self):
        return '{}{}'.format(self.name, FileExtension.mb)

    @property
    def scene_file_path(self):
        return self.source_folder.joinpath(self.scene_file)

    @property
    def scene_file_exists(self):
        return self.source_folder.joinpath(self.scene_file).exists()

    @property
    def all_scene_files(self):
        return [x for x in os.listdir(self.source_folder) if x.endswith(FileExtension.mb)]

    @property
    def animations(self):
        return [x for x in self.all_scene_files if x.startswith('{}_'.format(self.name))]

    @property
    def animation_paths(self):
        return [self.source_folder.joinpath(x) for x in self.animations]


if __name__ == '__main__':
    from core_tools.enums import AssetType
    clairee_folder = Path.home().joinpath('Dropbox/Projects/Unity/AnimationManager/SourceArt/Characters/clairee')
    clairee_asset = Asset(source_folder=clairee_folder, asset_type=AssetType.character)
    print(clairee_asset)
