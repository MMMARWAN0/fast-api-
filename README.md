# 📘 FastAPI JSON User Management

A simple **FastAPI project** to manage users with **CRUD operations** (Create, Read, Update, Delete).
Instead of using a database, all user details are stored in a **JSON file**.

Each user has a **unique auto-generated ID**.

---

## 📂 Project Structure

```
fastapi-json-users/
│── app/
│   ├── __init__.py          # Marks this as a Python package
│   ├── main.py              # FastAPI entry point
│   ├── models.py            # Internal data models
│   ├── schemas.py           # Request & response validation schemas
│   ├── crud.py              # CRUD operations on JSON data
│   └── utils.py             # File handling helpers (read/write JSON)
│
├── data/
│   └── users.json           # JSON file where users are stored
│
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-json-users.git
cd fastapi-json-users
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the API Server

```bash
uvicorn app.main:app --reload
```

Server will run at:
👉 `http://127.0.0.1:8000`

---

## 📌 API Endpoints

### 🔹 Get All Users

```
GET /users
```

Response:

```json
[
  {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 25},
  {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 30}
]
```

### 🔹 Get User by ID

```
GET /users/{id}
```

### 🔹 Create User

```
POST /users
```

Request Body:

```json
{
  "name": "Charlie",
  "email": "charlie@example.com",
  "age": 28
}
```

### 🔹 Update User

```
PUT /users/{id}
```

Request Body (partial updates allowed):

```json
{
  "age": 29
}
```

### 🔹 Delete User

```
DELETE /users/{id}
```

---

## 📖 Interactive API Docs

FastAPI automatically generates documentation:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🛠️ Tech Stack

* [FastAPI](https://fastapi.tiangolo.com/) — Web framework
* [Uvicorn](https://www.uvicorn.org/) — ASGI server
* [Pydantic](https://docs.pydantic.dev/) — Data validation