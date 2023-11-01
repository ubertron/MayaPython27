def import_base_character(gender):
    """
    Import a base character
    @param gender:
    """
    import pymel.core as pm

    from maya_tools.scene_utils import import_model
    from maya_tools.paths import MODELS_FOLDER

    import_path = MODELS_FOLDER.joinpath('base_mesh_male.fbx' if gender == 'male' else 'base_mesh_female.fbx')
    result = import_model(import_path=import_path)
    transform = next(x for x in result if type(x) is pm.nodetypes.Transform)
    pm.select(transform)
    pm.viewFit()
    return transform
