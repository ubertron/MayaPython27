import os
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
REQUIREMENTS = os.path.join(PROJECT_ROOT, 'requirements.txt')
SITE_PACKAGES = os.path.join(PROJECT_ROOT, 'site-packages')


def inspect_path(path_string):
    logging.info("{}: Exists? {}".format(path_string, os.path.exists(path_string)))


if __name__ == '__main__':
    inspect_path(PROJECT_ROOT)
    inspect_path(REQUIREMENTS)
    inspect_path(SITE_PACKAGES)
