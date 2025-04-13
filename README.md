# 🏏 Cricket Scorebook Management System

A simple and interactive web-based application for managing and recording cricket scores built using Django. This project helps digitize the traditional method of scorekeeping, making it easier to manage cricket match data with a clean and user-friendly interface.

---

## 🚀 Features

- 🎯 Add Team Details
- 📊 Record and Update Match Scores (Runs, Wickets, Overs)
- 📋 View and Display Score Summaries
- 💾 Save and Manage Match Results
- 🧭 Simple Navigation and Responsive UI

---

## 🛠 Tech Stack

- **Frontend**: HTML5, CSS3, Bootstrap
- **Backend**: Python, Django
- **Database**: MySQL 
- **Tools**: Atom / VS Code, Git, GitHub

---

## 📁 Project Structure
cricket_scorebook/ │ ├── cricket_scorebook/ # Django project configuration │ └── settings.py, urls.py, wsgi.py │ ├── match/ # Main Django app │ ├── migrations/ │ ├── templates/ # HTML Templates │ ├── static/ # CSS, JS, Images │ ├── models.py │ ├── views.py │ ├── urls.py │ └── forms.py (if present) │ ├── db.sqlite3 # Database ├── manage.py # Django entry point └── README.md




---

## 🔧 How to Run the Project Locally

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/cricket-scorebook.git
cd cricket-scorebook
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
