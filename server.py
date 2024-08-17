from flask import Flask, render_template, request
from database.db import *

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1> Hola desde Ec2 </h1>"

@app.route("/register_page")
def register_page():
    return render_template("register.html")

@app.route("/register_user", methods=["post"])
def register_user():
    data_user = request.form
    ident, name, lastname, birthday = data_user["id"], data_user["name"], data_user["lastname"], data_user["birthday"]
    add_user(ident, name, lastname, birthday)
    return "<h1> User was added </h1>"

if __name__ == "__main__":
    host = "0.0.0.0"
    port = "80"
    app.run(host, port, debug=True)   