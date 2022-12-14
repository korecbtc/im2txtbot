import os

import pytesseract
from dotenv import load_dotenv
from PIL import Image
from telegram.ext import Filters, MessageHandler, Updater

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
updater = Updater(token=TOKEN)


def img2txt(filename):
    '''Возвращает текст с картинки'''
    text = pytesseract.image_to_string(Image.open(filename), lang='rus+eng')
    if not text.strip():
        text = 'Не удалось распознать текст на картинке.'
    return text


def get_photo(update, context):
    '''Скачивает фотографию от пользователя и отправлеят текст'''
    file_id = update.message.photo[-1]
    newFile = context.bot.getFile(file_id)
    newFile.download('downloaded_img.jpg')
    context.bot.sendMessage(
        chat_id=update.message.chat_id, text=img2txt('downloaded_img.jpg')
    )


def give_me_a_photo_please(update, context):
    '''Обрабатывает текст, видео от пользователя'''
    context.bot.sendMessage(
        chat_id=update.message.chat_id,
        text='Привет! Кинь сюда картинку с текстом'
    )


def main():
    photo_handler = MessageHandler(Filters.photo, get_photo)
    video_handler = MessageHandler(Filters.video, give_me_a_photo_please)
    text_handler = MessageHandler(Filters.text, give_me_a_photo_please)
    updater.dispatcher.add_handler(photo_handler)
    updater.dispatcher.add_handler(video_handler)
    updater.dispatcher.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
