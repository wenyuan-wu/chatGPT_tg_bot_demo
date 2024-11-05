#!/bin/bash

source venv/bin/activate
nohup python run_bot.py > output.log &
