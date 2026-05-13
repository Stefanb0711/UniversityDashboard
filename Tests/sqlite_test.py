from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Ordner für SQLite-Datenbank
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Datenbank-Tabelle / Entity-Klasse
class Person(db.Model):

    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    eyes = db.relationship(
        "Eyes",
        backref="person",
        lazy=True
    )
class Eyes(db.Model):

    __tablename__ = "eyes"

    id = db.Column(db.Integer, primary_key = True)
    color = db.Column(db.String, nullable=False)
    shape = db.Column(db.String, nullable = False)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"),
                nullable=False)



#Hinzufügen eines Testeintrags
with app.app_context():
    db.create_all()

    #https://docs.sqlalchemy.org/en/14/orm/query.html?sqlalchemy.orm.Query.filter_by=#sqlalchemy.orm.Query.filter_by
    existing_person = Person.query.filter_by(name="Max").first()

    if not existing_person:

        person_max = Person(
            name="Max",
            age=25
        )

        eyes_of_max = Eyes(
            color="green",
            shape="round",
            person=person_max  # Beziehung direkt setzen
        )

        db.session.add(person_max)
        db.session.add(eyes_of_max)
        db.session.commit()


with app.app_context():
    for eye in Eyes.query.all():
        print(eye.id, eye.shape, eye.color)  # je nach deinen Spalten!    print(Person.query.all())

    for person in Person.query.all():
        print(person.name, person.age)



if __name__ == "__main__":
    app.run(debug=True)