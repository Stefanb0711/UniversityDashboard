from meineBib import *

app = flask.Flask(__name__)

app.config["DEBUG"] = True

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///meineDatenbank.db"


module_object_oriented_programming = Module(name="Object Oriented Programming", etc=5, exam_performance= )
module_discrete_mathmatics = Module(name="Discrete Mathmatics", etc=5, exam_performance=)
module_data_protection_laws = Module(name="Data Protection Laws", etc=5, exam_performance=)

exam_score_object_oriented_programming = ExamScore(module_)
exam_score_discrete_mathmatics = ExamScore(module_id=)
exam_score_data_protection_laws = ExamScore()



class Dashboard:

    def __init__(self):
        pass

    def save(self):

        students.insert(student.to_dict())


        result = students.search(StudentQuery.name == "Max")
        print(result)

    def read(self):
        pass





