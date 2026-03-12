# 📝 Flask Task Manager (Full-Stack CRUD)

A responsive, persistent To-Do application built to demonstrate backend web development fundamentals, database management, and clean UI design.

## 🚀 Live Demo
https://flask-todo-app-mpsj.onrender.com

## 🛠️ Tech Stack
* **Backend:** Python 3.10+, Flask
* **Database:** SQLite with SQLAlchemy ORM
* **Frontend:** HTML5, Jinja2, Bootstrap 5
* **Deployment:** Render / Gunicorn

## ✨ Key Features
* **Full CRUD Lifecycle:** Users can create, view, toggle status (Done/Undo), and delete tasks.
* **Data Persistence:** Uses SQLAlchemy to interface with a relational database, ensuring data survives server restarts.
* **Dynamic UI:** Leverages Jinja2 templating for real-time data rendering and conditional CSS (strike-through logic).
* **Responsive Design:** Fully mobile-friendly layout using Bootstrap's grid system.

## 🧠 Engineering Highlights
- **ORM Integration:** Moved away from raw SQL to use SQLAlchemy, making the code more maintainable and secure against SQL injection.
- **Toggled Logic:** Implemented a single-route toggle system for task status to keep the backend API "DRY" (Don't Repeat Yourself).
- **Production Ready:** Configured with `gunicorn` and a `requirements.txt` for seamless cloud deployment.

## 🏁 How to Run Locally
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Felixo-dev/flask-todo-app.git](https://github.com/YOUR_USERNAME/flask-todo-app.git)
   cd flask-todo-app