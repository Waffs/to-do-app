from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import requests
from flask_apscheduler import APScheduler
from datetime import datetime, timedelta
from models import Todo


app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.abspath('instance/db.sqlite3')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Scheduler for reminders
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


# Base URL for the API
API_BASE_URL = "https://virtserver.swaggerhub.com/4HM5AAD/Todo_App/1.0.0"

# Home route: Fetch all todos
@app.route('/')
def index():
    # Fetch all Todos
    response = requests.get(f"{API_BASE_URL}/todos")

    # Debug log for API response
    print(f"API response: {response.status_code}, {response.json()}")

    todos = response.json() if response.status_code == 200 else []
    return render_template('index.html', todos=todos)

# Add a new todo
@app.route('/add', methods=['GET', 'POST'])
def add_todo():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        completed = request.form.get('completed') == 'on'

        # Debug log to confirm form data
        print(f"Form data: {title}, {description}, {completed}")

        # Send data to API
        data = {
            "title": title,
            "description": description,
            "completed": completed
        }
        response = requests.post(f"{API_BASE_URL}/todos", json=data)

        # Debug log for API response
        print(f"API response: {response.status_code}, {response.json()}")

        if response.status_code == 201:
            return redirect(url_for('index'))
        else:
            return f"Error: {response.json()}", 400

    return render_template('add_todo.html')

# Edit an existing todo
@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    # Fetch the Todo
    response = requests.get(f"{API_BASE_URL}/todos/{todo_id}")
    if response.status_code != 200:
        return f"Error: Todo not found.", 404
    todo = response.json()

    if request.method == 'POST':
        # Collect updated data
        updated_data = {
            "title": request.form['title'],
            "description": request.form['description'],
            "completed": request.form.get('completed') == 'on'
        }

        # Debug log for updated data
        print(f"Updated data: {updated_data}")

        # Send update to API
        response = requests.put(f"{API_BASE_URL}/todos/{todo_id}", json=updated_data)

        # Debug log for API response
        print(f"API response: {response.status_code}, {response.json()}")

        if response.status_code == 200:
            return redirect(url_for('index'))
        else:
            return f"Error: {response.json()}", 400

    return render_template('edit_todo.html', todo=todo)

# Delete a todo
@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    # Send DELETE request to API
    response = requests.delete(f"{API_BASE_URL}/todos/{todo_id}")

    # Debug log for API response
    print(f"API response: {response.status_code}")

    if response.status_code == 204:
        return redirect(url_for('index'))
    else:
        return f"Error: Unable to delete todo.", 400

# Reminder functionality
def send_reminders():
    now = datetime.now()
    todos = Todo.query.filter(
        Todo.due_date <= now + timedelta(minutes=10),
        Todo.due_date >= now,
        Todo.reminder_sent == False
    ).all()

    for todo in todos:
        print(f"Reminder: '{todo.title}' is due at {todo.due_date}")
        todo.reminder_sent = True  # Mark reminder as sent
        db.session.commit()

# Add a job to check reminders every minute
scheduler.add_job(id='send_reminders', func=send_reminders, trigger='interval', minutes=1)


# Run the Flask app
if __name__ == '__main__':
    app.run()
