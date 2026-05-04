import flask
import flask_sqlalchemy
from sqlalchemy import create_engine, Column, Integer
from flask_sqlalchemy import SQLAlchemy
from app import db



#Benötigte Funktionen
#Prüfungsleistungen ausgeben
# Prüfungsleistung ändern
# Prüfungsleistungswecker
#Überwachung dass Du Dein Studium in 3 Jahren abschließen möchtest
#Überwachung, dass der aktuelle Notendurchschnitt besser ist als 3.0
# Semester und Fachsemesteranzahl berechnen

#Prüfungsleistungen



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
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.studies = Studies()

class Student(db.Model):
    def __init__(self, name, age, studies):
        self.name = name
        self.age = age
        self.studies = studies





class Studies(db.Model):
    def __init__(self, studies=None, semesters=None):

        self.studies = studies
        self.semesters = []



class Semester(db.Model):
    def __init__(self, semester_nummer, semester_name, module):
        self.semester_nummer = semester_nummer
        self.pruefungsleistungen = []
        self.module = []




class Module(db.Model):
    def __init__(self, name, etc, exam_performance):
        self.name = name
        self.etc = etc
        self.exam_perfromance = exam_performance




class Pruefungsleistung(db.Model):
    def __init__(self, modul, note):
        self.modul = modul
        self.note = note

    def pruefungsleistung_ausgeben(self):
        

        return f"Modul: {self.modul}, Note: {self.note}"
    




  