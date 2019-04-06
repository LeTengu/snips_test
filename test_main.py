#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):
    sentence = 'La réponse : '

    if intent_message.intent.intent_name == 'addNumber':
        sentence += 'pas de Tengu '
    elif intent_message.intent.intent_name == 'Tengu:addNumber':
        sentence += 'avec Tengu '
    else:
        return

    nb_1 = intent_message.slots.nb_1.first()
    nb_2 = intent_message.slots.nb_2.first()

    if nb_1 is not None:
        sentence += 'nb 1 : ' + nb_1.value
    if nb_2 is not None:
        sentence += 'nb 2 : ' + nb_2.value

    hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
