# imports
from telegram import Update
from telegram.ext import ContextTypes


async def blur(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''blurs the image.'''
    await update.message.reply_text('yes')
