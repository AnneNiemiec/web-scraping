# import necessary libraries
from flask import Flask, render_template, redirect
import PyMongo

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def echo():

    text1 = "Hello, World!"

    return render_template("index.html", text=text1, text2="Second Text")


if __name__ == "__main__":
    app.run(debug=True)