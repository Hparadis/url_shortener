# URL Shortener(LEARNING PROJECT)

A simple full-stack URL shortener built with:

- Frontend: HTML, CSS, JavaScript
- Backend: Flask
- Database: SQLite + SQLAlchemy

Users can:
- Paste a long URL
- Generate a short URL
- Copy the short URL
- Visit the short URL and get redirected to the original link

---

# Features

- URL shortening
- Random short code generation
- Redirect system
- SQLite database storage
- Copy-to-clipboard button
- REST API with Flask
- SQLAlchemy ORM integration

---

# Project Structure

```bash
url_shortner/
│
├── back_end/
│   ├── app.py
│   ├── requirements.txt
│   │
│   ├── routes/
│   │   └── url_shortner.py
│   │
│   ├── services/
│   │   ├── db.py
│   │   ├── database.py
│   │   └── logic.py
│   │
│   └── instance/
│
├── front_end/
│   ├── url_shortner.html
│   ├── url_shortner.css
│   └── url_shortner.js
│
└── README.md
