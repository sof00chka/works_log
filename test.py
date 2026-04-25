from flask import Flask
from data import db_session
from data.users import User

session = db_session.create_session()
user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"
user.hashed_password = "cap"
session.add(user)