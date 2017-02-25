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




# Autenticação nos Webhooks 

app = Flask(__name__)
 
@app.route('/', methods=['GET'])
def handle_verification():
    if request.args['hub.verify_token'] == 'EAARnqZCEhc8sBAM4kYOmmK0R4lQ7zu93rLg7ZBr1OZBqsCZBch1wzTuijNpnH2ZAadkVyhpojiiSBLhIj3jAi4ZCq0eNeKgnKOrMISKbErHAarptpJ7slGNg6y5zQYL8C2nBWQs89nkNSnq7ZAJ107LVG0QopUtuZCZB37Uk5j3qUYAZDZD':
        return request.args['hub.challenge','ok']
    else:
        return "Error, Invalid Token!"

@app.route('/', methods=['POST'])

def webhook():
   #s data = request.get_json()    

    #Uid - QuintanilhaEdu: 1746854645630719
    user = '1746854645630719'
    token = "EAARnqZCEhc8sBAM4kYOmmK0R4lQ7zu93rLg7ZBr1OZBqsCZBch1wzTuijNpnH2ZAadkVyhpojiiSBLhIj3jAi4ZCq0eNeKgnKOrMISKbErHAarptpJ7slGNg6y5zQYL8C2nBWQs89nkNSnq7ZAJ107LVG0QopUtuZCZB37Uk5j3qUYAZDZD"
    
    data = json.loads(request.data.decode('utf-8'))

    #text = data['entry'][0]['messaging'][0]['message']
    #print('\n=====================\n{}\n==============\n\n'.format(text))
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    payload = {'recipient': {'id': sender}, 'message': {'text': "Hello World"}}
    r = requests.post('https://graph.facebook.com/v2.8/me/messages/?access_token='+token,json=payload)

    #typ = {'recipient':{'id':sender},'sender_action':'typing_on'}

    #c = requests.post('https://graph.facebook.com/v2.8/me/messages/?access_token='+token,json=typ)



    return("ok",200)

if __name__ == '__main__':
	port = int(os.environ.get("PORT",5000))
	#app.run(debug=True)
	app.run(host='0.0.0.0', port=port)