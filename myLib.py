import flask
import flask_sqlalchemy
#from flask_wtf import FlaskForm
from sqlalchemy import create_engine, Column, Integer
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#from app import db

#db.init_app(app)

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

    #Die Attribute von __init__ sind Variabeln, die übergeben werden können an das Objekt von Dashboard
    #  __init__ wird hier genutzt
    def __init__(self, student):

        self.current_student = student
        self.studies = Studies.query.filter_by(student_id=self.current_student.id).first()

        self.semesters = Semester.query.filter_by(study_id=self.studies.id).all()

        self.exam_score_alarm_triggered = False

        last_semester = self.semesters[0]

        if self.current_student is None:
            return

        #Aktuelles Semester herausfinden
        for semester in self.semesters:

            if semester.semester_number > last_semester.semester_number:
                last_semester = semester

        self.current_semester = last_semester

        self.modules = []

        for semester in self.semesters:
            modules = Module.query.filter_by(semester_id=semester.id).all()
            self.modules.extend(modules)

        #Nach Modulen im aktuellen Semester filtern

        self.modules_of_current_semester = Module.query.filter_by(semester_id=self.current_semester.id).all()

        self.exam_scores_of_current_semester = []



        for module in self.modules_of_current_semester:
            current_exam_scores = ExamScore.query.filter(
                ExamScore.module_id == module.id,
                #Auschließung von Prüfungen die noch nicht geschrieben wurden
                ExamScore.score.is_not(None)
            ).all()


        self.all_exam_scores = []


        for module in self.modules:

            exam_scores = ExamScore.query.filter_by(module_id=module.id).all()

            for exam_score in exam_scores:
                self.all_exam_scores.append(exam_score.score)


            #self.all_exam_scores.extend(exam_score.score)

        #Anzahl aller Hochsschulsemester
        self.total_university_semesters = None


        #self.exam_scores_of_current_module = ExamScore.query.filter_by(module_id=self.curr.id).all()
        self.sum_exam_scores = None
        self.exam_score_goal_alarm = None


        #Variabeln für StudyDurationAlarm

        self.study_duration_alarm_triggered = False
        self.required_modules_per_month = None

        self.current_month_of_studying = self.studies.current_month_of_studying

        passed_modules = [module for module in self.modules if module.passed]
        self.current_amount_of_passed_modules = len(passed_modules)

        self.duration_goal_of_studying_in_months = 36



    def exam_score_alarm(self):


        print("Modules: ", self.modules)

        """  #Nach Semestern filtern
        semesters = Semester.query.filter_by(study_id=3).all()

        self.semesters = Semester.query.order_by(
            Semester.semester_number.desc()).first()

        #Nach Modulen filtern
        for semester in semesters:

            modules = Module.query.filter_by(semester_id=semester.id).all()

            self.modules.extend(modules)
        """


        #Nach Modulen im aktuellen Semester filtern
        #for module in self.modules:


        #Filtern nach allen ExamScores

        """
        for module in self.modules:
            exam_score_of_current_module = ExamScore.query.filter_by(module_id=module.id).all()

            for exam_score in exam_score_of_current_module:
                self.all_exam_scores.append(exam_score.score)

        """

        if not self.all_exam_scores:
            self.mean_of_all_exam_scores = None
            self.exam_score_alarm_triggered = False
            return

        self.mean_of_all_exam_scores = int(sum(self.all_exam_scores) / len(self.all_exam_scores))


        print("Durchschnitt der ExamScores: ", self.mean_of_all_exam_scores)



        if self.mean_of_all_exam_scores < 50:
            self.exam_score_alarm_triggered = True

    def study_duration_alarm(self):


        #Anzahl der Semester pro Modul

        #Anzahl der Module aufzählen, die bestanden wurden

        #Anzahl der Module des Studiengangs berechnen



        all_modules_of_studys = 0


        for semester in self.semesters:
            all_modules_of_studys += semester.modules_count

        print("All Modules of Studys: ", all_modules_of_studys)

        """
        current_month_of_studying = 24

        current_amount_of_passed_modules = 3

        duration_goal_of_studying_in_months = 36

        """

        # Formeln berechnen
        #Den Fortschritt den man haben sollte, um sein Studiendauerziel zu erfüllen
        expected_progress = self.current_month_of_studying / self.duration_goal_of_studying_in_months

        #Anzahl der bestanden Module, die man bräuchte, um sein Studiendauerziel zu erreichen
        expected_passed_exams = all_modules_of_studys * expected_progress


        #Langsamer als erwartet, um sein Ziel zu erreichen
        if self.current_amount_of_passed_modules < expected_passed_exams:
            #self.study_duration_alarm = True
            print("Du bist zu langsam")


            #Berechnen der Anzahl der Module, die man pro Monat bearbeiten sollte, um
            # sein Studiendauerziel noch zu erreichen

            #Berechnen der Anzahl der Module, die noch nicht bestanden wurden
            modules_to_work_on = all_modules_of_studys - self.current_amount_of_passed_modules

            #Berechnen der Anzahl der Monate, die übrig bleiben,bevor die Wunschstudiendauerzeit überschritten wurde

            months_left_for_studying = self.duration_goal_of_studying_in_months - self.current_month_of_studying


            #Die eigentliche Berechnung der Modulanzahl, die man pro Monat absolvieren muss

            self.required_modules_per_month = round(modules_to_work_on / months_left_for_studying, 1)


            print(f"Sie müssen {self.required_modules_per_month} Module pro Monat bearbeiten, damit sie "
                  f"ihre gewünschte Studiendauer erreichen können ")



        elif current_amount_of_passed_modules > expected_passed_exams:
            self.study_duration_alarm = False


            print("Du bist zeitlich gut dran. Weiter so")


        #not_passed_modules = Module.query.filter_by(passed=False).all()

        #examed_modules_of_current_semester = Semester.query.filter_by("Exa")

        #self.modules_of_current_semester

        #number_of_semesters = len(self.semesters)
        #print("Number of semesters: ", number_of_semesters)

        #for semester in self.semesters:


        """
            if self.semesters.extra_semesters > 0:
            self.exam_score_alarm_triggered = True

        """



