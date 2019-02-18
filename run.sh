#!/usr/bin/env bash

# nohup python3 main.py --nodes=24
nohup python3 main.py --nodes=400 --neighbors=8 --prop_delay_avg=5000 --prop_delay_std=2000 --sleep=60
