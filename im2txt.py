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
    context.bot.sendMessage(chat_id=update.message.chat_id, text=img2txt('downloaded_img.jpg'))


photo_handler = MessageHandler(Filters.photo, get_photo)
updater.dispatcher.add_handler(photo_handler)
updater.start_polling()
updater.idle()
