# coding=utf-8
from application import bot
import requests
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name + '!')


@bot.message_handler(commands=['search_author'])
def search_author(message):
    if len(message.text.split('/search_author')[1]) > 1:
        object_search = message.text.split('/search_author')[1]
        url = 'http://openlibrary.org/search.json?author=' + object_search

        resp = requests.get(url).json()

        docsDictionary = resp['docs']

        click_kb = InlineKeyboardMarkup()
        list_titles = []
        i = 0

        for doc in docsDictionary:
            title = doc['title']
            i += 1
            """     bot.send_message(message.chat.id, doc['title'], parse_mode="HTML")  """
            click_button = InlineKeyboardButton(title, callback_data='parent_' + title)
            list_titles.append(click_button)
            if i % 2 == 0:
                click_kb.row(*list_titles)
                list_titles = []
            bot.send_message(message.chat.id, "<b>Aquí se muestran todos los titulos de " + object_search + "...</b>", parse_mode="HTML", reply_markup=click_kb, disable_web_page_preview=True)
    else:

        bot.send_message(message.chat.id, 'Por favor, escribe /search_author "autor"', parse_mode="HTML")
"""
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data.startswith("parent_"):
        #mandar categorias hijos
        response = requests.get("https://openlibrary.org"+, allow_redirects = True)
        list_message = call.data.split("parent_")
        author = list_message[1]
        soup = BeautifulSoup(response.content)
        category = soup.find("h2", text=name_category)
        parent_div = category.parent()[1]
        subcategories = parent_div.findAll("a", {"class":"nav_a"})
        click_kb = InlineKeyboardMarkup()
        for subcategory in subcategories:
            name_subcategory = subcategory.get_text()
            click_button = InlineKeyboardButton(name_subcategory, callback_data='subcategory_' + name_subcategory)
            click_kb.row(click_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "Haz click en lo que desees", reply_markup=click_kb)
        #import ipdb; ipdb.set_trace()
    """
