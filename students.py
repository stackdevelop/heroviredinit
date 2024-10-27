from flask import Flask, request, jsonify

# Creating a server
app = Flask(__name__)

# Adding an 'id' field for each student
students = [
    {"id": 1, "name": "Rahul", "feedback": 4},
    {"id": 2, "name": "Rohit", "feedback": 3},
    {"id": 3, "name": "Rohan", "feedback": 2}
]

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Adding a student
@app.route('/addStudent', methods=['POST'])
def addStudent():
    student = request.json
    students.append(student)
    return jsonify(students)

@app.route('/updateStudent', methods=['PUT'])
def updateStudent():
    studentInput = request.json
    for student in students:
        if student["name"] == studentInput["name"]:
            student["feedback"] = studentInput["feedback"]
            break
    else:
        students.append(studentInput)
    return jsonify(students)

@app.route('/deleteStudent/<int:id>', methods=['DELETE'])
def deleteStudent(id):
    global students
    students = [student for student in students if student["id"] != id]
    return jsonify(students)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
