# imports
from os import getenv
import telegram
from telegram.ext import Application, CommandHandler, Defaults
from dotenv import load_dotenv
from commands.basic_commands import alive
from commands.image_commands import blur
from commands.dev_commands import *
from commands.help_command import help_command_creator, help_command

# loading envs
load_dotenv()

# Create the Application and pass it your bot's token.
Bot = Application.builder().token(getenv("TOKEN")).build()

# defining commands
basic_commands = [alive]
image_commands = [blur]
dev_commands = []


all_commands = [CommandHandler(i.__name__, i) for i in [*basic_commands, *image_commands, *dev_commands]]

# setting up help command
help_command_creator(basic_commands, image_commands, dev_commands)

# adding to bot
Bot.add_handlers(all_commands)
Bot.add_handler(CommandHandler("help", help_command))
