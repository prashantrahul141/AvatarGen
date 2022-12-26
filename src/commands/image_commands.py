# imports
from telegram import Update
from telegram.ext import ContextTypes
from .image_commands_impl import _blur


async def blur(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''blurs the image.'''
    await _blur._blur(update, ctx)
