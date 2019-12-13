# SWENGS Homework 2 Backend

## Install required Python packages using pip and requirements.txt
```shell
pip install -r requirements.txt
```

## Create database
```shell
python manage.py migrate
```

## Load initial data to database using Django fixtures 
```shell
python manage.py loaddata initial_departments
python manage.py loaddata initial_employees
python manage.py loaddata initial_projects
```
