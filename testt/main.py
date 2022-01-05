from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from Forms import Registration, Login
import shelve, students

app = Flask(__name__)


#  ____   ___  _   _ _____ _____ ____
# |  _ \ / _ \| | | |_   _| ____/ ___|
# | |_) | | | | | | | | | |  _| \___ \
# |  _ <| |_| | |_| | | | | |___ ___) |
# |_| \_\\___/ \___/  |_| |_____|____/


@app.route("/")
def landing():
    return render_template("landing-page.html")

@app.route("/home")
def home():
    return render_template("home-page.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    register = Registration(request.form)
    if request.method == "POST" and register.validate():
        students_dict = {}
        db = shelve.open("student.db", "c")

        try:
            students_dict = db["Students"]
        except:
            print("Error in retrieving Students from student.db")

        stud = students.students(register.name, register.username, register.email, register.password, register.confirmpass)
        students_dict[stud.get_student_id()] = stud

        db["Students"] = students_dict

        #test
        students_dict = db["Students"]
        stud = students_dict[stud.get_student_id()]
        print(stud.get_name(), stud.get_username(), "was stored")

        db.close()

        return redirect(url_for('home'))
    return render_template('register.html', form=register)


if __name__ == "__main__":
    app.run(debug=True)
