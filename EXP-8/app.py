from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage
students = []
next_id = 1


# -------------------------------
# HOME ROUTE (Fixes 404 error)
# -------------------------------
@app.route('/')
def home():
    return jsonify({
        "message": "Student CRUD API is running successfully!",
        "available_routes": {
            "GET all students": "/students",
            "GET single student": "/students/<id>",
            "POST create student": "/students",
            "PUT update student": "/students/<id>",
            "DELETE student": "/students/<id>"
        }
    })


# -------------------------------
# CREATE Student
# -------------------------------
@app.route('/students', methods=['POST'])
def create_student():
    global next_id

    data = request.get_json()

    if not data or not data.get('name') or not data.get('age'):
        return jsonify({"error": "Name and age are required"}), 400

    student = {
        "id": next_id,
        "name": data['name'],
        "age": data['age'],
        "course": data.get('course', "")
    }

    students.append(student)
    next_id += 1

    return jsonify(student), 201


# -------------------------------
# READ All Students
# -------------------------------
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200


# -------------------------------
# READ Single Student
# -------------------------------
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s["id"] == id), None)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student), 200


# -------------------------------
# UPDATE Student
# -------------------------------
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400
    
    student = next((s for s in students if s["id"] == id), None)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    student["name"] = data.get("name", student["name"])
    student["age"] = data.get("age", student["age"])
    student["course"] = data.get("course", student["course"])

    return jsonify(student), 200


# -------------------------------
# DELETE Student
# -------------------------------
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    student = next((s for s in students if s["id"] == id), None)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    students = [s for s in students if s["id"] != id]

    return jsonify({"message": "Student deleted successfully"}), 200


# -------------------------------
# RUN SERVER
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)