#!/usr/bin/env python3
from hermes_python.hermes import Hermes
from hermes_python.ontology import MqttOptions

import snips_common

class AddNumber(snips_common.ActionWrapper):
    
    def action(self):
        number_1 = self.intent_message.slots.nb_1.first().value
        number_2 = self.intent_message.slots.nb_2.first().value
        result = nb_1 * nb_2
        self.end_session("Le résultat de l'addition est ",result)

if __name__ == '__main__':
    mqtt_opts = MqttOptions()

    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("Tengu:addNumber", AddNumber.callback).start()

