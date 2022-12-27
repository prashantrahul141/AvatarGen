# imports
from os import getenv
import telegram
from telegram.ext import Application, CommandHandler
from telegram.ext.filters import Chat
from dotenv import load_dotenv
from commands.basic_commands import alive
from commands.image_commands import blur, pixelate, emojioverlay, deepfry, caption1, caption2
from commands.dev_commands import test_getImage
from commands.help_command import help_command_creator, help_command
from utils.deleteImage import deleteImageCoroutine
from constants.VALUES import DELETE_COROUTINE_TIME

# loading envs
load_dotenv()

# devs ids
_devs_id = []

for i in range(int(getenv("TOTAL_DEVS"))):  # type: ignore
    _devs_id.append(int(getenv(f"DEV_ID_{i}")))  # type: ignore
DEVS = set(_devs_id)

# Create the Application and pass it your bot's token.
Bot = Application.builder().token(getenv("TOKEN")).build()  # type: ignore

# defining commands
basic_commands = [alive]
image_commands = [blur, pixelate, emojioverlay, deepfry, caption1, caption2]
dev_commands = [test_getImage]
user_commands = [CommandHandler(i.__name__, i) for i in [*basic_commands, *image_commands]]

# setting up help command
help_command_creator(basic_commands, image_commands, dev_commands)

# adding to bot
Bot.add_handler(CommandHandler("help", help_command))
Bot.add_handlers(user_commands)  # type: ignore
Bot.add_handlers([CommandHandler(i.__name__, i, filters=Chat(chat_id=DEVS)) for i in dev_commands])

# Job queues
if (Bot.job_queue != None):
    Bot.job_queue.run_repeating(deleteImageCoroutine, DELETE_COROUTINE_TIME)
else:
    raise Exception("Jobs Couldn't be added.")
