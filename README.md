# FSD-II EXP-8
# Student CRUD API - Flask

## Project Description
This is a simple REST API built using Flask that performs CRUD operations on student data.
Data is stored in-memory using a Python list.

## Technologies Used
- Python
- Flask
- Postman

## How to Run

1. Create virtual environment
2. Install Flask:
   pip install flask
3. Run:
   python app.py

Server runs on:
http://127.0.0.1:5000

## API Endpoints

POST    /students
GET     /students
GET     /students/<id>
PUT     /students/<id>
DELETE  /students/<id>

## Notes
- Data is stored in-memory only.
- Data resets when server restarts.
