#!/usr/bin/env python3
from scapy.all import *
import sys
import os

dst_ip = "192.168.56.104"
port = 555
file_path = "--File path here--"

file_size = os.path.getsize(file_path)

with open(file_path, "rb") as f:
  file_array = []
  while True:
    file_content = f.read(5000)
    if len(file_content) < 5000:
      file_array.append(file_content)
      break
    else:
      file_array.append(file_content)

counter = 1
for item in file_array:
  print(item)
  packet = IP(dst=dst_ip,id=12345)/UDP(sport=100, dport=port)/item
  print ("Packet no#"+str(counter)+" Sent!")
  counter+=1
  send(packet)
