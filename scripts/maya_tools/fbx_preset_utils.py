import xml.etree.cElementTree as ET
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
BIN_FOLDER = os.path.join(PROJECT_ROOT, "bin")


class FbxExportPreset:
    def __init__(self, name):
        self.name = name
        self.root = ET.Element("Export", UIH="0", UIG="1", UIX="0", UIP="0", lbENU="Export")
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
        animation = ET.SubElement(include_group, "Animation", UIH="0", UID="0", UIG="0", UIBG="1", UIX="0", lbENU="Animation")
        cameras = ET.SubElement(include_group, "CameraGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Cameras")
        lights = ET.SubElement(include_group, "LightGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Lights")
        audio = ET.SubElement(include_group, "Audio", UIH="0", UID="0", UIG="0", UIBG="1", UIX="0", lbENU="Audio", dt="Bool", v="0")
        embed_texture = ET.SubElement(include_group, "EmbedTextureGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Embed Media")
        bind_pose = ET.SubElement(include_group, "BindPose", UIH="1", UID="0", UIG="0", UIBG="0", lbENU="Bind Pose", dt="Bool", v="1")
        pivot_to_nulls = ET.SubElement(include_group, "PivotToNulls", UIH="1", UID="0", UIG="0", UIBG="0", lbENU="Pivot To Null", dt="Bool", v="0")
        bypass_rrs_inheritance = ET.SubElement(include_group, "BypassRrsInheritance", UIH="1", UID="0", UIG="0", UIBG="0", lbENU="Bypass Rrs Inheritance", dt="Bool", v="0")
        input_connections = ET.SubElement(include_group, "InputConnectionsGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Connections")

        advanced_options = ET.SubElement(self.root, "AdvOptGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Advanced Options")
        units = ET.SubElement(advanced_options, "UnitsGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Units")
        axis_conversion = ET.SubElement(advanced_options, "AxisConvGrp", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Axis Conversion")
        ui = ET.SubElement(advanced_options, "UI", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="UI")
        fbx = ET.SubElement(advanced_options, "Fbx", UIH="0", UID="0", UIG="1", UIX="0", UIP="0", lbENU="FBX File Format")
        dxf = ET.SubElement(advanced_options, "Dxf", UIH="1", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Dxf")
        collada = ET.SubElement(advanced_options, "Collada", UIH="1", UID="0", UIG="1", UIX="0", UIP="0", lbENU="Collada")

        fbx_extensions_sdf = ET.SubElement(self.root, "FBXExtensionsSDK", UIH="1", UID="0", UIG="1", UIX="0", UIP="1", lbENU="FBX Extensions SDK")
        ET.SubElement(fbx_extensions_sdf, "FBXExtentionsSDKWarning", UIH="0", UID="0", UIG="0", lbENU="FBX Extensions SDK Warning", dt="Warning", v="Add your custom properties here")

    def save_bin_path(self):
        tree = ET.ElementTree(self.root)
        ET.indent(tree, "  ")
        tree.write(self.bin_path, encoding="utf-8", xml_declaration=True)

    @property
    def bin_path(self):
        return os.path.join(BIN_FOLDER, "{}.fbxexportpreset".format(self.name))


if __name__ == "__main__":
    preset = FbxExportPreset("test_preset")
    preset.save_bin_path()
