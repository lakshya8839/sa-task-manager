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
git clone https://github.com/yourusername/sa-task-manager.git
cd sa-task-manager

2. Create MySQL Database
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

pip install flask mysql-connector-python

4. Run the Flask app
python app.py

Visit http://127.0.0.1:5000 in your browser.

📁 Project Structure
sa-task-manager/
│
├── app.py
├── README.md
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html


🙌 Contributing
Contributions are welcome! Feel free to fork the repo and submit a pull request.

📃 License
This project is licensed under the MIT License.


Replace `https://github.com/yourusername/sa-task-manager.git` with your actual GitHub repo URL.

---

## ✅ Steps to Push Your Project to GitHub

### 1. Initialize Git in your folder

```bash
git init


