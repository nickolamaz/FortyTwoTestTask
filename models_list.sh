#!/bin/bash
filename=`date +%d_%m_%Y`.dat

python manage.py models_list 2> ${filename}