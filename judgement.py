from flask import Flask, render_template, redirect, request
from flask import session as websession
import model
import jinja2

app = Flask(__name__)

app.secret_key = '\xc1\xe2=\x1b\x8e\xdc\xfdbq\xdaKuO*}g\xfd'



@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)

@app.route("/signup")
def sign_up():
    # Sign up form to add new user to database

    #also: need to check if input fields are valid
    #invalid entries redirect back to sign_up 
    #flash "please enter valid data for so and so"
    return render_template("sign_up.html")

# @app.route("/signup", methods=["POST"])
# def process_signup():
#     #processess signup form and redirects to ??? if successful 

#     #get values from html fields: email, password, age, gender, zip
#     new_user = model.User()
#     new_user.email = request.form.get("email")
#     new_user.password = request.form.get("password")
#     new_user.age = request.form.get("age")
#     new_user.gender = request.form.get("gender")
#     new_user.zipcode = request.form.get("zipcode")

#     print new_user
#     #create a new user for the database

#     #insert that user into the database
#     # session.add(new_user)
#     # session.commit()
#     #redirect to login page 

#     return redirect("login.html")


@app.route("/login")
def login():
    # Login form 
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def process_login():
    #processess login form and redirects to ??? if successful
    return "Post request!"



@app.route("/users")
def display_all_users():
    #users need to be clickable
    #link needs to redirect to that user's ratings
    pass

@app.route("/userratings")
def display_movie_ratings_by_user():
    # Returns user's movie ratings
    pass

@app.route("/rate")
def rate_movie():
    #when logged in, add or update rating for movie
    return render_template("rate_movie.html", movie=movie_id) #figure out what to actually pass



if __name__ == "__main__":
    app.run(debug = True)

