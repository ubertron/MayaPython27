import xml.etree.cElementTree as ET
import os
import pyperclip

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
BIN_FOLDER = os.path.join(PROJECT_ROOT, "bin")


class FbxExportPreset:
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
        smoothing_groups = ET.SubElement(geometry, "SmoothingGroups", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Smoothing Groups", dt="Bool", v="0")
        hard_edges = ET.SubElement(geometry, "expHardEdges",  UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Split per-vertex Normals", dt="Bool", v="0")
        tangents_binormals = ET.SubElement(geometry, "TangentsandBinormals", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Tangents and Binormals", dt="Bool", v="0")
        smooth_mesh = ET.SubElement(geometry, "SmoothMesh", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Smooth Mesh", dt="Bool", v="1")
        selection_set = ET.SubElement(geometry, "SelectionSet", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Selection Sets", dt="Bool", v="0")
        blind_data = ET.SubElement(geometry, "BlindData", UIH="1", UID="0", UIG="0", UIBG="0", lbENU="Blind Data", dt="Bool", v="1")
        animation_only = ET.SubElement(geometry, "AnimationOnly", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Convert to Null objects", dt="Bool", v="0")
        instances = ET.SubElement(geometry, "Instances", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Preserve Instances", dt="Bool", v="0")
        container_objects = ET.SubElement(geometry, "ContainerObjects", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Referenced Assets Content", dt="Bool", v="1")
        triangulate = ET.SubElement(geometry, "Triangulate", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Triangulate", dt="Bool", v="0")
        convert_nurbs = ET.SubElement(geometry, "GeometryNurbsSurfaceAs", UIH="0", UID="0", UIG="0", lbENU="Convert NURBS surface to", dt="Enum", enumSelected="NURBS", v="0", enumItem_0="NURBS", enumItem_1="InteractiveDisplayMesh", enumItem_2="SoftwareRenderMesh")

        animation = ET.SubElement(include_group, "Animation", UIH="0", UID="0", UIG="0", UIBG="1", UIX="0", lbENU="Animation", dt="Bool", v="1")
        extra_group = ET.SubElement(animation, "ExtraGrp", UIH="0", UID="0", UIG="1", UIX="1", UIP="0", lbENU="Extra Options")
        use_scene_names = ET.SubElement(extra_group, "UseSceneName", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Use scene name", dt="Bool", v="0")
        remove_single_key = ET.SubElement(extra_group, "RemoveSingleKey", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Remove single key", dt="Bool", v="0")
        quaternion = ET.SubElement(extra_group, "Quaternion", UIH="0", UID="0", UIG="0", lbENU="Quaternion Interpolation Mode", dt="Enum", enumSelected="Resample As Euler Interpolation", v="2", enumItem_0="Retain Quaternion Interpolation", enumItem_1="Set As Euler Interpolation", enumItem_2="Resample As Euler Interpolation")
        bake_complex_animation = ET.SubElement(animation, "BakeComplexAnimation", UIH="0", UID="0", UIG="0", UIBG="1", UIX="1", lbENU="Bake Animation", dt="Bool", v="0")
        bake_frame_start = ET.SubElement(bake_complex_animation, "BakeFrameStart", UIH="0", UID="0", UIG="0", lbENU="Start", dt="Integer", v="1")
        bake_frame_end = ET.SubElement(bake_complex_animation, "BakeFrameEnd", UIH="0", UID="0", UIG="0", lbENU="End", dt="Integer", v="200")
        bake_frame_step = ET.SubElement(bake_complex_animation, "BakeFrameStep", UIH="0", UID="0", UIG="0", lbENU="Step", dt="Integer", v="1")
        resample_animation_curves = ET.SubElement(bake_complex_animation, "ResampleAnimationCurves", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Resample All", dt="Bool", v="0")
        hide_complex_animation_warning = ET.SubElement(bake_complex_animation, "HideComplexAnimationBakedWarning", UIH="1", UID="0", UIG="0", UIBG="0", lbENU="Hide Complex Animation Baked Warning", dt="Bool", v="0")
        deformation = ET.SubElement(animation, "Deformation", UIH="0", UID="0", UIG="0", UIBG="1", UIX="1", lbENU="Deformations", dt="Bool", v="1")
        skins = ET.SubElement(deformation, "Skins", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Skins", dt="Bool", v="1")
        shape = ET.SubElement(deformation, "Shape", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Blend Shapes", dt="Bool", v="1")
        curve_filter = ET.SubElement(animation, "CurveFilter", UIH="0", UID="0", UIG="0", UIBG="1", UIX="1", lbENU="Curve Filters", dt="Bool", v="0")
        curve_filter_apply = ET.SubElement(curve_filter, "CurveFilterApplyCstKeyRed", UIH="0", UID="0", UIG="0", UIBG="1", UIX="1", lbENU="Constant Key Reducer", dt="Bool", v="0")
        curve_filter_translation_precision = ET.SubElement(curve_filter_apply, "CurveFilterCstKeyRedTPrec", UIH="0", UID="0", UIG="0", lbENU="Translation Precision", dt="Number", v="0.0001", min="0", max="1")
        curve_filter_rotation_precision = ET.SubElement(curve_filter_apply, "CurveFilterCstKeyRedRPrec", UIH="0", UID="0", UIG="0", lbENU="Rotation Precision", dt="Number", v="0.009", min="0", max="1")
        curve_filter_scale_precision = ET.SubElement(curve_filter_apply, "CurveFilterCstKeyRedSPrec", UIH="0", UID="0", UIG="0", lbENU="Scaling Precision", dt="Number", v="0.004", min="0", max="1")
        curve_filter_other_precision = ET.SubElement(curve_filter_apply, "CurveFilterCstKeyRedOPrec", UIH="0", UID="0", UIG="0", lbENU="Other Precision", dt="Number", v="0.009", min="0", max="1")
        curve_filter_auto_tangents_only = ET.SubElement(curve_filter_apply, "AutoTangentsOnly", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Auto tangents only", dt="Bool", v="1")
        point_cache = ET.SubElement(animation, "PointCache", UIH="0", UID="0", UIG="0", UIBG="1", UIX="1", lbENU="Geometry Cache File(s)", dt="Bool", v="0")
        selection_set_name_as_point_cache = ET.SubElement(point_cache, "SelectionSetNameAsPointCache", UIH="0", UID="0", UIG="0", lbENU="Set", dt="Enum", enumSelected=", ", v="0", enumItem_0=", ", enumItem_1="defaultLightSet", enumItem_2="defaultObjectSet")
        constraints_group = ET.SubElement(animation, "ConstraintsGrp", UIH="0", UID="0", UIG="1", UIX="1", UIP="0", lbENU="Constraints")
        constraints = ET.SubElement(constraints_group, "Constraint", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Constraints", dt="Bool", v="0")
        skeleton_definition = ET.SubElement(constraints_group, "Character", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Skeleton Definitions", dt="Bool", v="0")

        camera_group = ET.SubElement(include_group, "CameraGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Cameras")
        lights = ET.SubElement(camera_group, "Camera", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Cameras", dt="Bool", v="1")

        light_group = ET.SubElement(include_group, "LightGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Lights")
        lights = ET.SubElement(animation, "Light", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Lights", dt="Bool", v="1")

        audio = ET.SubElement(include_group, "Audio", UIH="0", UID="0", UIG="0", UIBG="1", UIX="0", lbENU="Audio", dt="Bool", v="0")

        embed_texture_group = ET.SubElement(include_group, "EmbedTextureGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Embed Media")
        embed_texture = ET.SubElement(embed_texture_group, "EmbedTexture", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Embed Media", dt="Bool", v="0")

        bind_pose = ET.SubElement(include_group, "BindPose", UIH="1", UID="0", UIG="0", UIBG="0", lbENU="Bind Pose", dt="Bool", v="1")
        pivot_to_nulls = ET.SubElement(include_group, "PivotToNulls", UIH="1", UID="0", UIG="0", UIBG="0", lbENU="Pivot To Null", dt="Bool", v="0")
        bypass_rrs_inheritance = ET.SubElement(include_group, "BypassRrsInheritance", UIH="1", UID="0", UIG="0", UIBG="0", lbENU="Bypass Rrs Inheritance", dt="Bool", v="0")

        input_connections_group = ET.SubElement(include_group, "InputConnectionsGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Connections")
        include_children = ET.SubElement(input_connections_group, "IncludeChildren", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Include Children", dt="Bool", v="1")
        input_connections = ET.SubElement(input_connections_group, "InputConnections", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Input Connections", dt="Bool", v="1")

        advanced_options = ET.SubElement(self.root, "AdvOptGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Advanced Options")

        units_group = ET.SubElement(advanced_options, "UnitsGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Units")
        total_units_scale = ET.SubElement(units_group, "TotalUnitsScale", UIH="0", UID="0", UIG="0", lbENU="Total Units Scale", dt="TextLine")
        dynamic_scale_conversion = ET.SubElement(units_group, "DynamicScaleConversion", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Automatic", dt="Bool", v="1")
        units_selector = ET.SubElement(units_group, "UnitsSelector", UIH="0", UID="1", UIG="0", lbENU="Scene units converted to", dt="Enum", enumSelected="Centimeters", v="1", enumItem_0="Millimeters", enumItem_1="Centimeters", enumItem_2="Decimeters", enumItem_3="Meters", enumItem_4="Kilometers", enumItem_5="Inches", enumItem_6="Feet", enumItem_7="Yards", enumItem_8="Miles")
        axis_conversion_group = ET.SubElement(advanced_options, "AxisConvGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Axis Conversion")
        axis_conversion = ET.SubElement(axis_conversion_group, "UpAxis", UIH="0", UID="0", UIG="0", lbENU="Up Axis", dt="Enum", enumSelected="Y", v="0", enumItem_0="Y", enumItem_1="Z")
        ui = ET.SubElement(advanced_options, "UI", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="UI")
        show_warnings_manager = ET.SubElement(ui, "ShowWarningsManager", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Show Warning Manager", dt="Bool", v="1")
        generate_log_data = ET.SubElement(ui, "GenerateLogData", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Generate Log Data", dt="Bool", v="1")
        plugin_versions_url = ET.SubElement(ui, "PluginVersionsURL", UIH="1", UID="0", UIG="0", lbENU="Plugin Versions URL", dt="KString", v="http://download.autodesk.com/us/fbx/versions/fbxversion.xml")
        fbx = ET.SubElement(advanced_options, "Fbx", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="FBX File Format")
        ascii_fbx = ET.SubElement(fbx, "AsciiFbx", UIH="0", UID="0", UIG="0", lbENU="Type", dt="Enum", enumSelected="Binary", v="0", enumItem_0="Binary", enumItem_1="ASCII")
        export_file_version = ET.SubElement(fbx, "ExportFileVersion", UIH="0", UID="0", UIG="0", lbENU="Version", dt="Alias", enumSelected="FBX201800", v="0", enumItem_0="FBX201800", enumItem_1="FBX201600", enumItem_2="FBX201400", enumItem_3="FBX201300", enumItem_4="FBX201200", enumItem_5="FBX201100", enumItem_6="FBX201000", enumItem_7="FBX200900", enumItem_8="FBX200611")

        dxf = ET.SubElement(advanced_options, "Dxf", UIH="1", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Dxf")
        dxf_deformation = ET.SubElement(dxf, "Deformation", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Deformed Models", dt="Bool", v="1")
        dxf_triangulate = ET.SubElement(animation, "Triangulate", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Triangulate", dt="Bool", v="1")
        collada = ET.SubElement(advanced_options, "Collada", UIH="1", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Collada")
        collada_triangulate = ET.SubElement(collada, "Triangulate", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Triangulate", dt="Bool", v="1")
        collada_single_matrix = ET.SubElement(collada, "SingleMatrix", UIH="0", UID="0", UIG="0", UIBG="0", lbENU="Single Matrix", dt="Bool", v="1")
        collada_frame_rate = ET.SubElement(collada, "FrameRate", UIH="0", UID="0", UIG="0", lbENU="Frame Rate", dt="Number", v="24")

        fbx_extensions_sdf = ET.SubElement(self.root, "FBXExtensionsSDK", UIH="1", UID="0", UIG="1", UIX="0", UIP="1", lbENU="FBX Extensions SDK")
        ET.SubElement(fbx_extensions_sdf, "FBXExtentionsSDKWarning", UIH="0", UID="0", UIG="0", lbENU="FBX Extensions SDK Warning", dt="Warning", v="Add your custom properties here")

    def save_bin_path(self):
        tree = ET.ElementTree(self.root)
        ET.indent(tree, "  ")
        tree.write(self.bin_path, encoding="utf-8", xml_declaration=True)

    def strip_end_of_line_space(self):
        pass

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
    preset = FbxExportPreset("test_preset")
    preset.save_bin_path()
