# Django BIA Task

This is a Django project showcasing various concepts and features of django basics and REST framework.

## Requirements

Make sure you have [Python](https://www.python.org/downloads/) and [virtualenv](https://pypi.org/project/virtualenv/) installed.

```bash
# Clone the repository
git clone https://github.com/Er-shivam11/Django-concepts.git

# Navigate to the project directory
cd Django-concepts

# Create a virtual environment
1.virtualenv env or
2.python -m venv env

# Activate the virtual environment
# On Windows
\env\Scripts\activate
# On macOS/Linux
source env/bin/activate

# Install dependencies
pip install -r requirements.txt
cd BIA_ASSIGNMENT

# Create a superuser
python manage.py createsuperuser

# Apply database migrations
python manage.py makemigrations migrate

# Run the development server
python manage.py runserver

