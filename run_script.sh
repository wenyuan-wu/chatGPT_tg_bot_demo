#!/bin/bash

source venv/bin/activate
nohup python run_bot.py >> output.log 2>&1 & echo $! >> output.log

