from PIL import Image
import pytesseract


def img2txt(filename):
    """ Возвращает текст с картинки """
    text = pytesseract.image_to_string(Image.open(filename), lang='rus+eng')
    return text


print(img2txt('eng_pic.png'))
