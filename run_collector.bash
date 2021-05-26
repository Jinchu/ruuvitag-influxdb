#!/bin/bash
cd /home/ubuntu/ruuvitag_collect_to_influx

sleep_time=$(( ( RANDOM % 30 )  + 1 ))
echo "sleeping for $sleep_time" >> data.log
sleep ${sleep_time}

echo "  " >> data.log
echo "  " >> data.log
date -R >> data.log
python3 send_temp_data_to_influx.py >> data.log
echo "-----------" >> data.log

sleep_time=$(( ( RANDOM % 30 )  + 30 ))
echo "sleeping for $sleep_time" >> data.log
sleep ${sleep_time}

python3 send_temp_data_to_influx.py >> data.log
echo "-----------" >> data.log
