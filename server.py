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

port = int(os.environ.get("PORT"))

#token 08/03/2017 - 20:33h
token = "EAARnqZCEhc8sBAFjSXzGdTcUSZCZA5zW8v6futWExamOZBWquFzN8ErpBthsouZCTfjtZCibYd7ZCijYqoxB8FmRmpNSpEP9y2X43VqxxsfrKvabmPZCJtj4QxKZAH6IWpYp3X9fE7ksGj8vavWGT9Ct72RS6OvudZCqeMFRURCkLKrwZDZD"
    

''' 
# Data - 03/03/2017 - 22:58h
token = 'EAARnqZCEhc8sBAJyXtCJpjLQp3ZCJ7pPPRM8ZCRzvQ4hZAZBOMMUQ7UDHp68LtoJ0dCIURWyd6r1P2hoXlmP29l5Jpc5jgtrmIDertEdrXOS7enxzmFWB7nkPzG8Qo04UOqHndmZCc3AJXgXRYWdDmCaT3vef0bWpltQs9F6YaVwZDZD'


#FUNCIONA PARA AUTENTICAR O WEBHOOK PRIMARIO -----
@app.route('/', methods=['GET'])
def handle_verification():
    return request.args['hub.challenge']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
# -----------------------------------------------------
'''
@app.route('/', methods=['GET'])
def handle_verification():
  print "--- Handling Verification. -----"
  if request.args.get('hub.verify_token', '') == 'quintanilha':
    print "Verification successful!"
    return request.args.get('hub.challenge', '')
  else:
    print "Verification failed!"
    return 'Error, wrong validation token'
    
def reply(user_id, msg):
    data = {
    "recipient": {"id": user_id},
    "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.8/me/messages/?access_token=" +token, json=data)
    print(resp.content)

@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.get_json(force=True)
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    print('sender: {}'.format(sender))
    message = data['entry'][0]['messaging'][0]['message']['text']
    message.put('text','FUNCIONA?')
    print('message: {}'.format(message))

    reply(sender, message)
 
    return "ok"

''' TESTE FUNCIONAL
def webhook():

    #Uid - QuintanilhaEdu: 1746854645630719
    user = '1746854645630719'
    #token 08/03/2017 - 20:33h
    token = "EAARnqZCEhc8sBAFjSXzGdTcUSZCZA5zW8v6futWExamOZBWquFzN8ErpBthsouZCTfjtZCibYd7ZCijYqoxB8FmRmpNSpEP9y2X43VqxxsfrKvabmPZCJtj4QxKZAH6IWpYp3X9fE7ksGj8vavWGT9Ct72RS6OvudZCqeMFRURCkLKrwZDZD"

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
'''

######### For HEROKU DEPLOY  ##########
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
#######################################
