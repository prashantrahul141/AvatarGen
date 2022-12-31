# imports
from os import getenv
import telegram
from telegram.ext import Application, CommandHandler
from telegram.ext.filters import Chat
from dotenv import load_dotenv
from commands.basic_commands import alive
from commands.image_commands import blur, pixelate, emojioverlay, deepfry, caption1, caption2, cropcircle
from commands.image_commands import rotate, ascify, crop, saturate, grayscale, flip, mirror, invert
from commands.dev_commands import test_getImage, test_deleteCoroutine, test_forcedeleteCoroutine, create_commandlist, get_commandList
from commands.help_command import help_command_creator, help_command
from utils.deleteImage import deleteImageCoroutine
from constants.VALUES import DELETE_COROUTINE_TIME, READ_TIMEOUT, WRITE_TIMEOUT

# loading envs
load_dotenv()

# devs ids
_devs_ids = []

_get_devs = True
_dev_number = 0
while _get_devs:
    _dev_id = getenv(f"DEV_ID_{_dev_number}")  # type: ignore
    _dev_number += 1
    if _dev_id != None:
        _devs_ids.append(int(_dev_id))
    else:
        break

DEVS = set(_devs_ids)

# Create the Application and pass it your bot's token.
Bot = Application.builder().token(getenv("TOKEN")).read_timeout(READ_TIMEOUT).write_timeout(WRITE_TIMEOUT).build()  # type: ignore

# defining commands
basic_commands = [alive]
image_commands = [blur, pixelate, emojioverlay, deepfry, caption1, caption2,
                  cropcircle, rotate, ascify, crop, saturate, grayscale, flip, mirror, invert]
dev_commands = [test_getImage, test_deleteCoroutine, test_forcedeleteCoroutine, get_commandList]
user_commands = [CommandHandler(i.__name__, i) for i in [*basic_commands, *image_commands]]

# setting up help command
help_command_creator(basic_commands, image_commands, dev_commands)

# setting up get_commandlist command
create_commandlist(image_commands)

# adding to bot
Bot.add_handler(CommandHandler("help", help_command))
Bot.add_handlers(user_commands)  # type: ignore
Bot.add_handlers([CommandHandler(i.__name__, i, filters=Chat(chat_id=DEVS)) for i in dev_commands])

# Job queues
if (Bot.job_queue != None):
    Bot.job_queue.run_repeating(deleteImageCoroutine, DELETE_COROUTINE_TIME)
else:
    raise Exception("Jobs Couldn't be added.")
