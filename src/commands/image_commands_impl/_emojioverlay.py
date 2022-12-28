import os
from telegram import Update
from telegram.ext import ContextTypes
from utils.getImage import getImage
from utils.EC import EC
from constants.VALUES import EDITED_USER_GIVEN_IMAGES_DIR


# emojioverlay commands
async def _emojioverlay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    _image_path, _image_name = await getImage(update)

    if _image_path != None and _image_name != None:
        _emoji = '🤨'
        if context.args and len(context.args) > 0:
            try:
                _emoji = context.args[0]
            except Exception:
                pass

        new_path = os.path.join(EDITED_USER_GIVEN_IMAGES_DIR, _image_name.split('.')[0])

        try:
            _temp_image = EC.emojioverlay(_image_path, _emoji)
        except:
            await update.message.reply_text("couldn't find that emoji.")
            return

        _temp_image.save(f"{new_path}.png")
        await update.message.reply_photo(f"{new_path}.png")

    else:
        await update.message.reply_text('Error parsing image.')
