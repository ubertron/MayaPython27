import xml.etree.cElementTree as ET
import os
from xml.etree import ElementTree as ET

import pyperclip

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
BIN_FOLDER = os.path.join(PROJECT_ROOT, "bin")


class FbxExportPresetCreator:
    def __init__(self, name):
        self.name = name
        self.root = ET.Element("Export", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Export")
        plugin_grp = ET.SubElement(self.root, "PlugInGrp", UIH="1", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Plugin Information")
        ET.SubElement(plugin_grp, "PlugInUIWidth", UIH="1", UID="0", UIG="0", lbENU="Plugin UI Width", dt="Integer", v="500")
        ET.SubElement(plugin_grp, "PlugInUIHeight", UIH="1", UID="0", UIG="0", lbENU="Plugin UI Height", dt="Integer", v="500")
        ET.SubElement(plugin_grp, "PlugInUIXpos", UIH="1", UID="0", UIG="0", lbENU="Plugin UI X Position", dt="Integer", v="100")
        ET.SubElement(plugin_grp, "PlugInUIYpos", UIH="1", UID="0", UIG="0", lbENU="Plugin UI Y Position", dt="Integer", v="100")
        ET.SubElement(plugin_grp, "UILIndex", UIH="1", UID="0", UIG="0", lbENU="UI language", dt="Enum", enumSelected="ENU", v="0", enumItem_0="ENU", enumItem_1="DEU", enumItem_2="FRA", enumItem_3="JPN", enumItem_4="KOR", enumItem_5="CHS", enumItem_6="PTB")
        ET.SubElement(plugin_grp, "PluginProductFamily", UIH="0", UID="0", UIG="0", lbENU="Plugin product family", dt="KString", v="Maya  ( API cut number: 201708311015-002f4fe637 )")
        ET.SubElement(plugin_grp, "PresetSelected", UIH="1", UID="0", UIG="0", lbENU="Preset Selected", dt="KString", v="/Applications/Autodesk/maya2018/plug-ins/fbx/plug-ins/FBX/Presets/export/Autodesk Media &amp; Entertainment.fbxexportpreset")
        presets_group = ET.SubElement(self.root, "PresetsGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="1", lbENU="Presets")
        ET.SubElement(presets_group, "Presets", UIH="0", UID="0", UIG="0", lbENU="Current Preset", dt="Presets")
        statistics_group = ET.SubElement(self.root, "StatisticsGrp", UIH="1", UID="0", UIG="1", UIX="1", UIP="0", lbENU="Statistics")
        ET.SubElement(statistics_group, "Statistics", UIH="0", UID="0", UIG="0", lbENU="Statistics", dt="Statistics")

        include_group = ET.SubElement(self.root, "IncludeGrp", UIH="0", UID="0", UIG="1", UIX="1", UIP="0", lbENU="Include")

        geometry = ET.SubElement(include_group, "Geometry", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Geometry")
        self.smoothing_groups = ET.SubElement(geometry, "SmoothingGroups", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Smoothing Groups", dt="Bool", v="0")
        self.hard_edges = ET.SubElement(geometry, "expHardEdges",  UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Split per-vertex Normals", dt="Bool", v="0")
        self.tangents_binormals = ET.SubElement(geometry, "TangentsandBinormals", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Tangents and Binormals", dt="Bool", v="0")
        self.smooth_mesh = ET.SubElement(geometry, "SmoothMesh", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Smooth Mesh", dt="Bool", v="1")
        self.selection_set = ET.SubElement(geometry, "SelectionSet", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Selection Sets", dt="Bool", v="0")
        self.blind_data = ET.SubElement(geometry, "BlindData", UIH="1", UID="0", UIG="0", UIBG="0", lbENU="Blind Data", dt="Bool", v="1")
        self.animation_only = ET.SubElement(geometry, "AnimationOnly", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Convert to Null objects", dt="Bool", v="0")
        self.instances = ET.SubElement(geometry, "Instances", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Preserve Instances", dt="Bool", v="0")
        self.container_objects = ET.SubElement(geometry, "ContainerObjects", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Referenced Assets Content", dt="Bool", v="1")
        self.triangulate = ET.SubElement(geometry, "Triangulate", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Triangulate", dt="Bool", v="0")
        self.convert_nurbs = ET.SubElement(geometry, "GeometryNurbsSurfaceAs", UIH="0", UID="0", UIG="0", lbENU="Convert NURBS surface to", dt="Enum", enumSelected="NURBS", v="0", enumItem_0="NURBS", enumItem_1="Interactive Display Mesh", enumItem_2="Software Render Mesh")

        self.animation = ET.SubElement(include_group, "Animation", UIH="0", UID="0", UIG="0", UIBG="1", UIX="0", lbENU="Animation", dt="Bool", v="1")
        extra_group = ET.SubElement(self.animation, "ExtraGrp", UIH="0", UID="0", UIG="1", UIX="1", UIP="0", lbENU="Extra Options")
        self.use_scene_names = ET.SubElement(extra_group, "UseSceneName", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Use scene name", dt="Bool", v="0")
        self.remove_single_key = ET.SubElement(extra_group, "RemoveSingleKey", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Remove single key", dt="Bool", v="0")
        self.quaternion = ET.SubElement(extra_group, "Quaternion", UIH="0", UID="0", UIG="0", lbENU="Quaternion Interpolation Mode", dt="Enum", enumSelected="Resample As Euler Interpolation", v="2", enumItem_0="Retain Quaternion Interpolation", enumItem_1="Set As Euler Interpolation", enumItem_2="Resample As Euler Interpolation")
        self.bake_complex_animation = ET.SubElement(self.animation, "BakeComplexAnimation", UIH="0", UID="0", UIG="0", UIBG="1", UIX="1", lbENU="Bake Animation", dt="Bool", v="0")
        self.bake_frame_start = ET.SubElement(self.bake_complex_animation, "BakeFrameStart", UIH="0", UID="0", UIG="0", lbENU="Start", dt="Integer", v="1")
        self.bake_frame_end = ET.SubElement(self.bake_complex_animation, "BakeFrameEnd", UIH="0", UID="0", UIG="0", lbENU="End", dt="Integer", v="200")
        self.bake_frame_step = ET.SubElement(self.bake_complex_animation, "BakeFrameStep", UIH="0", UID="0", UIG="0", lbENU="Step", dt="Integer", v="1")
        self.resample_animation_curves = ET.SubElement(self.bake_complex_animation, "ResampleAnimationCurves", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Resample All", dt="Bool", v="0")
        self.hide_complex_animation_warning = ET.SubElement(self.bake_complex_animation, "HideComplexAnimationBakedWarning", UIH="1", UID="0", UIG="0", UIBG="0", lbENU="Hide Complex Animation Baked Warning", dt="Bool", v="0")
        self.deformation = ET.SubElement(self.animation, "Deformation", UIH="0", UID="0", UIG="0", UIBG="1", UIX="1", lbENU="Deformations", dt="Bool", v="1")
        self.skins = ET.SubElement(self.deformation, "Skins", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Skins", dt="Bool", v="1")
        self.shape = ET.SubElement(self.deformation, "Shape", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Blend Shapes", dt="Bool", v="1")
        self.curve_filter = ET.SubElement(self.animation, "CurveFilter", UIH="0", UID="0", UIG="0", UIBG="1", UIX="1", lbENU="Curve Filters", dt="Bool", v="0")
        self.curve_filter_apply = ET.SubElement(self.curve_filter, "CurveFilterApplyCstKeyRed", UIH="0", UID="0", UIG="0", UIBG="1", UIX="1", lbENU="Constant Key Reducer", dt="Bool", v="0")
        self.curve_filter_translation_precision = ET.SubElement(self.curve_filter_apply, "CurveFilterCstKeyRedTPrec", UIH="0", UID="0", UIG="0", lbENU="Translation Precision", dt="Number", v="0.0001", min="0", max="1")
        self.curve_filter_rotation_precision = ET.SubElement(self.curve_filter_apply, "CurveFilterCstKeyRedRPrec", UIH="0", UID="0", UIG="0", lbENU="Rotation Precision", dt="Number", v="0.009", min="0", max="1")
        self.curve_filter_scale_precision = ET.SubElement(self.curve_filter_apply, "CurveFilterCstKeyRedSPrec", UIH="0", UID="0", UIG="0", lbENU="Scaling Precision", dt="Number", v="0.004", min="0", max="1")
        self.curve_filter_other_precision = ET.SubElement(self.curve_filter_apply, "CurveFilterCstKeyRedOPrec", UIH="0", UID="0", UIG="0", lbENU="Other Precision", dt="Number", v="0.009", min="0", max="1")
        self.curve_filter_auto_tangents_only = ET.SubElement(self.curve_filter_apply, "AutoTangentsOnly", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Auto tangents only", dt="Bool", v="1")
        self.point_cache = ET.SubElement(self.animation, "PointCache", UIH="0", UID="0", UIG="0", UIBG="1", UIX="1", lbENU="Geometry Cache File(s)", dt="Bool", v="0")
        self.selection_set_name_as_point_cache = ET.SubElement(self.point_cache, "SelectionSetNameAsPointCache", UIH="0", UID="0", UIG="0", lbENU="Set", dt="Enum", enumSelected=", ", v="0", enumItem_0=", ", enumItem_1="defaultLightSet", enumItem_2="defaultObjectSet")
        self.constraints_group = ET.SubElement(self.animation, "ConstraintsGrp", UIH="0", UID="0", UIG="1", UIX="1", UIP="0", lbENU="Constraints")
        self.constraints = ET.SubElement(self.constraints_group, "Constraint", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Constraints", dt="Bool", v="0")
        self.skeleton_definition = ET.SubElement(self.constraints_group, "Character", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Skeleton Definitions", dt="Bool", v="0")

        self.camera_group = ET.SubElement(include_group, "CameraGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Cameras")
        self.lights = ET.SubElement(self.camera_group, "Camera", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Cameras", dt="Bool", v="1")

        self.light_group = ET.SubElement(include_group, "LightGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Lights")
        self.lights = ET.SubElement(self.light_group, "Light", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Lights", dt="Bool", v="1")

        self.audio = ET.SubElement(include_group, "Audio", UIH="0", UID="0", UIG="0", UIBG="1", UIX="0", lbENU="Audio", dt="Bool", v="0")

        self.embed_texture_group = ET.SubElement(include_group, "EmbedTextureGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Embed Media")
        self.embed_texture = ET.SubElement(self.embed_texture_group, "EmbedTexture", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Embed Media", dt="Bool", v="0")

        self.bind_pose = ET.SubElement(include_group, "BindPose", UIH="1", UID="0", UIG="0", UIBG="0", lbENU="Bind Pose", dt="Bool", v="1")
        self.pivot_to_nulls = ET.SubElement(include_group, "PivotToNulls", UIH="1", UID="0", UIG="0", UIBG="0", lbENU="Pivot To Null", dt="Bool", v="0")
        self.bypass_rrs_inheritance = ET.SubElement(include_group, "BypassRrsInheritance", UIH="1", UID="0", UIG="0", UIBG="0", lbENU="Bypass Rrs Inheritance", dt="Bool", v="0")

        self.input_connections_group = ET.SubElement(include_group, "InputConnectionsGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Connections")
        self.include_children = ET.SubElement(self.input_connections_group, "IncludeChildren", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Include Children", dt="Bool", v="1")
        self. input_connections = ET.SubElement(self.input_connections_group, "InputConnections", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Input Connections", dt="Bool", v="1")

        advanced_options = ET.SubElement(self.root, "AdvOptGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Advanced Options")

        self.units_group = ET.SubElement(advanced_options, "UnitsGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Units")
        self.total_units_scale = ET.SubElement(self.units_group, "TotalUnitsScale", UIH="0", UID="0", UIG="0", lbENU="Total Units Scale", dt="TextLine")
        self.dynamic_scale_conversion = ET.SubElement(self.units_group, "DynamicScaleConversion", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Automatic", dt="Bool", v="1")
        self.units_selector = ET.SubElement(self.units_group, "UnitsSelector", UIH="0", UID="1", UIG="0", lbENU="Scene units converted to", dt="Enum", enumSelected="Centimeters", v="1", enumItem_0="Millimeters", enumItem_1="Centimeters", enumItem_2="Decimeters", enumItem_3="Meters", enumItem_4="Kilometers", enumItem_5="Inches", enumItem_6="Feet", enumItem_7="Yards", enumItem_8="Miles")
        self.axis_conversion_group = ET.SubElement(advanced_options, "AxisConvGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Axis Conversion")
        self.axis_conversion = ET.SubElement(self.axis_conversion_group, "UpAxis", UIH="0", UID="0", UIG="0", lbENU="Up Axis", dt="Enum", enumSelected="Y", v="0", enumItem_0="Y", enumItem_1="Z")
        ui = ET.SubElement(advanced_options, "UI", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="UI")
        self.show_warnings_manager = ET.SubElement(ui, "ShowWarningsManager", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Show Warning Manager", dt="Bool", v="1")
        self.generate_log_data = ET.SubElement(ui, "GenerateLogData", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Generate Log Data", dt="Bool", v="1")
        self.plugin_versions_url = ET.SubElement(ui, "PluginVersionsURL", UIH="1", UID="0", UIG="0", lbENU="Plugin Versions URL", dt="KString", v="http://download.autodesk.com/us/fbx/versions/fbxversion.xml")
        fbx = ET.SubElement(advanced_options, "Fbx", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="FBX File Format")
        self.ascii_fbx = ET.SubElement(fbx, "AsciiFbx", UIH="0", UID="0", UIG="0", lbENU="Type", dt="Enum", enumSelected="Binary", v="0", enumItem_0="Binary", enumItem_1="ASCII")
        self.export_file_version = ET.SubElement(fbx, "ExportFileVersion", UIH="0", UID="0", UIG="0", lbENU="Version", dt="Alias", enumSelected="FBX201800", v="0", enumItem_0="FBX201800", enumItem_1="FBX201600", enumItem_2="FBX201400", enumItem_3="FBX201300", enumItem_4="FBX201200", enumItem_5="FBX201100", enumItem_6="FBX201000", enumItem_7="FBX200900", enumItem_8="FBX200611")

        dxf = ET.SubElement(advanced_options, "Dxf", UIH="1", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Dxf")
        self.dxf_deformation = ET.SubElement(dxf, "Deformation", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Deformed Models", dt="Bool", v="1")
        self.dxf_triangulate = ET.SubElement(dxf, "Triangulate", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Triangulate", dt="Bool", v="1")
        collada = ET.SubElement(advanced_options, "Collada", UIH="1", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Collada")
        self.collada_triangulate = ET.SubElement(collada, "Triangulate", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Triangulate", dt="Bool", v="1")
        self.collada_single_matrix = ET.SubElement(collada, "SingleMatrix", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Single Matrix", dt="Bool", v="1")
        self.collada_frame_rate = ET.SubElement(collada, "FrameRate", UIH="0", UID="0", UIG="0", lbENU="Frame Rate", dt="Number", v="24")

        fbx_extensions_sdf = ET.SubElement(self.root, "FBXExtentionsSDK", UIH="1", UID="0", UIG="1", UIX="0", UIP="1", lbENU="FBX Extensions SDK")
        self.custom_property = ET.SubElement(fbx_extensions_sdf, "FBXExtentionsSDKWarning", UIH="0", UID="0", UIG="0", lbENU="FBX Extensions SDK Warning", dt="Warning", v="Add your custom properties here")

    def save_bin_path(self, file_path=None):
        """
        Save the xml tree to file
        """
        tree = ET.ElementTree(self.root)
        ET.indent(tree, "  ")
        tree.write(file_path if file_path else self.bin_path, encoding="utf-8", xml_declaration=True)
        self._trim_and_fix(file_path)

    def _trim_and_fix(self, file_path):
        """
        Format the preset file to match the original
        """
        output_lines = []
        bin_file = open(file_path if file_path else self.bin_path, 'r')
        lines = bin_file.readlines()
        bin_file.close()

        for line in lines:
            fixed = line.replace(" />", "/>")
            fixed = fixed.replace(" &amp;amp;", " &amp;")   # &amp duplication can happen by accident
            fixed = fixed.replace(", ", " ")    # Can't think of a simple way to fix this in the main algorithm
            output_lines.append(fixed)

        output_lines[0] = output_lines[0].replace("'", "\"")
        output_lines.append("\n")

        with open(file_path if file_path else self.bin_path, "w") as f:
            for line in output_lines:
                f.write("%s" % line)

    @property
    def bin_path(self):
        return os.path.join(BIN_FOLDER, "{}.fbxexportpreset".format(self.name))


def parse_xml_string_to_python(input_string):
    tokens = input_string.split(' ')
    title = tokens[0]
    content = tokens[1:]
    buffer = ''
    attrs = []

    for i in range(len(content)):
        buffer += f' {content[i]}' if len(buffer) else content[i]

        if buffer.endswith('"'):
            attrs.append(buffer)
            buffer = ''

    output_string = f'"{title}", ' + ', '.join(attrs)
    print(input_string)
    print(output_string)
    pyperclip.copy(output_string)


if __name__ == "__main__":
    # parse_xml_string_to_python('Animation UIH="0" UID="0" UIG="0" UIBG="1" UIX="0" lbENU="Animation" dt="Bool" v="1"')
    preset = FbxExportPresetCreator("test_preset")
    preset.save_bin_path()


class FbxExportPresetEditor:
    def __init__(self, path):
        self.path = path
        self.tree = ET.parse(self.path)
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