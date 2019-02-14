from flask import Flask

app = Flask(__name__)

# define a welcome route
@app.route("/")
def index():
  return "Welcome!"

# define a welcome route with the student's name
@app.route("/welcome/")
def welcome(student_name):
  return "Hello {student_name}"

# define a class roster route 
app.route("/roster/")
def class_roster():
  class_roster = [("Alice","A", "Sophomore"), ("Marie","C", "Junior"), ("Jada","A", "Senior"),("Ella","A-", "Freshman"),("David","D", "Junior"), ("Alyssa","B", "Junior"),("Maya","A", Senior)]
  return (class_roster = class_roster)
