# imports
from constants.VALUES import LOGGING_LEVEL
import logging


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=LOGGING_LEVEL
)
logger = logging.getLogger(__name__)

# creating and setting up bot
from Bot import Bot  # noqa

# running bot
print("Starting up bot.")
Bot.run_polling()
