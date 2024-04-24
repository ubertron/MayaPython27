import os
import xml.etree.ElementTree as ET


CURRENT_PATH = os.path.realpath(__file__)
BIN_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(CURRENT_PATH))), 'bin')
DEFAULT_FBX_PRESET_PATH = os.path.join(BIN_FOLDER, 'default.fbxexportpreset')
USER_DIRECTORY = os.path.expanduser('~')
FBX_PRESET_FOLDER = os.path.join(USER_DIRECTORY, 'Library/Preferences/Autodesk/maya/FBX/Presets/2018.1.1/export')
FBX_PRESETS = [preset for preset in os.listdir(FBX_PRESET_FOLDER) if preset.endswith('.fbxexportpreset')]


def fbx_path_info():
    print(DEFAULT_FBX_PRESET_PATH, os.path.isfile(DEFAULT_FBX_PRESET_PATH))
    print(FBX_PRESET_FOLDER, os.path.isdir(FBX_PRESET_FOLDER))


def list_fbx_presets():
    print('\n'.join(FBX_PRESETS))


class FbxExportPreset:
    def __init__(self, path):
        self.path = path
        self.tree = ET.parse(self.path)
        # print(self.path, self.name)
        # print(self.preset_selected)
        print(self.include_lights, self.include_cameras, self.include_audio, self.embed_texture)
        print(self.total_units_scale)

    @property
    def root(self):
        return self.tree.getroot()

    @property
    def preset_selected(self):
        return self.get_value(self.root.find('PlugInGrp').find('PresetSelected'))

    @staticmethod
    def get_datatype(element):
        return {item[0]: item[1] for item in element.attrib.items()}['dt']

    def get_value(self, element):
        result = {item[0]: item[1] for item in element.attrib.items()}.get('v')
        return result == '1' if self.get_datatype(element) == 'Bool' else result

    @property
    def name(self):
        return os.path.basename(self.path).split('.')[0]

    @property
    def attrs(self):
        return self.root.find('IncludeGrp')

    @property
    def advanced(self):
        return self.root.find('AdvOptGrp')

    @property
    def geometry_element(self):
        return self.attrs.find('Geometry')

    @property
    def smoothing_groups(self):
        return self.get_value(self.geometry_element.find('SmoothingGroups'))

    @property
    def hard_edges(self):
        return self.get_value(self.geometry_element.find('expHardEdges'))

    @property
    def tangents_and_binormals(self):
        return self.get_value(self.geometry_element.find('TangentsandBinormals'))

    @property
    def smooth_mesh(self):
        return self.get_value(self.geometry_element.find('SmoothMesh'))

    @property
    def selection_set(self):
        return self.get_value(self.geometry_element.find('SelectionSet'))

    @property
    def blind_data(self):
        return self.get_value(self.geometry_element.find('BlindData'))

    @property
    def animation_only(self):
        return self.get_value(self.geometry_element.find('AnimationOnly'))

    @property
    def preserve_instances(self):
        return self.get_value(self.geometry_element.find('Instances'))

    @property
    def container_objects(self):
        return self.get_value(self.geometry_element.find('ContainerObjects'))

    @property
    def triangulate(self):
        return self.get_value(self.geometry_element.find('Triangulate'))

    @property
    def convert_nurbs(self):
        return self.get_value(self.geometry_element.find('GeometryNurbsSurfaceAs'))

    @property
    def animation_element(self):
        return self.attrs.find('Animation')

    @property
    def use_scene_name(self):
        return self.get_value(self.animation_element.find('ExtraGrp').find('UseSceneName'))

    @property
    def remove_single_key(self):
        return self.get_value(self.animation_element.find('ExtraGrp').find('RemoveSingleKey'))

    @property
    def quaternion_interpolation(self):
        return self.get_value(self.animation_element.find('ExtraGrp').find('Quaternion'))

    @property
    def bake_complex_animation(self):
        return self.get_value(self.animation_element.find('BakeComplexAnimation'))

    @property
    def bake_frame_start(self):
        return self.get_value(self.animation_element.find('BakeComplexAnimation').find('BakeFrameStart'))

    @property
    def bake_frame_end(self):
        return self.get_value(self.animation_element.find('BakeComplexAnimation').find('BakeFrameEnd'))

    @property
    def bake_frame_step(self):
        return self.get_value(self.animation_element.find('BakeComplexAnimation').find('BakeFrameStep'))

    @property
    def resample_animation_curves(self):
        return self.get_value(self.animation_element.find('BakeComplexAnimation').find('ResampleAnimationCurves'))

    @property
    def hide_complex_animation_baked_warning(self):
        return self.get_value(self.animation_element.find('BakeComplexAnimation').find('HideComplexAnimationBakedWarning'))

    @property
    def deformation(self):
        return self.get_value(self.animation_element.find('Deformation'))

    @property
    def deformation_skins(self):
        return self.get_value(self.animation_element.find('Deformation').find('Skins'))

    @property
    def deformation_shape(self):
        return self.get_value(self.animation_element.find('Deformation').find('Shape'))

    @property
    def curve_filter(self):
        return self.get_value(self.animation_element.find('CurveFilter'))

    @property
    def curve_filter_element(self):
        return self.animation_element.find('CurveFilter').find('CurveFilterApplyCstKeyRed')

    @property
    def constant_key_reducer(self):
        return self.get_value(self.curve_filter_element.find('CurveFilterApplyCstKeyRed'))

    @property
    def translation_precision(self):
        return self.get_value(self.curve_filter_element.find('CurveFilterCstKeyRedTPrec'))

    @property
    def rotation_precision(self):
        return self.get_value(self.curve_filter_element.find('CurveFilterCstKeyRedRPrec'))

    @property
    def scaling_precision(self):
        return self.get_value(self.curve_filter_element.find('CurveFilterCstKeyRedSPrec'))

    @property
    def other_precision(self):
        return self.get_value(self.curve_filter_element.find('CurveFilterCstKeyRedOPrec'))

    @property
    def auto_tangents_only(self):
        return self.get_value(self.curve_filter_element.find('AutoTangentsOnly'))

    @property
    def point_cache(self):
        return self.get_value(self.animation_element.find('PointCache'))

    @property
    def selection_set_name_as_point_cache(self):
        return self.get_value(self.animation_element.find('PointCache').find('SelectionSetNameAsPointCache'))

    @property
    def constraints(self):
        return self.get_value(self.animation_element.find('ConstraintsGrp').find('Constraint'))

    @property
    def skeleton_definitions(self):
        return self.get_value(self.animation_element.find('ConstraintsGrp').find('Character'))

    @property
    def include_cameras(self):
        return self.get_value(self.attrs.find('CameraGrp').find('Camera'))

    @property
    def include_lights(self):
        return self.get_value(self.attrs.find('LightGrp').find('Light'))

    @property
    def include_audio(self):
        return self.get_value(self.attrs.find('Audio'))

    @property
    def embed_texture(self):
        return self.get_value(self.attrs.find('EmbedTextureGrp').find('EmbedTexture'))

    @property
    def bind_pose(self):
        return self.get_value(self.attrs.find('BindPose'))

    @property
    def pivot_to_nulls(self):
        return self.get_value(self.attrs.find('PivotToNulls'))

    @property
    def bypass_rrs_inheritance(self):
        return self.get_value(self.attrs.find('BypassRrsInheritance'))

    @property
    def include_children(self):
        return self.get_value(self.attrs.find('InputConnectionsGrp').find('IncludeChildren'))

    @property
    def input_connections(self):
        return self.get_value(self.attrs.find('InputConnectionsGrp').find('InputConnections'))

    @property
    def total_units_scale(self):
        return self.get_value(self.advanced.find('UnitsGrp').find('TotalUnitsScale'))

    @property
    def dynamic_scale_conversion(self):
        return self.get_value(self.advanced.find('UnitsGrp').find('DynamicScaleConversion'))

    @property
    def units_selector(self):
        return self.get_value(self.advanced.find('UnitsGrp').find('UnitsSelector'))

    @property
    def up_axis(self):
        return self.get_value(self.advanced.find('AxisConvGrp').find('UpAxis'))

    @property
    def show_warnings_manager(self):
        return self.get_value(self.advanced.find('UI').find('ShowWarningsManager'))

    @property
    def generate_log_data(self):
        return self.get_value(self.advanced.find('UI').find('GenerateLogData'))

    @property
    def plugin_versions_url(self):
        return self.get_value(self.advanced.find('UI').find('PluginVersionsURL'))

    @property
    def ascii_fbx(self):
        return self.get_value(self.advanced.find('Fbx').find('AsciiFbx'))

    @property
    def export_file_version(self):
        return self.get_value(self.advanced.find('Fbx').find('ExportFileVersion'))

    @property
    def dxf_deformation(self):
        return self.get_value(self.advanced.find('Dxf').find('Deformation'))

    @property
    def dxf_triangulate(self):
        return self.get_value(self.advanced.find('Dxf').find('Triangulate'))

    @property
    def collada_triangulate(self):
        return self.get_value(self.advanced.find('Collada').find('Triangulate'))

    @property
    def collada_single_matrix(self):
        return self.get_value(self.advanced.find('Collada').find('SingleMatrix'))

    @property
    def collada_frame_rate(self):
        return self.get_value(self.advanced.find('Collada').find('FrameRate'))

    @property
    def custom_properties(self):
        return self.get_value(self.root.find('FBXExtentionsSDK').find('FBXExtentionsSDKWarning'))


preset = FbxExportPreset(path=os.path.join(FBX_PRESET_FOLDER, FBX_PRESETS[2]))
