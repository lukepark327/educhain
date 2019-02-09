#!/usr/bin/env bash

# nohup python3 main.py --nodes=24
python3 main.py --nodes=3 --neighbors=2 --prop_delay_avg=5000 --prop_delay_std=2000
