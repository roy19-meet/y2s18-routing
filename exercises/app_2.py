from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home_1.html")


@app.route('/student/<int:student_id>')
def display_student_id(student_id):
    return render_template(
        'student_id_1.html', student_id = student_id)



app.run(debug=True)