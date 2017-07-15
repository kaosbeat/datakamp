#!/bin/bash
while :
do
	python datakamp/MobileReader_RPi.py
	sleep 4
	echo "Python crashed"
done