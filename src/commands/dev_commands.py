# imports
from telegram import Update
from telegram.ext import ContextTypes
from utils.getImage import getImage
from utils.deleteImage import deleteImageCoroutine


async def test_getImage(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    '''To test getImage utils function.'''
    _file_path, _file_path = await getImage(update)
    if _file_path != None:
        with open(_file_path, 'rb') as f:
            await update.message.reply_photo(f)
            return

    await update.message.reply_text("None")
