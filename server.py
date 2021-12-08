from flask import Flask,render_template
import os

from werkzeug.wrappers import request

TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')

app = Flask(__name__,template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

data = {
    "Page Header":"Jayant Manchanda"
}
@app.route("/")
def landingPage():
    return render_template("index.html",data=data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form",methods=["GET","POST"])
def form():
    print(request)
    return render_template("index.html",data={request})


if __name__ == "__main__":
    app.run(debug=True)