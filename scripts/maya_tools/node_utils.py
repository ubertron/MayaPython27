import pymel.core as pm

from maya_tools.maya_enums import ComponentType


class State:
    """Query and restore selection/component mode"""

    def __init__(self):
        self.component_mode = get_component_mode()
        self.selection = pm.ls(sl=True)
        if self.object_mode:
            self.object_selection = pm.ls(sl=True)
            self.component_selection = []
        else:
            self.component_selection = pm.ls(sl=True)
            set_component_mode(ComponentType.object)
            self.object_selection = pm.ls(sl=True)
            set_component_mode(self.component_mode)
            pm.hilite(self.object_selection)

    def restore(self):
        if self.object_selection:
            pm.select(self.object_selection, noExpand=True)
            set_component_mode(self.component_mode)
        else:
            set_component_mode(ComponentType.object)
            pm.select(clear=True)
        if not self.object_mode:
            pm.select(self.component_selection)

    @property
    def object_mode(self):
        return self.component_mode == ComponentType.object

    def remove_objects(self, objects):
        # Sometimes necessary as pm.objExists check causes an exception
        for item in list(objects):
            if item in self.object_selection:
                self.object_selection.remove(item)


def get_component_mode():
    if pm.selectMode(query=True, object=True):
        return ComponentType.object
    elif pm.selectType(query=True, vertex=True):
        return ComponentType.vertex
    elif pm.selectType(query=True, edge=True):
        return ComponentType.edge
    elif pm.selectType(query=True, facet=True):
        return ComponentType.face
    elif pm.selectType(query=True, polymeshUV=True):
        return ComponentType.uv
    else:
        return 'unknown'


def set_component_mode(component_type=ComponentType.object):
    if component_type == ComponentType.object:
        pm.selectMode(object=True)
    else:
        pm.selectMode(component=True)
        if component_type == ComponentType.vertex:
            pm.selectType(vertex=True)
        elif component_type == ComponentType.edge:
            pm.selectType(edge=True)
        elif component_type == ComponentType.face:
            pm.selectType(facet=True)
        elif component_type == ComponentType.uv:
            pm.selectType(polymeshUV=True)
        else:
            pm.warning('Unknown component type')


def select_components(transform, components, component_type=ComponentType.face, hilite=True):
    state = State()

    if component_type == ComponentType.vertex:
        pm.select(transform.vtx[components])
    elif component_type == ComponentType.edge:
        pm.select(transform.e[components])
    elif component_type == ComponentType.face:
        pm.select(transform.f[components])
    elif component_type == ComponentType.uv:
        pm.select(transform.map[components])
    else:
        pm.warning('Component type not supported')

    if hilite:
        pm.hilite(transform)
    else:
        state.restore()
