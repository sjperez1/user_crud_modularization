from flask import Flask
app = Flask(__name__)
# If we were using session in users,py, we would add the following line here
# app.secret_key = "shhhhhh"

# The following allows easy changing of database name throughout our files
DATABASE = 'users_schema'