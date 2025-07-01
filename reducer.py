#!/usr/bin/env python
import sys

current_hour = None
total = 0
count = 0

for line in sys.stdin:
    hour, volume = line.strip().split('\t')
    volume = int(volume)

    if current_hour == hour:
        total += volume
        count += 1
    else:
        if current_hour is not None:
            print(f"{current_hour}\t{total // count}")
        current_hour = hour
        total = volume
        count = 1

if current_hour == hour:
    print(f"{current_hour}\t{total // count}")
