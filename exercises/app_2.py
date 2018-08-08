from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home_1.html")


@app.route('/student/<int:student_id>/<string:student_name>')
def display_student_id(student_id,student_name):
    return render_template(
        'student_id_1.html', student_id = student_id,student_name=student_name)



app.run(debug=True)