import model
import csv

def load_users(session):
    # use u.user
   
    #loop through file:

    #open u.user
    with open("seed_data/u.user") as u:
    # read a line from u.user
        reader = csv.reader(u, delimiter="|")
        for line in reader:
            #create a new user object -> model.User()
            new_user = model.User(id=line[0], age=line[1], zipcode=line[4], gender=line[2])
            # add object to a session
            session.add(new_user)
    #end loop
    # commit ALL users from that session
    session.commit()

    #return????? nothing????? ghost noises 

def load_movies(session):
    # use u.item
    with open("seed_data/u.item") as m:
    # create reader of u.item
        reader = csv.reader(m, delimiter="|")
        for line in reader:
            print line
    # create new item -> model.Movie()
        #new_movie = model.Movie()
    # add movie to session
        #session.add(new_movie)
    # commit all movies from session
    #session.commit()

    pass

def load_ratings(session):
    # use u.data
    pass

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_movies(session)

if __name__ == "__main__":
    s= model.connect()
    main(s)
