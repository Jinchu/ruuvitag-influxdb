"""
    An example configuration file for send_temp_data_to_influx.py
"""

delay = 0  # Time in seconds before anything happens. Useful for load distrib.

url = "www.example.com"
https_enabled = True
influx_port = "8086"

db_name = "temperature"
user_name = "user"
password = "Hunter2"

ruuvitags = [['backyard', 'C3:B1:CC:DD:EE:FF'], ['garage', 'C3:B1:CC:DD:EE:00'], ['bedroom', 'C3:B1:CC:DD:EE:11'] ]
ruuvi_timeout_sec = 30
