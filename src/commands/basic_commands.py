# imports
from telegram import Update
from telegram.ext import ContextTypes


async def alive(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''To check if bot is working.'''
    await update.message.reply_text('yes')
