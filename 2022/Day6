"""
Advent Of Code 2022 Day 6
Author: PineapplePeddler
Date: 06/12/22
"""

def check_packet_start(window):
    print(window)
    for i in range(0,len(window)-1):
        if window[i] in window[i+1:]:
            return False
    
    return True


# Import signal data
with open("2022/Day6_Input.txt") as f:
   signal = f.read()

# Task 1 - Detect start of packet

data_start = 0

# Detect start of signal.
for i in range(3,len(signal)-4):
    if check_packet_start(signal[i:i+4]):
        data_start = i + 4
        break

print(data_start)

# Task 2 - Detect start of message (Same but 14 long)

message_start = 0

for i in range(3,len(signal)-14):
    if check_packet_start(signal[i:i+14]):
        message_start = i + 14
        break

print(message_start)



