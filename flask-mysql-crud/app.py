from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abhinav@99",
    database="student_db"
)

cursor = db.cursor(dictionary=True)

# CREATE
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    name = data.get('name')
    age = data.get('age')
    course = data.get('course')

    if not name or not age or not course:
        return jsonify({"error": "All fields required"}), 400

    query = "INSERT INTO student (name, age, course) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, course))
    db.commit()

    return jsonify({"message": "Student added successfully"})

# READ ALL
@app.route('/students', methods=['GET'])
def get_students():
    cursor.execute("SELECT * FROM student")
    return jsonify(cursor.fetchall())

# READ ONE
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    cursor.execute("SELECT * FROM student WHERE id=%s", (id,))
    result = cursor.fetchone()

    if not result:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(result)

# UPDATE
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()

    name = data.get('name')
    age = data.get('age')
    course = data.get('course')

    cursor.execute(
        "UPDATE student SET name=%s, age=%s, course=%s WHERE id=%s",
        (name, age, course, id)
    )
    db.commit()

    return jsonify({"message": "Student updated"})

# DELETE
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    cursor.execute("DELETE FROM student WHERE id=%s", (id,))
    db.commit()

    return jsonify({"message": "Student deleted"})

if __name__ == '__main__':
    app.run(debug=True)
