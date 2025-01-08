# to-do-app
This assignment is part of the requirements for backend development bootcamp in tech4dev
# Todo App

A feature-rich Todo App built with Flask and SQLAlchemy, allowing users to manage their tasks effectively with features such as due dates, priority levels, and notifications.

---

## Features

- **Create, Edit, and Delete Todos**
- **Set Due Dates** for tasks
- **Assign Priority Levels** (Low, Medium, High)
- **Reminders and Notifications** for upcoming tasks
- Responsive web interface styled with **Bootstrap**

---

## Tech Stack

- **Backend:** Flask, SQLAlchemy
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap
- **API:** Swagger-based REST API

---

## Installation and Setup

### Prerequisites
- Python 3.8+
- Pip (Python Package Manager)

### 1. Clone the Repository

git clone https://github.com/your-username/todo-app.git
cd todo-app

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Set Up the Database
To initialize the database, run:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

5. Run the Application
flask run
The app will be available at http://127.0.0.1:5000/.

API Documentation
The app provides a fully documented REST API using Swagger.

Endpoints:
GET /todos - Fetch all todos
POST /todos - Create a new todo
GET /todos/{id} - Fetch a specific todo by ID
PUT /todos/{id} - Update a specific todo
DELETE /todos/{id} - Delete a specific todo
The full API documentation is available at /api/docs when the app is running.

Configuration
Environment Variables
SQLALCHEMY_DATABASE_URI - Database connection URI
FLASK_ENV - Set to development for debugging
Add these variables in a .env file or configure them in your deployment environment.

### Deployment
#### Vercel Deployment
Push the project to a GitHub repository.
Connect your repository to Vercel.
Configure the following environment variables in Vercel:
SQLALCHEMY_DATABASE_URI
Deploy your app and access it via the Vercel-provided URL.

### Future Improvements
Add tags or categories for better task organization.
Include recurring tasks functionality.
Add collaborative features (shared tasks).
Integrate more advanced notifications (email or SMS).
Calendar Synchronization to integrate tasks with external calendars
Contributing
Contributions are welcome! Please open an issue or create a pull request with your suggestions or improvements.

License
This project is licensed under the MIT License.
