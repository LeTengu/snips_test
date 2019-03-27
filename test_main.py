#!/usr/bin/env python
# -*- coding: utf-8 -*-

from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io

CONFIG_INI = "config.ini"

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

class Calcul(object):

    def __init__(self):
        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
        except :
            self.config = None

        # start listen MQTT
        self.start_blocking()


    def addNumber_callback(self, hermes, intent_message):
        # if not continue, terminate session
        hermes.publish_end_session(intent_message.session_id, "Pas possible Monsieur !")

        # action code
        if intent_message.slots.nb_1 and intent_message.slots.nb_2:
            nb_1 = intent_message.slots.nb_1.first().value()
            nb_2 = intent_message.slots.nb_2.first().value()
            result = int(nb_1 + nb_2)

        # audio return
        hermes.publish_start_session_notification(intent_message.site_id, "Le résultat est de", result)


    def master_intent_callback(self, hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
        if coming_intent == 'Tengu:addNumber':
            self.addNumber_callback(hermes, intent_message)


    # register callback function and start MQTT
    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subcribe_intents(self.master_intent_callback).start()

if __name__ == '__main__':
    Calcul()