# 📝 Task Flow API

Task Flow is a task management RESTful API built with Django and Django REST Framework. This project allows users to register, authenticate, and manage tasks with support for filtering by completion status, priority, and due dates.

---

## 🚀 Features

- 🔐 JWT-based authentication (access & refresh tokens)
- 👤 User registration and login
- ✅ Create, read, update, delete tasks (CRUD)
- 🔎 Filter tasks by:
  - Completion status
  - Priority level (low, medium, high)
  - Due date range
- 📄 Pagination for task listings
🔐 **Security**: users can only access and manage **their own tasks**. No one can view or edit tasks they do not own.
- 📄 API documentation with Swagger (drf-spectacular)

---

## 📦 Endpoints Overview

### 🔁 Tasks
| Method | Endpoint           | Description                   | Auth Required |
|--------|--------------------|-------------------------------|---------------|
| GET    | `/tasks/`          | List all tasks (with filters) | ✅ Yes        |
| POST   | `/tasks/`          | Create a new task             | ✅ Yes        |
| GET    | `/tasks/{id}/`     | Retrieve a single task        | ✅ Yes        |
| PUT    | `/tasks/{id}/`     | Update entire task            | ✅ Yes        |
| PATCH  | `/tasks/{id}/`     | Partially update task         | ✅ Yes        |
| DELETE | `/tasks/{id}/`     | Delete a task                 | ✅ Yes        |

> 🧭 **Filters supported on `/tasks/`:**  
> `?completed=true&priority=high&due_date_min=2024-06-01&due_date_max=2024-07-01`

> 📚 **Pagination supported using query params:**  
> `?page=2`

> Default page size: **5 tasks per page**

---

### 👤 Users
| Method | Endpoint                   | Description                  |
|--------|----------------------------|------------------------------|
| POST   | `/users/registration/`     | Register a new user         |
| POST   | `/users/login-token/`      | Login with email & password |
| POST   | `/users/token/refresh/`    | Refresh access token        |

---

## 🔐 Authentication

This API uses [JWT (JSON Web Tokens)](https://jwt.io/) for authentication.  
After logging in via `/users/login-token/`, include the token in the header:


---

## 🛠️ Tech Stack

- Python 3
- Django
- Django REST Framework
- PostgreSQL
- dj-database-url
- djangorestframework-simplejwt
- django-filter
- drf-spectacular (for Swagger UI)

---

### 🗃️ Database Configuration
*The app uses PostgreSQL as the primary database.*
You must define a DATABASE_URL in your environment or .env file like this:
`DATABASE_URL=postgres://<user>:<password>@<host>:<port>/<database_name>`
You can generate this automatically if using Render (If you are using Render).


>If you wish to use SQLite3 for the sake of simplicity instead of using PostgreSQL, just comment the configuration for PostqreSQL and remove the comment(Tripple Quote strings) for SQLite3 configuration in setting.py


## 💻 Running Locally


**Clone the repo**
```bash
git clone https://github.com/johnpauljpc/task_flow.git
cd task_flow
```

**Create and activate virtual environment** 
`python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate`

**Install dependencies**<br>
`pip install -r requirements.txt`

**Create and configure a .env file**<br>
`touch .env`  or `echo > .env`  if you are on windows OS.<br>*Also Add your DATABASE_URL, SECRET_KEY, and DEBUG=True*
**Run migrations**<br>
`python manage.py migrate`

**Start the development server** <br />
`python manage.py runserver`

### 📬 Contact
**GitHub:** *@johnpauljpc* <br>
**Email:** *jpcwork081@gmail.com* <br>
**X:** *@iam_johnpauljp*

>If you found this helpful, kindly give it a Star ⭐. THANKS 🤝

