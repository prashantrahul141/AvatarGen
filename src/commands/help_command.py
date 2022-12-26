# imports
from telegram import Update
from telegram.ext import ContextTypes

ALL_HELP_REPLIES = {}
BASIC_HELP = ''


async def help_command(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    _search_term = 'None'
    if ctx.args and len(ctx.args) > 0:
        _search_term = ctx.args[0]
    _help_message = BASIC_HELP

    try:
        _current_command_help = ALL_HELP_REPLIES[_search_term.upper()]
        _help_message = f"<b>{_current_command_help['NAME']}</b>\n"
        _help_message += f"{_current_command_help['DESCRIPTION']}"

    except:
        if _search_term != 'None':
            _help_message = "That command does not exist."

    await update.message.reply_text(_help_message, parse_mode='html')


def help_command_creator(_basic_commands: list, _image_commands: list, _dev_commands: list):
    '''Creates help messages from doc strings.'''

    global ALL_HELP_REPLIES, BASIC_HELP

    _output = {"BASIC": {"NAME": "Basic Commands", "DESCRIPTION":  "A set of basic commands.\n"},
               "IMAGE": {"NAME": "Image Manipulation", "DESCRIPTION": "A set of commands to edit images.\n"},
               "DEV": {"NAME": "Dev Commands", "DESCRIPTION": "A set of commands for debugging.\n"}}

    BASIC_HELP += "<b>Basic Commands</b>\n"
    for _each_command in _basic_commands:
        BASIC_HELP += f"/{_each_command.__name__} "
        _output[_each_command.__name__.upper()] = {}
        _output["BASIC"]["DESCRIPTION"] += '/' + _each_command.__name__ + " "
        _output[_each_command.__name__.upper()]["NAME"] = "/" + _each_command.__name__
        _output[_each_command.__name__.upper()]["DESCRIPTION"] = _each_command.__doc__

    BASIC_HELP += "\n\n<b>Image Manipulation</b>\n"
    for _each_command in _image_commands:
        BASIC_HELP += f"/{_each_command.__name__} "
        _output["IMAGE"]["DESCRIPTION"] += '/' + _each_command.__name__ + " "
        _output[_each_command.__name__.upper()] = {}
        _output[_each_command.__name__.upper()]["NAME"] = "/" + _each_command.__name__
        _output[_each_command.__name__.upper()]["DESCRIPTION"] = _each_command.__doc__

    BASIC_HELP += "\n\n<b>Dev Commands (not for public usage)</b>\n"
    for _each_command in _dev_commands:
        BASIC_HELP += f"/{_each_command.__name__} "
        _output["DEV"]["DESCRIPTION"] += '/' + _each_command.__name__ + " "
        _output[_each_command.__name__.upper()] = {}
        _output[_each_command.__name__.upper()]["NAME"] = "/" + _each_command.__name__
        _output[_each_command.__name__.upper()]["DESCRIPTION"] = _each_command.__doc__

    ALL_HELP_REPLIES = _output
