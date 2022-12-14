# Проект im2txtBot

### Описание
Телеграм-бот для распознавания текста с картинки. Все просто - отправляешь боту картинку, например, фото документа, в ответ он присылает текст с картинки. Распознает 2 языка: русский и английский. Лучше всего работает с черно-белыми документами, такими как скан страницы из книги. Написан в познавательно-практических целях. Удобнее просто отправить боту картинку и получить текст, чем ставить для этого отдельное приложение или пользоваться WEB-ресурсами. Кроме того, картинка и текст остается у меня, поэтому, можно распознавать конфиденциальные документы.
### Запуск проекта:

- Клонируйте репозиторий:
```
git clone git@github.com:korecbtc/im2txtbot.git
```
 - Создайте файл .env и пропишите в него строчку
 ```
 BOT_TOKEN=<токен вашего бота>
 ```
 - Установите и активируйте виртуальное окружение:
```
python -m venv venv
source venv/bin/activate
```
- Установите библиотеку tesseract и языковой пакет к ней
```
sudo apt-get update
sudo apt-get install libleptonica-dev tesseract-ocr libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn
sudo apt-get install tesseract-ocr-rus
```
 - В папке с проектом установите зависимости из файла requirements.txt

``` 
pip install -r requirements.txt
```
 - Запустите программу
***

# Примеры
![Скан](https://github.com/korecbtc/im2txtbot/blob/master/rus_pic.jpg)
![Результат](https://github.com/korecbtc/im2txtbot/blob/master/telegram_bot_response.png)
# Технологии
Библиотеки:

tesseract

telegram

# Автор
Корец Иван
