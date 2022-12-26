# imports
from telegram import Update
from telegram.ext import ContextTypes
from utils.getImage import getImage


async def test_getImage(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''To test getImage utils function.'''
    _file_path: str | None = await getImage(update)
    if _file_path != None:
        with open(_file_path, 'rb') as f:
            await update.message.reply_photo(f)
