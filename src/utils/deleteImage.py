import os
from constants.VALUES import USER_GIVEN_IMAGES_DIR, EDITED_USER_GIVEN_IMAGES_DIR, DELETE_COROUTINE_TIME, LOGGING_LEVEL
import time
import logging

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=LOGGING_LEVEL
)
logger = logging.getLogger(__name__)


async def deleteImageCoroutine(context,  _force: bool = False) -> int:
    # delete images coroutine
    # deletes images after a set amount of time they are created

    _total_deleted = 0
    _files = os.listdir(USER_GIVEN_IMAGES_DIR)
    _current_unix_timestamp = time.time()
    for _file in _files:
        _file_path = os.path.join(USER_GIVEN_IMAGES_DIR, _file)
        try:
            _file_unix_timestamp = os.path.getmtime(_file_path)
            if _current_unix_timestamp - _file_unix_timestamp > DELETE_COROUTINE_TIME/12 or _force and _file != '.local':
                os.remove(_file_path)
                _total_deleted += 1

        except Exception:
            pass

        _file_path = os.path.join(EDITED_USER_GIVEN_IMAGES_DIR, _file)
        try:
            _file_unix_timestamp = os.path.getmtime(_file_path)
            if _current_unix_timestamp - _file_unix_timestamp > DELETE_COROUTINE_TIME/12 or _force and _file != '.local':
                os.remove(_file_path)
                _total_deleted += 1

        except Exception:
            pass

    logger.info(f"Deleted {_total_deleted} files.")
    return _total_deleted
