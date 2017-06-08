from flask import Flask, render_template, request, redirect, flash
import re

app= Flask(__name__)
app.secret_key="sosecret"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results')
def results(name, location, language, comment):
    return render_template("results.html")

@app.route('/users', methods=['POST'])
def create_users():
    print "Got Post Info"
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(request.form['name']) < 1:
        flash("Name can not be blank")
        return redirect('/')
    elif len (request.form['comment']) < 1:
        flash ("Comment can not be blank")
        return redirect ('/')
    elif len(request.form['comment']) > 120:
        flash ("Comment can not be more than 120 characters")
        return redirect('/')
    else:
        return render_template('results.html', name =name, location =location, language =language, comment=comment)

app.run(debug=True)