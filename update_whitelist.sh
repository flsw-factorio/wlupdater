#!/bin/bash


iptables -F

for addr in $(cat /home/ec2-user/whitelist.txt | cut -f1)
do
  iptables -A INPUT -s $addr -j ACCEPT
done

iptables -A INPUT -p udp --destination-port 34197 -j DROP
