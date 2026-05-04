import flask
from flask import request
from flask import render_template
from flask import redirect
import flask_sqlalchemy
from meineBib import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///meineDatenbank.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = flask_sqlalchemy.SQLAlchemy(app)


    #class StudentModel(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #name = db.Column(db.String(100), nullable=False)





#student1Studium = Studium("Cybersecurity", 3)

#erstesSemester = Semester(semester_nummer=1, module= ["Einführung in die Informatik", "Programmierung mit Python",
#Objektorientierte Programmierung", "Theoretische Informatik", "Algorithmen und Datenstrukturen"])
#zweitesSemester = Semester(semester_nummer=2, module=["Datenbanken und Informationssysteme",
#"Datenbanken und Informationssysteme", "Betriebssysteme", "Verteilte Systeme", "Mobile App Entwicklung"])


first_semester_module_introduction = Module(name="Introduction into Informatic", etc=5, exam_performance=4 )
second_semester_module_object_oriented_programming = Module(name="Object Oriented Programming", etc=5, exam_performance=3 )
third_semester_module = Module(name="Theoretical Informatic", etc=5, exam_performance=3)
fourth_semester_module = Module(name="Algorithms &  Datastructures", etc=5, exam_performance=4)
fifth_semester_module = Module(name="Databases", etc=5, exam_performance=2)


student1 = Student(name="Stefan", age=25, studies="Cybersecurity")

cybersecurity_semesters = [first_semester_module_introduction, second_semester_module_object_oriented_programming,
                          third_semester_module, fourth_semester_module,
                          fifth_semester_module]


cyberSecurityStudies = Studies("Cybersecurity", cybersecurity_semesters   )




db.session.add(student1, cyberSecurityStudies, first_semester_module_introduction,
               second_semester_module_object_oriented_programming, third_semester_module,
               fourth_semester_module,
               fifth_semester_module)


db.session.commit()







@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():


    try:

        student = Student.query.filter(
            db.or_(
                Student.name == "Stefan",
            )
        ).all()

    except Exception as e:
        print(f"Fehler bei der Abfrage: {e}")
        student = None
    

    
    
    
    return render_template("dashboard.html")



if __name__ == "__main__":
    app.run(debug=True)