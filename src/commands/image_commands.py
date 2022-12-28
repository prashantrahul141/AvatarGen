# imports
from telegram import Update
from telegram.ext import ContextTypes
from .image_commands_impl import _blur, _pixelate, _emojioverlay, _deepfry, _caption1, _caption2, _cropcircle
from .image_commands_impl import _rotate, _ascify, _crop, _saturate, _grayscale, _flip


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
    '''adds captions to the bottom part of the image.'''
    await _caption2._caption2(update, ctx)


async def cropcircle(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''crops image in a circle.'''
    await _cropcircle._cropcircle(update, ctx)


async def rotate(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''rotates the image.'''
    await _rotate._rotate(update, ctx)


async def ascify(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''rotates the image.'''
    await _ascify._ascify(update, ctx)


async def crop(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''crops images in 1:1 ratio'''
    await _crop._crop(update, ctx)


async def saturate(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''change saturation of an image.'''
    await _saturate._saturate(update, ctx)


async def grayscale(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''grayscales an image.'''
    await _grayscale._grayscale(update, ctx)


async def flip(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''flips an image vertically.'''
    await _flip._flip(update, ctx)
