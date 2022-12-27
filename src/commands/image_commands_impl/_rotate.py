import os
from telegram import Update
from telegram.ext import ContextTypes
from utils.getImage import getImage
from utils.EC import EC
from constants.VALUES import EDITED_USER_GIVEN_IMAGES_DIR


# Blur commands
async def _rotate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _image_path, _image_name = await getImage(update)

    if _image_path != None and _image_name != None:
        _rotation_angle = 90
        if context.args and len(context.args) > 0:
            try:
                _rotation_angle = int(context.args[0])
                if _rotation_angle > 360:
                    _rotation_angle = 360
                elif _rotation_angle <= 0:
                    _rotation_angle = 0

            except Exception:
                pass

        new_path = os.path.join(EDITED_USER_GIVEN_IMAGES_DIR, _image_name.split('.')[0])

        EC.rotate(_image_path, _rotation_angle).save(f"{new_path}.jpg")
        await update.message.reply_photo(f"{new_path}.jpg")

    else:
        await update.message.reply_text('Error parsing image.')
