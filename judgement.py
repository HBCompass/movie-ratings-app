from flask import Flask, render_template, redirect, request, flash
from flask import session as session
import model
import jinja2
import api

app = Flask(__name__)

app.secret_key = '\xc1\xe2=\x1b\x8e\xdc\xfdbq\xdaKuO*}g\xfd'

@app.before_first_request
def setup_session():
    session.setdefault("logged_in", False)
    session.setdefault("user_id", None)

# @app.before_request
# def get_user():
#     if session["user_id"] is not None:
#         g.user = 

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

@app.route("/signup", methods=["POST"])
def process_signup():
    #processess signup form and redirects to ??? if successful

    #if any values are null
    #flash("please fill out all fields")
    #redirect back to /signup (GET)
    print "Request is: ", request
    print "Request form is: ", request.form

    for value in request.form.values():
        if value == "": 
            flash("Please fill out all fields.")
            return redirect("/signup")

    if api.get_user_by_email(request.form.get("email")):
        flash("Email already in use.")
        return redirect ('/signup')

    # new_user = model.User()
    # new_user.email = request.form.get("email")
    # new_user.password = request.form.get("password")
    # new_user.age = request.form.get("age")
    # new_user.gender = request.form.get("gender")
    # new_user.zipcode = request.form.get("zipcode")

    new_user = model.User()
    new_user.form_user(request.form)

    print new_user

    #insert that user into the database
    # session.add(new_user)
    # session.commit()

    #redirect to login page 
    flash('Thanks for singing up! Please login!')
    return redirect("/login")



@app.route("/login")
def login():
    # Login form 
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def process_login():
    #processess login form and redirects to ??? if successful
    #login unsuccessful:
        flash('login unsuccessful')
        return redirect("/login")
    #login successful:
        flash('login successful')
        return redirect("/userratings")



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
    movie_id=42 #placeholder
    return render_template("rate_movie.html", movie=movie_id) #figure out what to actually pass



if __name__ == "__main__":
    app.run(debug = True)

