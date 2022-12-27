# imports
from telegram import Update
from telegram.ext import ContextTypes
from .image_commands_impl import _blur, _pixelate, _emojioverlay, _deepfry, _caption1, _caption2


async def blur(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''blurs the image.'''
    await _blur._blur(update, ctx)


async def pixelate(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''pixelates an images.'''
    await _pixelate._pixelate(update, ctx)


async def emojioverlay(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''overlays an emoji over an image.'''
    await _emojioverlay._emojioverlay(update, ctx)


async def deepfry(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''make deepfry meme from an image.'''
    await _deepfry._deepfry(update, ctx)


async def caption1(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''adds captions to the upper part of the image.'''
    await _caption1._caption1(update, ctx)


async def caption2(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''adds captions to the upper part of the image.'''
    await _caption2._caption2(update, ctx)
