# pip install python-telegram-bot --upgrade
# pip install beautifulsoup4
# pip install requests
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, ApplicationBuilder
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


def get_news():
    list_news = []
    r = requests.get("https://vnexpress.net/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_news.append(newdict)

    return list_news


# def hello(update: Update, context: CallbackContext):
#     update.message.reply_text(f'xin chao {update.effective_user.first_name}')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Xin chao: {update.effective_user.first_name}')


async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_news()
    str1 = ""

    for item in data:
        str1 += item["title"] + "\n"
    await update.message.reply_text(f'{str1}')


# def getlist(request):
#     product = Product.object.all()
#     return render(request, "product.html", product: "product")
tele_token = '7400665111:AAGoNT-SaGmGJZUzJRw9l-cWyQTWX-eNBSA'
app = ApplicationBuilder().token(tele_token).build()
# updater = Updater('7400665111:AAGoNT-SaGmGJZUzJRw9l-cWyQTWX-eNBSA', )

app.add_handler(CommandHandler('hello', hello))
app.add_handler(CommandHandler('news', news))

app.run_polling()
# app.idle()
