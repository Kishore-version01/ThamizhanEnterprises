from flask import Flask, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_login import UserMixin 
import os


app = Flask(__name__)
app.secret_key = os.getenv("SUPA_KEY")

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route("/home")
@login_required
def home():
    return "Welcome!"

@app.route("/")
def logout():
    logout_user()
    return "Logged out"
