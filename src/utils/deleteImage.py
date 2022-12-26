import os
from constants.VALUES import USER_GIVEN_IMAGES_DIR
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
            if _current_unix_timestamp - _file_unix_timestamp > 120:
                os.remove(_file_path)

        except Exception:
            raise Exception
