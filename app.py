from flask import Flask, render_template, jsonify, request, redirect, url_for
import os
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin
from login import loginManager
from stdlogin import User
app=Flask(__name__)

app.secret_key = os.getenv("SUPABASE_KEY")


login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route("/home")
@login_required
def home():
    return redirect(url_for('home'))



#homepage
@app.route("/")
def index():
    return render_template("index.html")



#loginpage
@app.route("/login", methods=['GET', 'POST'])
def login():
    print("Login route accessed")
    print("Method:", request.method)
    if request.method == 'POST':
        print("FORM DATA:", request.form)
        username = request.form.get('username')
        password = request.form.get('password')
        login_manager = loginManager()
        if login_manager.authenticate(username, password):
            user = User(username)
            login_user(user, remember=True)
            print("Login successful")
            return redirect(url_for('home'))
        else:
            print("Login failed")
            return render_template("index.html", error="Invalid credentials")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "Logged out"

#about page
@app.route("/about")
def about():
    return render_template("aboutus.html")

#data entry
@app.route("/dataentry")
def dataentry():
    return render_template("dataentry.html")


#route entry page
@app.route("/routeentry")
def routeentry():
    return render_template("newentry.html")

#delay entry
@app.route("/delayentry")
def delayentry():
    return render_template("delay.html")



#progress page
@app.route("/progress")
def progress():
    return render_template("progress.html")


#logs
@app.route("/log")
def log():
    return render_template("log.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
