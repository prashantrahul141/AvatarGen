import os
import logging


# logging level
LOGGING_LEVEL = logging.ERROR


# Time outs
READ_TIMEOUT = 30
WRITE_TIMEOUT = 30

PHOTO_SIZE = -1
DELETE_COROUTINE_TIME = 120

# paths
CONSTANTS_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.split(CONSTANTS_DIR)[0]
ROOT_DIR = os.path.split(SRC_DIR)[0]
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets')
USER_GIVEN_IMAGES_DIR = os.path.join(ASSETS_DIR, 'user_given_images')
EDITED_USER_GIVEN_IMAGES_DIR = os.path.join(ASSETS_DIR, 'edited_user_given_images')
