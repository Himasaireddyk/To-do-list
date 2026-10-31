 
<h1 align="center">📝 Django To-Do List</h1>

<p align="center">
  A simple To-Do List web application built using Python and Django.
</p>

---

## 🚀 About the Project

This is a Django-based To-Do List application that helps users manage their daily tasks. Users can add, edit, delete, and mark tasks as completed. It also provides separate sections for pending and completed tasks.

## ✨ Features

- 🔐 **User Authentication** – Login and logout functionality.
- ➕ **Add Tasks** – Add new tasks to your list.
- 📋 **View Tasks** – Display pending and completed tasks separately.
- ✏️ **Edit Tasks** – Update existing tasks.
- ✅ **Mark as Done** – Mark pending tasks as completed.
- ↩️ **Undo Completed Tasks** – Move completed tasks back to pending.
- 🗑️ **Delete Tasks** – Remove tasks from the list.
- 🕒 **Timestamps** – Track task creation and update times.
- 📅 **Current Date** – Display the current date.
- 🔎 **Django Admin** – Manage and search tasks through the admin panel.

## 🛠️ Technologies Used

- 🐍 Python
- 🌐 Django
- 🎨 HTML
- 🧩 Bootstrap 5
- 🗄️ SQLite
- ⭐ Font Awesome

## 📂 Project Structure

```text
to_do_list/
│
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── to_do_list/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── login.html
│   │   └── edit.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── .gitignore
├── db.sqlite3
├── manage.py
└── README.md
```

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project folder**

```bash
cd to-do-list
```

**3. Create a virtual environment**

```bash
python -m venv myvenv
```

**4. Activate the virtual environment (Windows)**

```bash
myvenv\Scripts\activate
```

**5. Install the required packages**

```bash
pip install -r requirements.txt
```

**6. Apply database migrations**

```bash
python manage.py migrate
```

**7. Create a superuser (optional)**

```bash
python manage.py createsuperuser
```

**8. Run the development server**

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 🔗 Important URLs

| URL | Description |
|---|---|
| `/login/` | User Login |
| `/admin/` | Django Admin Panel |

## 👨‍💻 Author

**Himasai Reddy**

---

<p align="center">
  ⭐ Thank you for visiting my project! ⭐
</p>
