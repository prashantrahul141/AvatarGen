import os
from constants.VALUES import USER_GIVEN_IMAGES_DIR, EDITED_USER_GIVEN_IMAGES_DIR, DELETE_COROUTINE_TIME
import time


async def deleteImageCoroutine(context) -> None:
    # delete images coroutine
    # deletes images after a set amount of time they are created

    _files = os.listdir(USER_GIVEN_IMAGES_DIR)
    _current_unix_timestamp = time.time()
    for _file in _files:
        _file_path = os.path.join(USER_GIVEN_IMAGES_DIR, _file)
        try:
            _file_unix_timestamp = os.path.getmtime(_file_path)
            if _current_unix_timestamp - _file_unix_timestamp > DELETE_COROUTINE_TIME:
                os.remove(_file_path)

        except Exception:
            raise Exception

        _file_path = os.path.join(EDITED_USER_GIVEN_IMAGES_DIR, _file)
        try:
            _file_unix_timestamp = os.path.getmtime(_file_path)
            if _current_unix_timestamp - _file_unix_timestamp > DELETE_COROUTINE_TIME:
                os.remove(_file_path)

        except Exception:
            raise Exception
