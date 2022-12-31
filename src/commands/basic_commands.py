# imports
from telegram import Update
from telegram.ext import ContextTypes


async def alive(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''To check if bot is working.'''
    await update.message.reply_text('yes')


async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    '''To start the bot.'''
    await update.message.reply_text(f'''Hello {update.effective_user.first_name if update.effective_user else ''}! \
You can try /help to get a proper help message on how to use this bot.''')
