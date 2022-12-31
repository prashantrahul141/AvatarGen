# imports
from telegram import Update
from telegram.ext import ContextTypes
from utils.getImage import getImage
from utils.deleteImage import deleteImageCoroutine

COMMAND_LIST = "help - get help on how to use bot\n"


async def test_getImage(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    '''To test getImage utils function.'''
    _file_path, _file_name = await getImage(update)
    if _file_path != None:
        with open(_file_path, 'rb') as f:
            await update.message.reply_photo(f)
            return

    await update.message.reply_text("None")


async def test_deleteCoroutine(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    '''runs the delete coroutine.'''
    _total_deleted = await deleteImageCoroutine(ctx)
    await update.message.reply_text(f"{_total_deleted}")


async def test_forcedeleteCoroutine(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    '''runs the delete coroutine.'''
    _total_deleted = await deleteImageCoroutine(ctx, True)
    await update.message.reply_text(f"{_total_deleted}")


def create_commandlist(command_list: list) -> None:
    '''creates a command list for get_commandList func.'''
    global COMMAND_LIST
    for _each_command in command_list:
        COMMAND_LIST += f"{_each_command.__name__} - {_each_command.__doc__}\n"


async def get_commandList(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    '''returns a commmand list which can be used through t.m/BotFather'''
    global COMMAND_LIST
    await update.message.reply_text(COMMAND_LIST)
