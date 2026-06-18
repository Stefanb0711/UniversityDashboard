import flask
from flask import request, url_for
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy


from meineBib import *



app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///meineDatenbank.db"

db.init_app(app)



#db = SQLAlchemy(app)

with app.app_context():
    db.create_all()


with app.app_context():
    db.create_all()

    student1 = Student(name="Max Müller", age=24)
    student2 = Student(name="Anna Schmidt", age=27)

    study1 = Studies(name="Informatik", student=student1,
                     semester_count=6, current_semester=1)
    study2 = Studies(name="Wirtschaftsinformatik", student=student2,
                     semester_count=7, current_semester=3)

    # region Semesters

    semester1 = Semester(
        semester_number=1,
        semesters_per_semester=0,
        study=study1,
        modules_count=5
    )

    semester2 = Semester(
        semester_number=2,
        semesters_per_semester=0,
        study=study1,
        modules_count=5
    )

    semester3 = Semester(
        semester_number=3,
        semesters_per_semester=0,
        study=study1,
        modules_count=5
    )

    semester4 = Semester(
        semester_number=4,
        semesters_per_semester=0,
        study=study1,
        modules_count=5
    )

    semester5 = Semester(
        semester_number=5,
        semesters_per_semester=0,
        study=study1,
        modules_count=5
    )

    semester6 = Semester(
        semester_number=6,
        semesters_per_semester=0,
        study=study1,
        modules_count=5
    )

    sem1 = Semester(
        semester_number=2,
        semesters_per_semester=0,
        study=study2,
        modules_count=6
    )

    # endregion

    # region Modules
    # ------------------------
    # Module für Semester 1
    # ------------------------

    modul1 = Module(name="Programmierung 1", semester=semester1, passed=True, number_of_attempts=1)
    modul2 = Module(name="Mathematik 1", semester=semester1, passed=True, number_of_attempts=2)
    modul3 = Module(name="Einführung Informatik", semester=semester1, passed=False, number_of_attempts=1)
    modul4 = Module(name="Datenbanken", semester=semester1, passed=True, number_of_attempts=1)
    modul5 = Module(name="Webentwicklung", semester=semester1, passed=False, number_of_attempts=3)

    # ------------------------
    # Module für Semester 2
    # ------------------------

    modul6 = Module(name="Programmierung 2", semester=semester2, passed=True, number_of_attempts=1)
    modul7 = Module(name="Mathematik 2", semester=semester2, passed=False, number_of_attempts=2)
    modul8 = Module(name="Software Engineering", semester=semester2, passed=True, number_of_attempts=1)
    modul9 = Module(name="Betriebssysteme", semester=semester2, passed=True, number_of_attempts=2)
    modul10 = Module(name="Netzwerktechnik", semester=semester2, passed=False, number_of_attempts=3)

    # ------------------------
    # Module für Semester 3
    # ------------------------

    modul11 = Module(name="Algorithmen", semester=semester3, passed=True, number_of_attempts=1)
    modul12 = Module(name="Cyber Security", semester=semester3, passed=False, number_of_attempts=2)
    modul13 = Module(name="Cloud Computing", semester=semester3, passed=True, number_of_attempts=1)
    modul14 = Module(name="Projektmanagement", semester=semester3, passed=True, number_of_attempts=1)
    modul15 = Module(name="KI Grundlagen", semester=semester3, passed=False, number_of_attempts=3)

    # ------------------------
    # Module für Semester 4
    # ------------------------

    modul16 = Module(name="Machine Learning", semester=semester4, passed=False, number_of_attempts=2)
    modul17 = Module(name="Mobile Entwicklung", semester=semester4, passed=True, number_of_attempts=1)
    modul18 = Module(name="DevOps", semester=semester4, passed=True, number_of_attempts=1)
    modul19 = Module(name="IT-Recht", semester=semester4, passed=True, number_of_attempts=2)
    modul20 = Module(name="Bachelorarbeit", semester=semester4, passed=False, number_of_attempts=1)
    # endregion

    # region Examscores

    exam_scores = [
        ExamScore(score=85, module=modul1),
        ExamScore(score=78, module=modul2),
        # modul3 hat noch keinen Score

        ExamScore(score=91, module=modul4),
        # modul5 hat noch keinen Score

        ExamScore(score=88, module=modul6),
        # modul7 hat noch keinen Score

        ExamScore(score=73, module=modul8),
        ExamScore(score=80, module=modul9),
        # modul10 hat noch keinen Score

        ExamScore(score=95, module=modul11),
        # modul12 hat noch keinen Score

        ExamScore(score=82, module=modul13),
        ExamScore(score=77, module=modul14),
        # modul15 hat noch keinen Score

        # modul16 hat noch keinen Score
        ExamScore(score=89, module=modul17),
        ExamScore(score=84, module=modul18),
        ExamScore(score=76, module=modul19),
        # modul20 hat noch keinen Score
    ]

    db.session.add_all(exam_scores)
    db.session.commit()

    # semester2 = Semester(semester=1, extra_semester=2, study=study2)

    module1 = Module(name="Programmierung 1", semester=semester1)
    module2 = Module(name="Datenbanken", semester=semester2)

    exam_score1 = ExamScore(score=85, module=module1)
    exam_score2 = ExamScore(score=92, module=module2)

    db.session.add_all([
        student1, student2,
        study1, study2,
        semester1, semester2,
        module1, module2,
        exam_score1, exam_score2
    ])

    db.session.commit()

    with app.app_context():
        current_student = Student.query.filter_by(name="Anna Schmidt").first()

        print(current_student.studies)

        current_semester = Semester.query.order_by(
            Semester.semester_number.desc()
        ).first()


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False







#class StudentModel(db.Model):
#id = db.Column(db.Integer, primary_key=True)
#name = db.Column(db.String(100), nullable=False)




#Temporärer Speicher für die FlaskApp
#create_database_entries(app)

"""
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

"""





@app.route("/")
def index():
    return redirect(url_for("dashboard"))


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    print("Dashboard wurde aufgerufen")

    student = Student.query.filter_by(name="Max Müller").first()


    my_dashboard = Dashboard(student=student
                             # , studies=current_student.studies,
                             # semesters=current_student.studies.semesters,
                             # modules=current_student.studies.semesters.modules,
                             # current_semester=current_semester
                             )

    my_dashboard.exam_score_alarm()


    my_dashboard.study_duration_alarm()

    #for semester in my_dashboard.semesters:

    #print("Number of Semesters: ", len(semester))
    #print("MyDashboardSemesters: ", my_dashboard.semesters.count())



    return render_template("dashboard.html", my_dashboard=my_dashboard,
                           semesters=my_dashboard.semesters,
                           current_semester=my_dashboard.current_semester)




@app.route("/test", methods=["GET", "POST"])
def test():

    return """
        <!DOCTYPE html>
    <html>
    <head>
        <title>Dashboard</title>
    </head>
    <h1>TEst Dashboard</h1>
    <body>
    """


if __name__ == "__main__":
    app.run(debug=True)