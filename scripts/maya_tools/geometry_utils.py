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
