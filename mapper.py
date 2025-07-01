#!/usr/bin/env python
import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin)
next(reader)  # skip the header

for row in reader:
    try:
        date_time = datetime.strptime(row[5], '%m/%d/%Y %H:%M')
        hour = date_time.hour
        traffic_volume = int(row[6])
        print(f"{hour}\t{traffic_volume}")
    except:
        continue
