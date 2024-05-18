import os

# from dotenv import load_dotenv, set_key   # cannot install via mayapy Python 2.7.11
from core_tools.system_utils import is_using_maya_python

if is_using_maya_python():
    from pymel.core import Path
else:
    from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
ENV_PATH = PROJECT_ROOT.joinpath('.env')

if not ENV_PATH.exists():
    ENV_PATH.touch(mode=0o600, exist_ok=False)


def env_file_to_dict():
    return {x.split('=')[0]: x.split('=')[1] for x in open(str(ENV_PATH), "r").readlines()}


def get_env_value(key):
    """
    Get environment variable from local .env
    @param key:
    @return:
    """
    # load_dotenv(ENV_PATH)
    #
    # return os.getenv(key)

    return env_file_to_dict().get(key).strip().replace("'", "")


def set_env_value(key, value):
    """
    Set environment variable to local .env
    @param key:
    @param value:
    """
    # set_key(dotenv_path=ENV_PATH, key_to_set=key, value_to_set=str(value))

    env_dict = env_file_to_dict()
    env_dict[key] = value

    with open(str(ENV_PATH), 'w') as f:
        for k, v in env_dict.items():
            f.write('{}=\'{}\'\n'.format(k, v))


if __name__ == '__main__':
    engine_key = 'ENGINE_ROOT'
    # engine_root = Path.home().joinpath('Dropbox/Projects/Unity/AnimationManager')
    _result = get_env_value('ENGINE_ROOT')
    print(_result)
    # set_env_value(key=engine_key, value=engine_root)

