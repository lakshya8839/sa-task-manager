from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Connect to MySQL
load_dotenv()
try:
    db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
except Error as e:
    print("Database connection error:", e)
    exit()

# Home page: Show and Add tasks
@app.route('/', methods=['GET', 'POST'])
def home():
    cursor = db.cursor(dictionary=True)

    if request.method == 'POST':
        task_name = request.form.get('task')
        due_date = request.form.get('due_date') or None
        category = request.form.get('category') or None

        if task_name:
            try:
                cursor.execute(
                    "INSERT INTO tasks (name, due_date, category) VALUES (%s, %s, %s)",
                    (task_name, due_date, category)
                )
                db.commit()
            except Error as e:
                print("Insert Error:", e)
        return redirect(url_for('home'))

    cursor.execute("SELECT * FROM tasks ORDER BY id DESC")
    tasks = cursor.fetchall()
    cursor.close()

    return render_template('index.html', tasks=tasks)

# Mark task as completed
@app.route('/complete-task/<int:id>', methods=['POST'])
def complete_task(id):
    cursor = db.cursor()
    try:
        cursor.execute("UPDATE tasks SET completed = 1 WHERE id = %s", (id,))
        db.commit()
    except Error as e:
        print("Completion Error:", e)
    cursor.close()
    return redirect(url_for('home'))

# Delete task
@app.route('/delete-task/<int:id>', methods=['POST'])
def delete_task(id):
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
        db.commit()
    except Error as e:
        print("Deletion Error:", e)
    cursor.close()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
