from PIL import Image 
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(filename):
    """ This function will handle the core OCR processing of images. """
    text = pytesseract.image_to_string(Image.open(filename))
    return text

print(ocr_core('C:\dev\im2txt\ine.jpg'))
