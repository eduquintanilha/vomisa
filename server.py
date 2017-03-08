#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sex 24 Fev 2017 22:32:42 BRT - Inicio

from flask import Flask, request

import os
import requests
import traceback
import json

## Token = 25/02/2017 - 01:03h ##
## EAARnqZCEhc8sBAM4kYOmmK0R4lQ7zu93rLg7ZBr1OZBqsCZBch1wzTuijNpnH2ZAadkVyhpojiiSBLhIj3jAi4ZCq0eNeKgnKOrMISKbErHAarptpJ7slGNg6y5zQYL8C2nBWQs89nkNSnq7ZAJ107LVG0QopUtuZCZB37Uk5j3qUYAZDZD

#Token - 25/02/2017 - 10:48h
# EAARnqZCEhc8sBAL3nFiAMwPIb5g3PEWV8SiUQkBGhMPIJXpWiCyIZBDnK5uFJNiVbBxuDExgaTfucU3Qvgufwu9P1ODgsdkQLskAamBXMXnq1QSoKjwmK9XLBCxsmBmt5rJdufcKDByYFj1WayWI6CWG4Q7S4OJiZCDzEAVrQZDZD



# Autenticação nos Webhooks 

app = Flask(__name__)
 
# Data - 03/03/2017 - 22:58h
token = 'EAARnqZCEhc8sBAJyXtCJpjLQp3ZCJ7pPPRM8ZCRzvQ4hZAZBOMMUQ7UDHp68LtoJ0dCIURWyd6r1P2hoXlmP29l5Jpc5jgtrmIDertEdrXOS7enxzmFWB7nkPzG8Qo04UOqHndmZCc3AJXgXRYWdDmCaT3vef0bWpltQs9F6YaVwZDZD'


#FUNCIONA PARA AUTENTICAR O WEBHOOK PRIMARIO -----
@app.route('/', methods=['GET'])
def handle_verification():
    return request.args['hub.challenge']

if __name__ == '__main__':
    app.run(debug=True)
# -----------------------------------------------------
'''
@app.route('/', methods=['POST'])

def webhook():

    #Uid - QuintanilhaEdu: 1746854645630719
    user = '1746854645630719'
    #token = "EAARnqZCEhc8sBAM4kYOmmK0R4lQ7zu93rLg7ZBr1OZBqsCZBch1wzTuijNpnH2ZAadkVyhpojiiSBLhIj3jAi4ZCq0eNeKgnKOrMISKbErHAarptpJ7slGNg6y5zQYL8C2nBWQs89nkNSnq7ZAJ107LVG0QopUtuZCZB37Uk5j3qUYAZDZD"
    
    data = json.loads(request.data.decode('utf-8'))

    for entry in data["entry"]:
    	for messaging_event in entry["messaging"]:

    		if messaging_event.get("message"):
    			text = data['entry'][0]['messaging'][0]['message']
    			#print('\n=====================\n{}\n==============\n\n'.format(text))
    			
    			if(text == "teste" | text == "Teste"):
    				sender = data['entry'][0]['messaging'][0]['sender']['id']
    				payload = {'recipient': {'id': sender}, 'message': {'text': "Seu teste funcionou!"}}
    				r = requests.post('https://graph.facebook.com/v2.8/me/messages/?access_token='+token,json=payload)
    			else:
    				sender = data['entry'][0]['messaging'][0]['sender']['id']
    				payload = {'recipient': {'id': sender}, 'message': {'text': "Desculpe. Não reconheço esses comandos.  :("}}
    				r = requests.post('https://graph.facebook.com/v2.8/me/messages/?access_token='+token,json=payload)

    			#typ = {'recipient':{'id':sender},'sender_action':'typing_on'}

    			#c = requests.post('https://graph.facebook.com/v2.8/me/messages/?access_token='+token,json=typ)

    return("\nok\n",200)


if __name__ == '__main__':
    app.run(debug=True)
'''
