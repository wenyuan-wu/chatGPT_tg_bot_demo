#!/bin/bash

source .env
source venv/bin/activate
nohup python run_bot.py > output.log &
