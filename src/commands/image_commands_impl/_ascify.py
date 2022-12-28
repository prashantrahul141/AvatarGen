from telegram import Update
from telegram.ext import ContextTypes
from utils.EC import EC


# Ascify commands
async def _ascify(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if ctx.args and len(ctx.args) > 0:
        _text = " ".join(ctx.args)
        _reply_text = EC.asicfy(_text)
        await update.message.reply_text(f"<code>{_reply_text}</code>", parse_mode='HTML')
    else:
        await update.message.reply_text("Please provide text.")
