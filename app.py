from flask import Flask, request, render_template, redirect # type: ignore
from cs50 import SQL

app = Flask(__name__)

# Connect to the database
db = SQL("sqlite:///sports.db")

# Declare the global variables to be rendered onto the index page
SPORTS = ["Basketball", "Netball", "Football", "Other"]
GENDER = ["Male", "Female"]
RESIDENCE = ["Day Scholar", "Border"]

# Global dictionary to store the residents
@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS, gender=GENDER, residence=RESIDENCE)

@app.route("/register", methods=["POST", "GET"])
def register():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    gender = request.form.get("gender")
    sport = request.form.get("sport")
    residence = request.form.get("residence")

    if not firstname or not lastname:
        return render_template("error.html", message="Name cannot be empty")
    elif gender not in GENDER:
        return render_template("error.html", message="Invalid gender!")
    elif residence not in RESIDENCE:
        return render_template("error.html", message="Invalid residence!")
    elif sport not in SPORTS:
        return render_template("error.html", message="Invalid sport!")
    return render_template("success.html", message="Registered successfull")

# insert the data into the database
    db.execute("INSERT INTO registrants(firstname, lastname, gender, sport, redidence) VALUES (?, ?, ?, ?, ?)", firstname, lastname, gender, sport, residence)

@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants ORDER BY firstname, lastname")
    return render_template("registrants.html", registrants=registrants)

   