# imports
from telegram import Update
from telegram.ext import ContextTypes
from utils import getImage


async def test_getImage(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''To test getImage utils function.'''
    await update.message.reply_text(update.message.chat_id)
    a = await getImage.getImage(update)
    print(a)
