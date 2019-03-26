#!/usr/bin/env python3
# encoding: utf-8
"""
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print('Connected')
    mqtt.surscribe('hermes/intent/#')

mqtt = mqtt.Client()
mqtt.on_connect = on_connect
mqtt.connect('raspberry,local', 1883)
mqtt.loop_forever()
"""

from hermes_python.hermes import Hermes
from hermes_python.ontology import MqttOptions

import snips_common

class AddNumber(snips_common.ActionWrapper):
    
    def action(self):
        number_1 = self.intent_message.slots.nb_1.first().value
        number_2 = self.intent_message.slots.nb_2.first().value
        result = nb_1 + nb_2
        self.end_session("Le résultat de l'addition est ",result)

if __name__ == '__main__':
    mqtt_opts = MqttOptions()

    with Hermes('raspberrypi.local:1883') as h:
        h.subscribe_intent("Tengu:addNumber", AddNumber.callback).start()

