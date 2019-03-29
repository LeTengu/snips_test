#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes, MqttOptions

def parle(hermes, intent_message):
    nb_1 = intent_message.slots.nb_1.first().value
    hermes.publish_end_session(intent_message.session_id, "Numéro 1 : {}".format(nb_1))

with Hermes(mqtt_options=MqttOptions()) as h:
    h.subscribe_intent("addNumber", parle).start()