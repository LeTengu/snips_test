#!/usr/bin/env python3
from hermes_python.hermes import Hermes
from hermes_python.ontology import MqttOptions

import snips_common


class ActionSalutation(snips_common.ActionWrapper):
    def action(self):
        self.end_session("Bonjour à vous")


if __name__ == "__main__":
    mqtt_opts = MqttOptions()

    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("Tengu:SayHi", ActionSalutation.callback).start()
