# imports
import logging
from Bot import Bot
from constants.VALUES import LOGGING_LEVEL

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=LOGGING_LEVEL
)
logger = logging.getLogger(__name__)


# running bot
Bot.run_polling()
