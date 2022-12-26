from telegram import Update
from telegram.ext import ContextTypes
from utils.getImage import getImage
from ImageEffects import EffectsCreator


# Blur commands
async def _blur(update: Update, context: ContextTypes.DEFAULT_TYPE, EC: EffectsCreator):
    _image = await getImage(update)
    if _image != None:
        await Update.message.reply_photo(_image)
