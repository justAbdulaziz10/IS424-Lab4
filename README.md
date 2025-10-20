# Lab Assignment #4 – Django (Part 1)

## 📘 Course
**IS424 – Web Programming**  
**Instructor:** Mr. Mourad Benchikh

---

## 🧩 Project Overview

This Django project was developed as part of **Lab Assignment #4**.  
The goal is to build a small web app that calculates the **square** or **square root** of a given number based on the URL input.

It demonstrates:
- URL parameter handling using `<str:value>`
- Template rendering with context variables
- Exception handling for invalid input
- Basic CSS styling for a simple UI
- Conditional logic inside the view function

---

## ⚙️ Project Structure

```
lab4/
├── lab4/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── calc/
│   ├── __init__.py
│   ├── apps.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   └── calc/
│   │       └── result.html
│   └── static/
│       └── calc/
│           └── style.css
│
├── db.sqlite3
└── manage.py
```

---

## 🚀 Features

### Part A
- Displays the **square** of any valid number.
- Shows a default message for invalid inputs (e.g. `/calc/abc/`).
- Page styled with light blue background (`#f0f8ff`) and centered text.

### Part B
- Applies the **square root function only for even numbers**.
- For **odd numbers**, displays:
  > "Even numbers not accepted, showing the result for input 0"
- The template includes the student’s name as a third heading.

---

## 🧠 Example Outputs

| URL | Output |
|------|--------|
| `/calc/4/` | Square calculation → The square root of 4 is 2.0 |
| `/calc/3/` | Even numbers not accepted, showing the result for input 0 |
| `/calc/abc/` | Even numbers not accepted, showing the result for input 0 |

---

## 🧰 How to Run

1. **Activate your environment:**
   ```bash
   conda activate envis424
   ```
2. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
3. **Run the server:**
   ```bash
   python manage.py runserver
   ```
4. **Open in browser:**
   ```
   http://127.0.0.1:8000/calc/4/
   ```

---

## 👨‍💻 Author

**Name:** Abdulaziz Alkhlaiwe  
**Student ID:** 444101708  
**University:** King Saud University  
**Course:** IS424 – Web Programming  
**Semester:** Fall 2025  

---

## 📝 License

This project was created for academic purposes only.  
© 2025 Abdulaziz Alkhlaiwe. All rights reserved.
