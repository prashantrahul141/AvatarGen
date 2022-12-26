# imports
from telegram import Update
from telegram.ext import ContextTypes
from image_commands import _blur


async def blur(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''blurs the image.'''
    await _blur.blur(update, ctx)
