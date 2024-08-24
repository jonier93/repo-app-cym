from database.db import *
from flask import render_template, request
from controller.s3_administrator import connection_s3, save_file, upload_file

def func_home_page():
    return render_template("home.html")

def func_register_page():
    return render_template("register.html")

def func_consult_page():
    return render_template("consult.html")

def func_register_user():
    data_user = request.form
    data_file = request.files
    ident, name, lastname, birthday = data_user["id"], data_user["name"], data_user["lastname"], data_user["birthday"]
    photo = data_file["photo"]
    add_user(ident, name, lastname, birthday)
    session_s3 = connection_s3()
    photo_path = save_file(ident, photo)  
    upload_file(session_s3, photo, photo_path, ident)
    return "<h1> User was added </h1>"  

def func_consult_user():
    req_data = request.get_json()
    ident = req_data["id"]
    result_data = consult_user(ident)
    if result_data != False:
        if len(result_data) != 0:
            response_data = {
                "status":"ok",
                "name": result_data[0][1],
                "lastname": result_data[0][2],
                "birtday": result_data[0][3]
            }
        else:
            response_data = {
                "status":"error"
            }
    else:
        response_data = {
            "status":"error"
        }
    return response_data