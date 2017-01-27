#!/bin/bash

mount /dev/sda1 /usr/src/app/mnt

if [ ! -f /usr/src/app/mnt/logging/speedtest.csv ]; then
    /usr/local/bin/speedtest-cli --csv-header >> /usr/src/app/mnt/logging/speedtest.csv
    /usr/local/bin/speedtest-cli --csv >> /usr/src/app/mnt/logging/speedtest.csv
fi

systemctl start speedtest.timer

python /usr/src/app/server.py
