# GreenBus
A bus booking system.
Documentation for APIs can be found [here](https://drive.google.com/file/d/1esWZ2qqCA1ZMgvjvw9jjyWus5ZeTQbkR/view?usp=sharing).
# Requirements
- Python
- pip

# Installation
Navigate to the root directory of the project and run the following command:
```bash
pip install -r requirements.txt
```

This will install all the required dependencies for the project.

# Running the project
Navigate to the root directory of the project and run the following command:
```bash
python manage.py makemigrations
python manage.py migrate
```

This will create the database and all the required tables.

Create a superuser by running the following command:
```bash
python manage.py createsuperuser
```

To run the project, run the following command:
```bash
python manage.py runserver
```

This will start the server on port 8000. To access the project, navigate to http://localhost:8000/ in your browser.

---