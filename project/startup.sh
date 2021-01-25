# !/bin/bash
python run.py && 
python manage.py db init && 
python manage.py db migrate && 
python manage db upgrade