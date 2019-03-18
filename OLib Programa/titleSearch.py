# -*- coding: utf-8 -*-
import requests
import json
import re

print("Dime el nombre del libro a buscar")
bookname = raw_input()
bookname_list = list(bookname)
for index, letra in enumerate(bookname_list):
    if re.match(" ", letra):
        bookname_list[index] = "+"
bookname = ''.join(bookname_list)
books_dic = requests.get('http://openlibrary.org/search.json?q=' + bookname).json()

docs_dic = books_dic['docs']
for doc in docs_dic:
    if 'author_name' in doc:
        author = "".join(doc['author_name'])
        author = re.sub(r"(?<=\w)([A-Z])", r" | \1", author)
        print (doc['title'] + " - " + author )
        print ('URL: https://openlibrary.org'+doc['key'])
        print('\n')
    else:
        print (doc['title'] + " - " + "Unknown Author")
