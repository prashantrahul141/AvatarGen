import os
from telegram import Update
from telegram.ext import ContextTypes
from utils.getImage import getImage
from ImageEffects import EffectsCreator
from utils.EC import EC
from constants.VALUES import EDITED_USER_GIVEN_IMAGES_DIR


# Blur commands
async def _blur(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _image_path, _image_name = await getImage(update)
    if _image_path != None and _image_name != None:
        new_path = os.path.join(EDITED_USER_GIVEN_IMAGES_DIR, _image_name)
        EC.blur(_image_path, 2).save(new_path)
        await update.message.reply_photo(new_path)
