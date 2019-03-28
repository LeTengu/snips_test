#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import MqttOptions

import snips_common

class Calcul(snips_common.ActionWrapper):

    """def __init__(self):
        # start listen MQTT
        self.start_blocking()
    """

    def addNumber_callback(self):
        # action code
        
        nb_1 = self.intent_message.slots.nb_1.first().value
        nb_2 = self.intent_message.slots.nb_2.first().value
        result = nb_1 + nb_2

        self.end_session("Le résultat est de :",result)

    """
    def master_intent_callback(self, hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
        if coming_intent == 'addNumber':
            self.addNumber_callback(hermes, intent_message)


    # register callback function and start MQTT
    def start_blocking(self):
        mqtt_options = MqttOptions()

        with Hermes(mqtt_options) as h:
            h.subscribe_intents(self.master_intent_callback).start()
    """

if __name__ == '__main__':
    mqtt_options = MqttOptions()

    with Hermes(mqtt_options) as h:
        h.subscribe_intent("Tengu:addNumber", Calcul.callback).start()