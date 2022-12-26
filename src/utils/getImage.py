import uuid
from os import path
from telegram import Update, PhotoSize, File, User
from constants.VALUES import PHOTO_SIZE, USER_GIVEN_IMAGES_DIR


async def getImageObject(update: Update) -> PhotoSize | None:
    # if message is replied to another message
    if update.message.reply_to_message != None:
        if len(update.message.reply_to_message.photo) > 0:
            photo = update.message.reply_to_message.photo
            return photo[PHOTO_SIZE]

        photo = await update.message.reply_to_message.from_user.get_profile_photos()
        if photo != None and photo.total_count > 0:
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
    _effective_user = update.effective_user
    if isinstance(_effective_user, User):
        photo = await _effective_user.get_profile_photos()
        if photo != None and photo.total_count > 0:
            return photo.photos[0][PHOTO_SIZE]

    return None


async def getImage(update: Update) -> list[str] | list[None]:
    _photo_size = await getImageObject(update)
    if _photo_size != None:
        _image_file: File or None = await _photo_size.get_file()
        _temp_name = f"{uuid.uuid4().hex}.jpg"
        _file_path = path.join(USER_GIVEN_IMAGES_DIR, _temp_name)
        await _image_file.download_to_drive(_file_path)
        return [_file_path, _temp_name]

    return [None, None]
