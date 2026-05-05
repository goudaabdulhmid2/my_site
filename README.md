# Python and Django Learning Projects

A collection of hands-on projects built throughout my journey learning **Python and Django**, combining concepts from the **ITI 9-Month Program** and the **Academind (Maximilian Schwarzmüller) Udemy course**.

This repository showcases practical implementations of backend development concepts, including web application architecture, database design, Django ORM, and production deployment.

## 🎓 My Learning Journey

I am currently a trainee in the **9-Month Trainee Program at the Information Technology Institute (ITI)**, where I am learning a wide variety of software engineering technologies.

I mention ITI and Maximilian here specifically to document my journey and progress in learning **Python and Django**. Python and Django represent just one of the courses I am taking at ITI, and I supplemented this learning with Academind's Udemy course.

This blog is one of several projects I've built to apply what I've learned from these two sources:

### 1. Python & Django Course (ITI)

During the Python and Django portion of my ITI training, I worked on:

- **[Crowdfunding (Vanilla Python)](https://github.com/goudaabdulhmid2/crowdfunding)**: A console-based crowdfunding platform built entirely with vanilla Python.
- **[BookStore (Django)](https://github.com/goudaabdulhmid2/BookStore)**: A comprehensive online bookstore application.
- **[Clinic Appointment System](https://github.com/goudaabdulhmid2/clinic_appointment_system)**: _Currently in development!_

### 2. Academind by Maximilian Schwarzmüller (Udemy)

To further solidify my skills, I took the Udemy course _"Learn how to build web applications and websites with Python and the Django framework"_ by Academind. **This very blog project was built as a core part of that course's curriculum!** Other projects from this track include:

- **[Monthly Challenges](https://github.com/goudaabdulhmid2/monthly_challenges)**: An introductory Django routing and views application.
- **[Project 3 - BookStore](https://github.com/goudaabdulhmid2/project3-bookStore)**: Further exploration into Django models, admin, and querying.

---

## 🧠 Key Concepts & What I Learned

Throughout my journey learning Python and Django (via ITI and hands-on practice), I gained practical experience in:

### 🔹 Django Fundamentals

- Django MVT Architecture
- Class-Based Views vs Function-Based Views
- URL routing and clean URL design using slugs

### 🔹 Database & ORM

- Designing relational databases
- Working with Django ORM
- Query optimization using `select_related` and `prefetch_related`

### 🔹 Backend Engineering Concepts

- Building scalable application structure
- Thinking in terms of full system flow (not isolated features)
- Handling validation and edge cases

### 🔹 Authentication & Authorization

- Implementing authentication systems
- Working with JWT (JSON Web Tokens)
- Managing roles using:
  - Role field approach
  - Django Groups & Permissions

### 🔹 APIs Development

- Understanding RESTful API principles
- Building APIs using Django REST Framework (DRF)

### 🔹 State Management

- Working with Sessions & Cookies
- Implementing features like "Read Later"

### 🔹 Static & Media Files

- Understanding the difference between static and media files
- Handling static files in development vs production

### 🔹 Deployment & Production

- Deploying Django apps on Railway
- Using PostgreSQL in production
- Managing environment variables
- Solving production issues:
  - CSRF errors
  - ALLOWED_HOSTS configuration
  - Static files serving with WhiteNoise

## 🧠 Architecture Highlights

- Separation between **static** and **media** files
- Session-based state management (Read Later feature)
- Clean and scalable URL design using **slugs**
- Modular app structure following Django best practices

---

## ⚠️ Challenges & Solutions

- ❌ Static files not working in production  
  → ✅ Solved using **WhiteNoise**

- ❌ Database migration (SQLite → PostgreSQL)  
  → ✅ Configured using `dj_database_url`

- ❌ CSRF & ALLOWED_HOSTS issues  
  → ✅ Fixed via proper environment configuration

- ❌ Running commands on remote environment  
  → ✅ Used Railway CLI & automated deployment

---

## ✨ Features of this Blog

- **Premium UI/UX:** A custom, fully responsive dark theme using CSS grid and glass-morphism styling.
- **Dynamic Routing:** SEO-friendly URLs utilizing Django slug fields (`/posts/my-post-title`).
- **Interactive Comments:** Visitors can leave comments on individual posts.
- **Read Later System:** A session-based functionality allowing users to save articles to read later without needing to create an account.
- **Tagging System:** Posts are categorized via Many-to-Many relationships.
- **Production Ready:** Configured with `python-dotenv` for environment variable management and `Whitenoise` for serving static assets.

## 🛠️ Technology Stack

- **Backend:** Python 3, Django 5+
- **Database:** SQLite (Development) / PostgreSQL via `dj_database_url` (Production ready)
- **Frontend:** HTML5, Vanilla CSS (Custom Design System)
- **Static Files:** Whitenoise
- **Deployment:** Railway

## 🚀 Deployment

This project is deployed using **Railway**:

- Gunicorn as WSGI server
- WhiteNoise for static file serving
- PostgreSQL database
- Environment variables for secure configuration

---

## 🌍 Live Demo

👉 https://mysite-production-d8c3.up.railway.app/

## 🚀 How to Run Locally

1. **Clone the repository**
2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables:**
   Create a `.env` file in the root directory mirroring `.env.example`.
5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
7. **Access the application** at `http://127.0.0.1:8000/`

---

_Built with passion by Abdulhamid Gouda as part of a continuous journey in software engineering._