class Student(db.Model):

    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable=False)
    age = db.Column(db.Integer, nullable=False)

    studies = db.relationship("Studies", back_populates="student")


class Studies(db.Model):

    __tablename__ = "studies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    current_semester = db.Column(db.Integer, nullable=False)

    #Anzahl der Semester im Studiengang
    semester_count = db.Column(db.Integer, nullable=False)

    current_amount_of_passed_modules = db.Column(db.Integer)
    current_month_of_studying = db.Column(db.Integer)

    #Stellt Verbindung zu übergeordneten Studentobjet her
    # Sie verbindet die Tabellen Studies und Students miteinander

    student_id  = db.Column(
        db.Integer,
        db.ForeignKey("student.id")
    )

    #Stellt die objektorientierte Beziehung zum Objekt Student her
    student = db.relationship("Student", back_populates="studies")

    #Ermöglicht den Zugriff auf alle Semester dieses Studiengangs
    semesters = db.relationship("Semester",back_populates="study")



class Semester(db.Model):


    __tablename__ = "semester"

    id = db.Column(db.Integer, primary_key=True)
    semester_number = db.Column(db.Integer, nullable=False)

    #Anzahl der Hochschulsemester per Fachsemester
    semesters_per_semester = db.Column(db.Integer, nullable=False)

    modules_count = db.Column(db.Integer, nullable=False)

    #Stellt Verbindung zum übergeordneten Studiesobjekt her. Sie verbindet die Tabellen Semester und Studies
    study_id = db.Column(
        db.Integer,
        db.ForeignKey("studies.id")
    )

    #Stellt die objektorientierte Beziehung zum Objekt Student her. Hier werden die Pythob-Objete Semester und
    #das entsprechende Studies-Objekt miteinander verbunden

    study = db.relationship("Studies", back_populates="semesters")

    #Ermöglicht Zugriff auf die zugehörigen Module-Objekte
    modules = db.relationship("Module", back_populates="semester")



class Module(db.Model):
    __tablename__ = "module"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    #Stellt Verbindung zum übergeordneten Semesterobjekt her
    # Sie verbindet die Tabellen Semester und Module miteinander

    semester_id = db.Column(db.Integer, db.ForeignKey("semester.id"))
    number_of_attempts = db.Column(db.Integer, nullable=False, default=3)

    #Ermöglicht Zugriff auf das Semesterobjekt
    semester = db.relationship("Semester", back_populates="modules")

    passed = db.Column(db.Boolean)

    #Zugriff auf das zugehörige ExamScore-Objekt für dieses Modul
    exam_score = db.relationship(
        "ExamScore",
        back_populates="module",
        uselist=False,

    )


class ExamScore(db.Model):

    __tablename__ = "exam_score"

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)

    #Stellt Verbindung zum übergeordneten Moduleobjekt her
    #Sie stellt die Verbindung zwischen den Tabellen ExamScore und Module her
    module_id = db.Column(db.Integer, db.ForeignKey("module.id"))

    #Stellt die objektorientierte Beziehung zum Modulobjekt her
    module = db.relationship("Module", back_populates="exam_score")

    #student_id = db.Column(db.Integer, db.ForeignKey("student"))




