from PIL import Image
import pytesseract
import os
from dotenv import load_dotenv
import telegram
from telegram.ext import Updater, Filters, MessageHandler

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
updater = Updater(token=TOKEN)


def img2txt(filename):
    '''Возвращает текст с картинки'''
    text = pytesseract.image_to_string(Image.open(filename), lang='rus+eng')
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


photo_handler = MessageHandler(Filters.photo, get_photo)
video_handler = MessageHandler(Filters.video, give_me_a_photo_please)
text_handler = MessageHandler(Filters.text, give_me_a_photo_please)
updater.dispatcher.add_handler(photo_handler)
updater.dispatcher.add_handler(video_handler)
updater.dispatcher.add_handler(text_handler)
updater.start_polling()
updater.idle()
