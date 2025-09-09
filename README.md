# TaskManagement API  

This project is a **Task Management API** built with **Supabase** as the backend infrastructure and **FastAPI** as the framework.  
The goal is to provide a **secure and modern backend solution** that allows users to create, list, update, and delete their own tasks. 🚀  

---

## ⚙️ Technologies & Components  
- **Python 3.9+**  
- **FastAPI** → Modern, type-safe web framework  
- **Supabase** → Postgres database, Auth, Storage, Realtime features  
- **Supabase-Py** → Official Supabase client for Python  
- **Uvicorn** → ASGI server  

---

## 📝 Task Breakdown  

### 1. Supabase Configuration  
- Create a Supabase project  
- Create a `tasks` table  
- Add RLS (Row Level Security) rules  
- Configure Auth for JWT validation  

### 2. Backend Setup  
- Install `supabase-py` and `fastapi` dependencies  
- Configure Supabase connection via `.env`  
- Start FastAPI (with `Uvicorn`)  

### 3. CRUD Endpoints  
- `POST /tasks/` → Create a new task  
- `GET /tasks/` → List user-specific tasks  
- `PUT /tasks/{id}` → Update a task (e.g., mark as completed)  
- `DELETE /tasks/{id}` → Delete a task  

### 4. Authentication & Security  
- Add JWT token validation  
- Retrieve `user_id` from Supabase Auth  
- Return `403 Forbidden` on unauthorized access  

### 5. Extra Features (Optional)  
- Task categories (e.g., `work`, `personal`)  
- Deadline field (`due_date`)  
- Realtime support → live updates for tasks  
- File attachment upload (Supabase Storage)  

---

## 🎯 Goal  
With this project you will:  
- Learn how to use Supabase database and Auth module from Python,  
- Gain practice in building REST APIs with FastAPI,  
- Develop a modern Task Management API with CRUD and security mechanisms.  
