import os
from telegram import Update
from telegram.ext import ContextTypes
from utils.getImage import getImage
from utils.EC import EC
from constants.VALUES import EDITED_USER_GIVEN_IMAGES_DIR


# Blur commands
async def _blur(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _image_path, _image_name = await getImage(update)

    if _image_path != None and _image_name != None:
        _blur_intensity = 2
        if context.args and len(context.args) > 0:
            try:
                _blur_intensity = int(context.args[0])
                if _blur_intensity > 10:
                    _blur_intensity = 10
                elif _blur_intensity <= 0:
                    _blur_intensity = 1
            except Exception:
                pass

        new_path = os.path.join(EDITED_USER_GIVEN_IMAGES_DIR, _image_name.split('.')[0])

        EC.blur(_image_path, _blur_intensity).save(f"{new_path}.jpg")
        await update.message.reply_photo(f"{new_path}.jpg")

    else:
        await update.message.reply_text('Error parsing image.')
