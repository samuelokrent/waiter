#!/bin/bash

python up_for_grabs/manage.py runserver &
python mailbot/readmail.py
