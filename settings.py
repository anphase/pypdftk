import configparser
import os


config = configparser.ConfigParser()
current_path = os.path.abspath('')
config.read(os.path.join(current_path, '.env'))


try:
    PYPDFTK_TMP_PATH = config.get("PDFTK", "TMP_PATH")
except (configparser.NoSectionError, configparser.NoOptionError, KeyError):
    if os.getenv('PYPDFTK_TMP_PATH'):
        PYPDFTK_TMP_PATH = os.getenv('PYPDFTK_TMP_PATH')
    else:
        current_path = os.path.abspath('')
        PYPDFTK_TMP_PATH = os.path.join(current_path, 'tmp')
