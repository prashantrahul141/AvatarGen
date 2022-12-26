# imports
from telegram import Update
from telegram.ext import ContextTypes
from .image_commands_impl import _blur, _pixelate


async def blur(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''blurs the image.'''
    await _blur._blur(update, ctx)


async def pixelate(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''pixelates an images'''
    await _pixelate._pixelate(update, ctx)
