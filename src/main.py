# imports
from constants.VALUES import LOGGING_LEVEL, RUNNING_IN_BACKGROUND

# creating and setting up bot
from Bot import Bot  # noqa

if not RUNNING_IN_BACKGROUND:
    import logging

    # Enable logging
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=LOGGING_LEVEL
    )
    logger = logging.getLogger(__name__)

    print("Starting up bot.")

# running bot
Bot.run_polling()
