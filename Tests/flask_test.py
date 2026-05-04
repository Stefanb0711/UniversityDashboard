from flask import Flask, request, render_template_string

app = Flask(__name__)

# Startseite
@app.route("/")
def home():
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Startseite</title>
        </head>
        <body>
            <h1>Flask funktioniert</h1>
            
        </body>
        </html>
    """)


if __name__ == "__main__":
    app.run(debug=True)

