import flask
import flask_sqlalchemy
from flask_wtf import FlaskForm
from sqlalchemy import create_engine, Column, Integer
from flask_sqlalchemy import SQLAlchemy
from app import db, app


#Benötigte Funktionen
#Prüfungsleistungen ausgeben
# Prüfungsleistung ändern
# Prüfungsleistungswecker
#Überwachung dass Du Dein Studium in 3 Jahren abschließen möchtest
#Überwachung, dass der aktuelle Notendurchschnitt besser ist als 3.0
# Semester und Fachsemesteranzahl berechnen

#Prüfungsleistungen




#Flask SQLAlchemy Vorteile
#




class Dashboard:

    def __init__(self):
        pass

    def exam_score_alarm(self):
        #all_modules =
        pass


    def study_duration_alarm(self):
        pass




def datei_speichern(datei_name, inhalt):
    with open(datei_name, "w") as datei:
        datei.write(inhalt)

def datei_laden(datei_name):
    with open(datei_name, "r") as datei:
        return datei.read()
    

class DashboardWidget:
    def __init__(self, name, inhalt):
        self.name = name
        self.inhalt = inhalt

    


class Student(db.Model):

    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, primary_key=True)
    age = db.Column(db.Integer, primary_key=True)

    studies = db.relationship("Studies", back_populates="student")


with app.app_context():
    pass


class Studies(db.Model):

    __tablename__ = "studies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


    #Stellt Verbindung zu übergeordneten Studentobjet her
    # Sie verbindet die Tabellen Studies und Students miteinander

    student_id  = db.Column(
        db.Integer,
        db.ForeignKey("student.id")
    )

    #Stellt die objektorientierte Beziehung zum Objekt Student her
    student = db.relationship("Student", back_populates="studies")

    semesters = db.relationship("Semester", backref="study", lazy=True)



class Semester(db.Model):




    __tablename__ = "semester"

    id = db.Column(db.Integer, primary_key=True)
    studies = db.Column(db.String, primary_key=True)

    #Stellt Verbindung zum übergeordneten Studiesobjekt her. Sie verbindet die Tabellen Semester und Studies
    study_id = db.Column(
        db.Integer,
        db.ForeignKey("studies.id")
    )

    #Stellt die objektorientierte Beziehung zum Objekt Student her. Hier werden die Pythob-Objete Semester und
    #das entsprechende Studies-Objekt miteinander verbunden

    study = db.relationship("Studies", back_populates="semester")

    module = db.relationship(db.Integer, db.ForeignKey("modul.id"), nullable=False)


class Module(db.Model):
    __tablename__ = "module"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    #Stellt Verbindung zum übergeordneten Semesterobjekt her
    # Sie verbindet die Tabellen Semester und Module miteinander

    semester_id = db.Column(db.Integer, db.ForeignKey("semester.id"))
    semester = db.relationship("Semester", back_populates="module")


    exam_score = db.relationship(
        "ExamScore",
        back_populates="module",
        uselist=False,

    )


class ExamScore(db.Model):

    __tablename__ = "exam_score"

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)

    #Stellt Verbindung zum übergeordneten Moduleobjekt her
    #Sie stellt die Verbindung zwischen den Tabellen ExamScore und Module her
    module_id = db.Column(db.Integer, db.ForeignKey("module.id"))

    #Stellt die objektorientierte Beziehung zum Modulobjekt her
    module = db.relationship(db.Integer, back_populates="exam_score")

    student_id = db.Column(db.Integer, db.ForeignKey("student"))


"""
class Student(db.Model):
    def __init__(self, name, age, studies):
        self.name = name
        self.age = age
        self.studies = studies

"""


class Studies(db.Model):
    def __init__(self, studies=None, semesters=None):

        self.studies = studies
        self.semesters = []

    def to_dict(self):
        return {
            "studies": self.studies,
            "semesters": self.semesters
        }



class Semester(db.Model):

    __tablename__ = "semester"

    id = db.Column(db.Integer, primary_key=True)
    semester_name = db.Column(db.String(100), nullable=False)

    module = db.relationship(
        "Module",
        backref="semester",
        lazy=True
    )

    def __init__(self, semester_nummer, semester_name, module):
        self.semester_nummer = semester_nummer
        self.pruefungsleistungen = []
        self.module = []




class Module(db.Model):

    __tablename__ = "module"

    id = db.Column(db.Integer, primary_key = True)

    module_name = db.Column(db.String(100), nullable=False)

    semester_id = db.Column(
        db.Integer,
        db.ForeignKey("semester.id"),
        nullable = False
    )
    def __init__(self, name, etc, exam_performance):
        self.name = name
        self.etc = etc
        self.exam_perfromance = exam_performance




class ExamScore(db.Model):

    __tablename__ = "exam_score"

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey("module.id"), nullable=False)
    module = db.relationship("Module", back_populates="exam_score")

