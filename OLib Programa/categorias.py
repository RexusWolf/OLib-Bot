# -*- coding: utf-8 -*-
import requests
import json
import random



url = "https://openlibrary.org/dev/docs/api/subjects/love.json?details=true"





headers = {
        'cache-control': "no-cache"
}

response = requests.get('https://openlibrary.org/subjects/love.json?limit=100').json()


works_diccionary=response['works']

#random.shuffle(works_diccionary)

#print (response.text)
for i in range(0,10):
	x= random.randrange(99)
	if 'authors' in works_diccionary[x]:
		print ("Titulo:" + works_diccionary[x]['title'] )
		print ("Autor:" + works_diccionary[x]['authors'][0]['name']+'\n')
		
	else:
		print ("Titulo:" + works_diccionary[x]['title'] + "        Autor: Desconocido")
		print ("Autor: Desconocido"+'\n')
		

