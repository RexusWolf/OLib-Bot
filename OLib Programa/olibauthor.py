# -*- coding: utf-8 -*-
import requests
import json

""" @bot.message_handler(commands=['search_author'])
def search_cheaper(message):
    if len(message.text.split('/search_author')[1]) > 1:
        object_search = message.text.split('/search_author')[1]
        url = 'http://openlibrary.org/search.json?author=' + object_search.encode(encoding='utf-8', errors='strict')'
        response = requests.get(url)

"""
autor = 'tolkien'

url = 'http://openlibrary.org/search.json?author=' + autor


resp = requests.get(url).json()



docsDictionary = resp['docs']

for doc in docsDictionary:
    print doc['title']
