# Secure-Coding-Review
Choose a programming language and application. Review the code for security vulnerabilities and provide recommendations for secure coding practices. Use tools like static code analyzers or manual code review.
# README.md

# Secure Coding Review - Flask Login Example

## Description

This project demonstrates a secure coding review exercise as part of a cybersecurity internship. The goal is to review a Flask web application for security vulnerabilities, identify issues, and apply secure coding best practices.

## Vulnerabilities Found

- SQL Injection vulnerability due to unsafe string formatting
- Storing plaintext passwords without hashing
- Debug mode enabled in production
- No session management
- No rate limiting or brute-force protection

## Fixed Code Improvements

- Used parameterized queries to prevent SQL injection
- Passwords hashed securely using bcrypt
- Debug mode disabled
- Session management implemented
- Code ready for further enhancement (rate limiting, CSRF, input validation)

## Tools Used

- Python
- Flask
- SQLite
- Bandit (static code analyzer)
- bcrypt (password hashing)

## How to Run

1. Install dependencies:

```bash
pip install flask bcrypt bandit
```

2. Initialize the database (example):

```bash
sqlite3 users.db "CREATE TABLE users (username TEXT, password TEXT);"
```

3. Run the fixed code:

```bash
python fixed_code.py
```

4. Run Bandit to analyze code:

```bash
bandit -r .
```

## Educational Purpose Only

This project is for learning and educational purposes only.
