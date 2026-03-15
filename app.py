from flask import Flask, render_template, jsonify, request, redirect, url_for
import os
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin , current_user
from login import LoginManagerAuth
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
    return render_template("home.html")


@app.route("/api/me")
@login_required
def me():
    from login import supabase
    res = supabase.table("Employee_details").select("Full Name, Email").eq("Email", current_user.id).execute()
    if res.data:
        return jsonify({"full_name": res.data[0]["Full Name"], "email": res.data[0]["Email"]})
    return jsonify({"email": current_user.id})


#homepage
@app.route("/")
def index():
    return render_template("index.html")



#loginpage
@app.route("/login", methods=['GET', 'POST'])
def login():
    
    print("Login route accessed")
    print("Method:", request.method)

    if current_user.is_authenticated:
        print("User already logged in:", current_user.id)
        return redirect(url_for("home"))
    
    if request.method == 'POST':
        
        print("FORM DATA:", request.form)
        
        username = request.form.get('username')
        password = request.form.get('password')
        
        auth = LoginManagerAuth()
        
        if auth.authenticate(username, password):
            user = User(username)
            login_user(user, remember=True)
            print("Login successful")
            return redirect(url_for('home'))
        else:
            print("Login failed")
            return render_template("index.html", error="Invalid credentials")
        
        return render_template("index.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

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
