#!/bin/sh

iptables -I INPUT 1 -s $1 -j DROP
