# 📝 SA Task Manager

A simple, responsive Flask-based task manager where you can:

- ✅ Add tasks with a due date and category  
- 📅 View all tasks with due dates and categories  
- ✔️ Mark tasks as complete  
- 🗑️ Delete tasks  

---

## 💻 Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python (Flask)  
- **Database**: MySQL  

---

## 🚀 Features

- Responsive UI with sidebar layout  
- Task category and due date support  
- Complete/delete functionality  
- Persistent storage with MySQL  

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/lakshya8839/sa-task-manager.git
cd sa-task-manager

2. Create MySQL Database
Open your MySQL CLI or GUI tool and run:
CREATE DATABASE task_manager;

USE task_manager;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    due_date DATE DEFAULT NULL,
    category VARCHAR(50) DEFAULT NULL,
    completed BOOLEAN DEFAULT 0
);

3. Install dependencies
Make sure you have Python 3 and pip installed.
pip install -r requirements.txt


4. Set up environment variables
Create a .env file in the root directory:DB_HOST=localhost
DB_USER=root
DB_PASSWORD=root
DB_NAME=task_manager
🔒 Keep this file safe and don’t share it publicly.

5. Run the Flask app
python app.py

Open your browser and visit:
http://127.0.0.1:5000


📁 Project Structure
sa-task-manager/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
├── Procfile
├── README.md
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html

