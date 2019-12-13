# Install required Python packages using pip and requirements.txt
pip install -r requirements.txt

# Create database
python manage.py migrate

# Load initial data to database using Django fixtures 
python manage.py loaddata initial_departments
python manage.py loaddata initial_employees
python manage.py loaddata initial_projects
