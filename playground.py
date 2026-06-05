import flask
from flask import request, url_for
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
#from meineBib import *

app = flask.Flask(__name__)

#app.config["DEBUG"] = True

#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///meineDatenbank.db"

#db.init_app(app)


@app.route("/")
def index():



    return render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True)


