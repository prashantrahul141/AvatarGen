# imports
from os import getenv
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv
from commands.basic_commands import alive
from commands.image_commands import blur

# loading envs
load_dotenv()

# Create the Application and pass it your bot's token.
Bot = Application.builder().token(getenv("TOKEN")).build()

# defining commands
basic_commands = [alive]
image_commands = [blur]
dev_commands = []

all_commands = [CommandHandler(i.__name__, i) for i in [*basic_commands, *image_commands, *dev_commands]]

# adding to bot
Bot.add_handlers(all_commands)
