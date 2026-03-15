from flask import Flask, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_login import UserMixin 
import os

class User(UserMixin):
    def __init__(self, id):
        self.id = id