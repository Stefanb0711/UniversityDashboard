from flask import Flask, request, redirect, url_for, render_template_string
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# SQLite-Datenbank im Projektordner
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Datenbank-Tabelle / Entity-Klasse
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


# Datenbank beim Start erstellen
with app.app_context():
    db.create_all()



#Hinzufügen eines Testeintrags





#return redirect(url_for("index"))



@app.route("/", methods=["GET", "POST"])
def home():

    print("In der Home-Route angekommen.")
    neuer_testEintrag = Test(name="erster Eintrag")
    db.session.add(neuer_testEintrag)
    db.session.commit()

    testEinträge = Test.query.all()
    print("Alle Testeinträge:")
    for eintrag in testEinträge:
        print(f"ID: {eintrag.id}, Name: {eintrag.name}")


    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>SQLAlchemy Test-App</title>
    </head>
    <body>
        <h1>Student hinzufügen</h1>

        <form method="POST">
            <input type="text" name="name" placeholder="Name" required>
            <input type="email" name="email" placeholder="E-Mail" required>
            <button type="submit">Speichern</button>
        </form>

        <hr>

        <h2>Gespeicherte Studenten</h2>

        {% if studenten %}
            <ul>
                {% for student in studenten %}
                    <li>
                        ID: {{ student.id }} |
                        Name: {{ student.name }} |
                        E-Mail: {{ student.email }}
                    </li>
                {% endfor %}
            </ul>
        {% else %}
            <p>Noch keine Einträge vorhanden.</p>
        {% endif %}
    </body>
    </html>
    """)


if __name__ == "__main__":
    app.run(debug=True)