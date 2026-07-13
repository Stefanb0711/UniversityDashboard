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

    """
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

    """


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

    #study1 = Studies.query.filter_by(name="")

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