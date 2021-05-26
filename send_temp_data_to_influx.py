#!/usr/bin/python3
"""
    Simple script for sending data from ruuvitag to influx db database. Note
    that configuration is in a separate example_configuration.py file.
"""

import sys
import time
#import requests
import subprocess
import example_configuration
from ruuvitag_sensor.ruuvi import RuuviTagSensor


def form_uri():
    """ Forms the whole URI based on configuration and returns it as a string.
    """
    if example_configuration.https_enabled:
        buf = "https://" + example_configuration.url
    else:
        buf = "http://" + example_configuration.url

    buf += ":" + example_configuration.influx_port + "/write?"

    buf += "db=" + example_configuration.db_name
    buf += "&u=" + example_configuration.user_name
    buf += "&p=" + example_configuration.password

    return buf


"""
r = requests.post("http://bugs.python.org", data={'number': 12524, 'type': 'issue', 'action': 'show'})
"""


def form_payload(measure, current_tag, data_set):
    """
    Forms the binary data for POST to the database. Returns a list of tuples.
    """
    buf = current_tag[0]
    buf += " " + measure + "=" + str(data_set[current_tag[1]][measure]) + " "
    buf += str(int(round(time.time() * 10 ** 9)))

    return buf


def write_values_to_database(measurement, data_set, current_tag):
    """ Handles writing the values to the databese. """
    uri = form_uri()
    print(uri)
    payload = form_payload(measure=measurement, current_tag=current_tag, data_set=data_set)
    print(payload)
    subprocess.run(["curl", "-i", "-X", "POST", uri, "--data-binary", payload])

def main():
    """ Main. """
    time.sleep(example_configuration.delay)

    macs = []
    print('Configured ruuvitags:')
    for tag in example_configuration.ruuvitags:
        print(tag)
        macs.append(tag[1])

    all_ruuvitags = RuuviTagSensor.get_data_for_sensors(macs,
                                                        example_configuration.ruuvi_timeout_sec)

    for mac_addr in all_ruuvitags:
        current_tag = ""
        for tag in example_configuration.ruuvitags:
            if tag[1] == mac_addr:
                current_tag = tag

        write_values_to_database('temperature', all_ruuvitags, current_tag)
        write_values_to_database('humidity', all_ruuvitags, current_tag)
        write_values_to_database('pressure', all_ruuvitags, current_tag)


if __name__ == '__main__':
    sys.exit(main())
