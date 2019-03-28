#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt 
import paho.mqtt.publish as mqttPublishpl
import json

ADD_NUMBER = 'hermes/intent/Tengu:addNumber'
SALUT = 'hermes/intent/Tengu:SayHi'

def on_connect(client, userdata, flags, rc): 
    print('Connected') 
    mqtt.subscribe(ADD_NUMBER)

def on_message(client, userdata, msg):

    # Parse the json response
    intent_json = json.loads(msg.payload)
    sessionId = intent_json['sessionId']
    intentName = intent_json['intent']['intentName']
    slots = intent_json['slots']
    print('Intent {}'.format(intentName))
    for slot in slots:
        slot_name = slot['slotName']
        raw_value = slot['rawValue']
        value = slot['value']['value']
        print('Slot {} -> \n\tRaw: {} \tValue: {}'.format(slot_name, raw_value, value))

    if intentName == 'addNumber':
        endTalk(sessionId, 'bravo')
    elif intentName == 'SayHi':
        endTalk(sessionId, 'Bonjour monsieur !')


def endTalk(sessionId, text):
    mqttClient.publish('hermes/dialogueManager/endSession', json.dumps({
        'sessionId': sessionId,
        'text': text
    }))

if __name__ == '__main__':
    mqtt = mqtt.Client() 
    mqtt.on_connect = on_connect
    mqtt.on_message = on_message
    mqtt.connect('raspberrypi.local', 1883) 
    mqtt.loop_forever()
