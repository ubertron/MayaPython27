import math
import pymel.core as pm


def create_cube(name=None, size=1, divisions=1):
    """
    Mirrors geometry along an axis
    :param name: str
    :param size: int
    :param divisions: int
    """
    cube, _ = pm.polyCube(
        name=name if name else 'cube',
        width=size, height=size, depth=size, 
        sx=divisions, sy=divisions, sz=divisions
    )
    return cube


def merge_vertices(transform=None, precision=5):
    """
    Merge vertices
    @param transform:
    @param precision:
    @return:
    """
    transform = pm.ls(transform, tr=True) if transform else pm.ls(sl=True, tr=True)
    result = pm.polyMergeVertex(transform, distance=precision_to_threshold(precision))
    return pm.ls(result[0])[0]


def precision_to_threshold(precision=1):
    """
    Convert digits of precision to a float threshold
    @param precision:
    @return:
    """
    return 1.0 / math.pow(10, precision)

