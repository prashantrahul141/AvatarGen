from telegram import Update, PhotoSize
from constants.VALUES import PHOTO_SIZE


async def getImageObject(update: Update) -> PhotoSize | None:
    # if message is replied to another message
    if update.message.reply_to_message != None:
        if len(update.message.reply_to_message.photo) > 0:
            photo = update.message.reply_to_message.photo
            return photo[PHOTO_SIZE]

        photo = await update.message.reply_to_message.from_user.get_profile_photos()
        if photo.total_count > 0:
            return photo.photos[0][PHOTO_SIZE]

    # if message contains username
    # if len(update.message.entities) > 0:
    #     for _each_entity in update.message.entities:
    #         if _each_entity.type == 'text_mention':
    #             if _each_entity.user != None:
    #                 photo = await _each_entity.user.get_profile_photos()
    #                 if photo.total_count > 0:
    #                     return photo.photos[0][PHOTO_SIZE]

    #         if _each_entity.type == 'mention':
    #             _mentioned_username = update.message.text[_each_entity.offset:][:_each_entity.length]

    # tries to get user's avatar as a last resort
    photo = await update.effective_user.get_profile_photos()
    if photo.total_count > 0:
        return photo.photos[0][PHOTO_SIZE]

    return None


async def getImage(update: Update):
    _image_object = await getImageObject(update)
    return _image_object
