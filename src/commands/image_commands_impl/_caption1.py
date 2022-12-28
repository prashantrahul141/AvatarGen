import os
from telegram import Update
from telegram.ext import ContextTypes
from utils.getImage import getImage
from utils.EC import EC
from constants.VALUES import EDITED_USER_GIVEN_IMAGES_DIR


# Caption1 commands
async def _caption1(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    _image_path, _image_name = await getImage(update)

    if _image_path != None and _image_name != None:
        _text = 'text here'
        if ctx.args and len(ctx.args) > 0:
            _text = " ".join(ctx.args)

        new_path = os.path.join(EDITED_USER_GIVEN_IMAGES_DIR, _image_name.split('.')[0])

        EC.caption1(_image_path, _text).save(f"{new_path}.jpg")
        await update.message.reply_photo(f"{new_path}.jpg")

    else:
        await update.message.reply_text('Error parsing image.')
