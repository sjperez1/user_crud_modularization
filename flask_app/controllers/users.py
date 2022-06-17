# session would be added to the end of the following line if we were using it in this file
from flask import render_template, redirect, request
from flask_app import app
# import the class from friend.py
from flask_app.models.user import User

@app.route("/")
def show_users():
    # When you get an error look at: front end, controller, model
    # controller to route
    """ call the get all classmethod to get all users by doing the variable name equals the function called: users = User.get_all(), which basically means that the variable will be equal to whatever the function is returning. Then, it would need to be placed in the render_template parentheses as something like: return render_template("read_all.html", users = users). You have to include it here too because this is what you are sending to the front end in these parentheses and you are wanting to show all of the users, which is data obtain from the query in the model, on the front end.

    OR  to make it even shorter, just put the variable name that you want to use in the html equal to the function you are calling because this will make the variable equal to whatever the function is returning.
    """
    # users = User.get_all()        No longer needed bc put next to render template.
    # The part on the left of the equals sign is used in the html.
    return render_template("read_all.html", users = User.get_all())

@app.route("/user/new")
def display_create_user():
    return render_template("create.html")

@app.route("/user/new", methods = ['POST'])
def create_user():
    # Need to put a data dictionary here with info that you need to pass into your models for a model query. Class methods like create, get_user, edit, delete.
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
    User.delete_one(data)
    return redirect("/")