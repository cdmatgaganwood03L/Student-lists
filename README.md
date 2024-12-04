
#Student_lists

A simple web-based CRUD (Create, Read, Update, Delete) system built using the Django framework. This application allows users to manage a list of students, including adding, viewing, updating, and deleting student records.

---

## Features
- Add new students with details like name, email, and age.
- View a list of all students.
- Update student details.
- Delete students from the database.
- Responsive user interface designed with Bootstrap.

---

## Prerequisites
Before running this project, ensure you have the following installed on your system:

- Python (3.12.4)
- pip (Python package manager)
- Django (5.1.1)
- A web browser for testing
- SQLite (default database for Django)

---

## Installation and Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/cdmatgaganwood03L/Stu-list-Repo
cd Stu-list-Repo

---

### Step 2: Set Up a Virtual Environment
Create a virtual environment to isolate project dependencies:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

---

### Step 3: Install Required Packages
Install the dependencies listed in the requirements.txt file:
pip install -r requirements.txt

---

### Step 4: Configure the Project
Ensure the settings in settings.py are correctly configured, especially the database and STATICFILES_DIRS.

---

### Step 5: Apply Migrations
Run the following commands to set up the database:
python manage.py makemigrations
python manage.py migrate

---

### Step 6: Create a Superuser (Optional)
To access the Django Admin interface:
python manage.py createsuperuser

---

### Step 7: Start the Development Server
Run the Django development server:
python manage.py runserver

---

### Usage
#1. Add Students
- Navigate to the Add Student page.
- Fill out the form with student details and click Submit.

#2. View Students
- Visit the Students page to see a list of all students.

#3. Update Students
- Click the Edit button next to a student's record, update the details, and save.

#4. Delete Students
- Click the Delete button next to a student's record to remove it from the database.

---

### Technologies Used
- Django: Web framework for Python
- Bootstrap: For responsive UI design
- SQLite: Default database for Django

---

###Notes
- This project uses Django’s built-in development server, which is not suitable for production.
- For deploying the project, consider using a web server like Gunicorn or deploying it on platforms like Heroku, AWS, or Azure.

### Contributing
If you’d like to contribute to this project:
- Fork the repository.

- Create a new branch: 
git checkout -b feature-name.

- Make your changes and commit them:
 git commit -m 'Add feature'.

- Push to the branch:
 git push origin feature-name.

- Submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.


