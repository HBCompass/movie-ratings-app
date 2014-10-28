from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from datetime import datetime
from flask import Flask, render_template, redirect, request, flash
from flask import session as session
import judgement
import model
from model import session as dbsession

def get_user_from_db(id):
    return dbsession.query(model.User).filter_by(id=id).first()

def get_users_ratings(id):
    pass

def get_user_by_email(email): 
    #email should be unique 
    return dbsession.query(model.User).filter_by(id="email").first()

def check_login(email, password):
    #when a user a logs in: 
    #query the database for that email 
        #user_record = get_user_by_email
    #check if email and password match
        #if user_record.password == password:
            #set sesion["logged-in"] = True
            #set session["user_id"]= user_record.id
            #return true
        #else 
            #return false
    pass