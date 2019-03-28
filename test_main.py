#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt 
import paho.mqtt.publish as mqttPublish
import json

from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io

TTS_SAY = "hermes/tts/say"
END_SESSION = "hermes/dialogueManager/endSession"
ALL_INTENTS = "hermes/intent/#"
MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

class Calcul(object):

    def __init__(self):
        self.start_blocking()

    def add_callback(self, hermes, intent_message):
        nb_1 = intent_message.slots.nb_1.first().value
        nb_2 = intent_message.slots.nb_2.first().value
        result = nb_1 + nb_2
        hermes.publish_end_session(intent_message.session_id, "Ok ! le résultat est :")

    def hi_callback(self, hermes, intent_message):
        hermes.publish_end_session(intent_message.session_id, "Salut !")

    def master_intent_callback(self, hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
        if coming_intent == 'addNumber':
            self.add_callback(hermes, intent_message)
        if coming_intent == "Tengu:addNumber":
            self.hi_callback(hermes, intent_message)

    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.master_intent_callback).start()





if __name__ == '__main__':
    Calcul()
