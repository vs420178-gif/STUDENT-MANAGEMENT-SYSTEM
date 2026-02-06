from flask import Flask, request, render_template
from database import get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add-student", methods=["POST"])
def add_student():
    data = request.json

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, course) VALUES (?, ?)",
        (data["name"], data["course"])
    )

    conn.commit()
    conn.close()

    return {
        "message": "Student added successfully",
        "student": data
    }

@app.route("/students", methods=["GET"])
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    return {
        "students": [dict(student) for student in students]
    }

if __name__ == "__main__":
    app.run(debug=True)