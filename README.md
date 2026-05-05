# Python and Django Learning Projects

A collection of hands-on projects built throughout my journey learning **Python and Django**, combining knowledge from the **ITI 9-Month Program** and the **Academind (Maximilian Schwarzmüller) course**.

This repository reflects my progression from learning fundamentals to building real-world backend applications and deploying them to production.

---

## 🌍 Live Demo

👉 https://mysite-production-d8c3.up.railway.app/

---

## Key Concepts & What I Learned

Throughout this journey, I gained practical experience in:

### 🔹 Django Fundamentals

- MVT Architecture
- Class-Based Views vs Function-Based Views
- Clean URL design using slugs

### 🔹 Database & ORM

- Relational database design
- Django ORM usage
- Query optimization (`select_related`, `prefetch_related`)

### 🔹 Backend Engineering Concepts

- Structuring scalable Django applications
- Thinking in terms of full system flow (not isolated features)
- Handling validation and edge cases

### 🔹 Authentication & Authorization

- Implementing authentication systems
- JWT-based authentication
- Managing roles using:
  - Role field approach
  - Django Groups & Permissions

### 🔹 APIs Development

- RESTful API principles
- Building APIs using Django REST Framework (DRF)

### 🔹 State Management

- Sessions & Cookies
- Implementing features like "Read Later"

### 🔹 Static & Media Handling

- Understanding static vs media files
- Handling static files in development vs production

### 🔹 Deployment & Production

- Deploying Django apps on Railway
- Using PostgreSQL in production
- Managing environment variables
- Solving real production issues:
  - CSRF errors
  - ALLOWED_HOSTS configuration
  - Static files serving with WhiteNoise

---

## Architecture Highlights

- Clear separation between **static** and **media**
- Session-based state management
- Clean and scalable URL design
- Modular app structure following Django best practices

---

## ⚠️ Challenges & Solutions

- Static files not working in production  
  → solved using **WhiteNoise**

- Database migration (SQLite → PostgreSQL)  
  → handled using `dj_database_url`

- CSRF & ALLOWED_HOSTS issues  
  → fixed via proper environment configuration

- Running commands on remote environment  
  → solved using Railway CLI & automation

---

## ✨ Featured Blog Project

- Custom UI (dark theme + glass-morphism)
- SEO-friendly routing using slugs
- Comment system
- Read Later (session-based)
- Tagging system (Many-to-Many)

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (Dev) / PostgreSQL (Production)
- **Frontend:** HTML5, CSS
- **Static Files:** WhiteNoise
- **Deployment:** Railway

---

## 🎓 Learning Journey

As part of my learning path:

### ITI (Information Technology Institute)

- [Crowdfunding (Python)](https://github.com/goudaabdulhmid2/crowdfunding)
- [BookStore (Django)](https://github.com/goudaabdulhmid2/BookStore)
- [Clinic Appointment System](https://github.com/goudaabdulhmid2/clinic_appointment_system)

### Academind (Udemy)

- [Monthly Challenges](https://github.com/goudaabdulhmid2/monthly_challenges)
- [Project 3 - BookStore](https://github.com/goudaabdulhmid2/project3-bookStore)

---

## How to Run Locally

```bash
git clone <repo-url>

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```
