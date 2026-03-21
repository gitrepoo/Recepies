Register Page
<img width="1528" height="875" alt="image" src="https://github.com/user-attachments/assets/11562630-1a82-4452-99cc-852acd18f4dc" />
Login Page
<img width="1145" height="626" alt="image" src="https://github.com/user-attachments/assets/63c5b3f4-b41b-4672-a38a-10ae88802f76" />
Recepies dashboard and Search items
<img width="1907" height="908" alt="image" src="https://github.com/user-attachments/assets/6fda46f9-45d3-4cec-8df3-b218e95e4fc2" />
Sees Recepies Items and update and delete
<img width="1905" height="689" alt="image" src="https://github.com/user-attachments/assets/212a8d01-6202-4066-92a7-e4f68152a1c9" />

# 🍽️ Recipe Management System (Django)

A web-based Recipe Management System built using Django that allows users to securely manage their recipes with authentication and authorization.

---

## Features

-  User Registration & Login Authentication  
-  Create Recipes  
-  Update Recipes  
-  Delete Recipes  
-  Search Recipes  
-  Image Upload Support  
-  Export Recipes Data as CSV  
-  Secure Access Control (User-specific data)

---

## Access Control

Only authenticated users can access the system.

Each user can:
- Create their own recipes  
- Update their own recipes  
- Delete their own recipes  

Users **cannot modify or delete other users' data**, ensuring proper authorization and data security.

---

## Tech Stack

- Python  
- Django  
- Django ORM  
- SQLite  
- HTML, CSS  
- Django REST Framework (for API)

---

## Project Functionality

1. User registers on the platform  
2. User logs into the system  
3. After login, user can:
   - Add new recipes  
   - View all recipes  
   - Search recipes  
   - Update their recipes  
   - Delete their recipes  

---

## API Feature

- Export all recipes data into CSV format using a custom API endpoint.

---

## Installation

```bash

# Navigate to project folder
cd your-repo-name

# Create virtual environment
python -m venv env

# Activate environment
env\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run server
python manage.py runserver
