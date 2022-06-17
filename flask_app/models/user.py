from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * "
        query += "FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)

        users = []
        # Since we are doing a query and then wanting to display it on the web page, we have to make instances of each user in the table (this is done by looping through each dictionary in the list(which is equal to one row in each ) and creating an instance of a user (which is cls(user))) and then put it in something to hold it, like the users array
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    # Data is holding a dictionary of things that come from our form. The insert into in parentheses has names matching the columns in database and values names need to match the keys in the dictionaries that you are giving the values for
    def create(cls, data):
        query = "INSERT INTO users(first_name, last_name, email) "
        # The blue names are taking in the data from the data dictionary in the 
        query += "VALUES( %(first_name)s, %(last_name)s, %(email)s);"
        # create queries return the id of the user to the controller and we do not have to store it in a varible because we are not showing it back on our page right away, it is just getting stored in the database. Due to this, we just have it redirect to somewhere in our controller.
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_user(cls, data):
        query = "SELECT * "
        query += "FROM users "
        query += "WHERE id = %(id)s;"
        # Put the following in result so that the first entry can later be selected. The query, which comes back as a list of dictionaries, will be stored in a variable that I am calling result. One item in the list will be a dictionary. Use print statements to visualize.
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        # Need result[0] because result is a list of dictionaries and I want to look at the first dictionary in the result list to to get the user with that id. Found this out by printing result and refreshing page and looking at the list in my terminal.
        # This line: one_user = cls(result[0])   is creating an instance of a user. one_user is like the variable name for this user that I can use in other files that use this classmethod (such as in show.html, edit.html, and users.py when calling this funtion). cls is like saying the class name User and the result[0] in parentheses has all of the info that each user will have, as specified at the top of this file in def __init__(self, data). Use print to visualize one_user. Return the instance of the class at the end.
        # When you make a query, the database knows its a user, but these python files do not know that it is user, which is why an instance of a user still has to be made after the query.
        one_user = cls(result[0])
        print(one_user)
        return one_user

    @classmethod
    def edit(cls, data):
        query = "UPDATE users "
        query += "SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s "
        query += "WHERE id = %(id)s;" 
        return connectToMySQL(DATABASE).query_db(query, data)
        # Update queries return None, which is why the return is just the query and no addition steps after like in def get_user().

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM users "
        query += "WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
        # # Delete queries return None, which is why the return is just the query and no addition steps after like in def get_user().



"""
How to name functions based on what you doing in the database:

SELECT:
def get_all()
def get_one()

INSERT:
def create()

DELETE:
def delete_one()

UPDATE:
def update_one()
def edit_one()
"""