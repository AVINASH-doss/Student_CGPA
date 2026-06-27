from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/create")
def create():
    return render_template("create_student.html")



@app.route("/students", methods=["POST"])
def save_student():

    roll_no = request.form["roll_no"]
    name = request.form["name"]
    semester = request.form["semester"]
    total_subjects = int(request.form["total_subjects"])
    total_marks = int(request.form["total_marks"])

    cgpa = round((total_marks / total_subjects) / 10, 2)

    student = {
        "roll_no": roll_no,
        "name": name,
        "semester": semester,
        "total_subjects": total_subjects,
        "total_marks": total_marks,
        "cgpa": cgpa
    }

    students.append(student)

    return redirect("/students")


@app.route("/students")
def display():
    return render_template(
        "display.html",
        students=students
    )


@app.route("/delete/<roll_no>")
def delete(roll_no):

    global students

    students = [
        student for student in students
        if student["roll_no"] != roll_no
    ]

    return redirect("/students")


if __name__ == "__main__":
    app.run(debug=True)