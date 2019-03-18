# coding=utf-8
from application import bot


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)
    lista_cat = ["love","science","art","biographies","fantasy","romance","religion","recipes", "mystery","music", "medicine","history", "chilcren","sci-fi"]
    bot.send_message("Categorías disponibles: " + lista_cat)

@bot.message_handler(commands=['search_title'])
def searchTitle(message):
    if len(message.text.split('/search_title')[1]) > 1:
        object_search = message.text.split('/search_title')[1]
        bookname_list = list(object_search)
        for index, letra in enumerate(bookname_list):
            if re.match(" ", letra):
                bookname_list[index] = "+"
        bookname = ''.join(bookname_list)
        books_dic = requests.get('http://openlibrary.org/search.json?q=' + bookname).json()

        docs_dic = books_dic['docs']
        for doc in docs_dic:
            url = 'URL: https://openlibrary.org'+doc['key']
            if 'author_name'in doc:
                if 'publish_date' in doc:
                    author = "".join(doc['author_name'])
                    author = re.sub(r"(?<=\w)([A-Z])", r"|\1", author)
                    bot.send_message (doc['title'] + " - " + author )
                    bot.send_message ('Publish date: ' + doc['publish_date'][0])
                    bot.send_message (url)
                    bot.send_message('\n')
            elif 'publish_date' in doc:
                if 'author_name' not in doc:
                    bot.send_message (doc['title'] + " - " + "Unknown Author")
                    bot.send_message ('Publish date: ' + doc['publish_date'][0])
                    bot.send_message (url)
                    bot.send_message('\n')
            else:
                bot.send_message (doc['title'] + " - " + "Unknown Author")
                bot.send_message ('Publish date: Unknown')
                bot.send_message (url)
                bot.send_message('\n')
    else:

        bot.send_message(message.chat.id, "Por favor, escribe /search_title titulo")


@bot.message_handler(commands = ['search_category'])
def searchCategory(message):
    if len(message.text.split('/search_category')[1]) > 1:
        object_search = message.text.split('/search_category')[1]
        subject= object_search #selecionar por menus la que sea
        url = "https://openlibrary.org/subjects/"+subject+".json?limit=50"
        response = requests.get(url).json()

        works_diccionary=response['works']

        for i in range(0,10):
        	x= random.randrange(50)
        	if 'authors' in works_diccionary[x]:
        		bot.send_message ("Titulo:" + works_diccionary[x]['title'] )
        		bot.send_message ("Autor:" + works_diccionary[x]['authors'][0]['name']+'\n')

        	else:
        		bot.send_message ("Titulo:" + works_diccionary[x]['title'] + "        Autor: Desconocido")
        		bot.send_message ("Autor: Desconocido"+'\n')
    else:
        bot.send_message(message.chat.id, "Por favor, escribe /search_category categoría")

@bot.message_handler(commands = ['help'])
    lista_cat = ["love","science","art","biographies","fantasy","romance","religion","recipes", "mystery","music", "medicine","history", "chilcren","sci-fi"]
    bot.send_message(lista_cat)
