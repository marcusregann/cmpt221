"""app.py: render and route to webpages"""
from flask import render_template

from db.server import app

# create a webpage based off of the html in templates/index.html
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/GUI2')
def GUI2():
    return render_template("GUI2.html")
@app.route('/GUI3')
def GUI3():
    return render_template("GUI3.html")
@app.route('/notit')
def notit():
    return render_template("notit.html")

if __name__ == "__main__":
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)

