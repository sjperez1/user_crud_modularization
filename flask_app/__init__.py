from flask import Flask
app = Flask(__name__)
# If we were using session in users,py, we would add the following line here
# app.secret_key = "shhhhhh"