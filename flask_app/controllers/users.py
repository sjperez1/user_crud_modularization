# session would be added to the end of the following line if we were using it in this file
from flask import render_template, redirect, request
from flask_app import app
# import the class from friend.py
from flask_app.models.user import User

@app.route("/")
def show_users():
    # call the get all classmethod to get all users
    users = User.get_all()
    return render_template("read_all.html", users = users)

@app.route("/user/new")
def display_create_user():
    return render_template("create.html")

@app.route("/user/new", methods = ['POST'])
def create_user():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }

    User.create(data)

    return redirect("/user/new")

@app.route("/user/<int:id>")
def show_user(id):
    data = {
        "id" : id
    }
    one_user = User.get_user(data)
    return render_template("show.html", one_user = one_user)

@app.route("/user/<int:id>/edit")
def display_edit_user(id):
    data = {
        "id" : id
    }
    one_user = User.get_user(data)
    return render_template("edit.html", one_user = one_user)

@app.route("/user/<int:id>/edit", methods=['POST'])
def edit_user(id):
    data = {
        "id" : id,
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.edit(data)
    return redirect(f"/user/{id}")

@app.route("/user/<int:id>/delete")
def delete_user(id):
    data = {
        "id" : id
    }
    User.delete(data)
    return redirect("/")