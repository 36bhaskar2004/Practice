#Flask required moduls
from flask import Flask, render_template, request,g, session, redirect
#firebase required library
import pyrebase
#firebase configuration
Config = {
  "apiKey": "AIzaSyA9gGabeep472ajAzxwaArHSqREmMngFOM",
  "authDomain": "my-first-flask-app-8519a.firebaseapp.com",
  "projectId": "my-first-flask-app-8519a",
  "storageBucket": "my-first-flask-app-8519a.firebasestorage.app",
  "messagingSenderId": "756020657220",
  "appId": "1:756020657220:web:fed6245ba9d0c500249011",
  "measurementId": "G-RNDZLQTWFR",
  "databaseURL":"https://my-first-flask-app-8519a-default-rtdb.firebaseio.com/"
};

#firebase config
firebase_ = pyrebase.initialize_app(Config)
db = firebase_.database()

#flask app decleration
app=Flask(__name__)
app.secret_key= "hiuffhhwiuf"

#main route
@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        Name = request.form
        db.child("All Data").push(Name)
        return render_template("form.html")
    return render_template("main.html")

#form route
@app.route("/form", methods=["GET","POST"])
def form():
    if request.method == "POST":
        Name = request.form
        db.child("All Data").push(Name)
        return render_template("form.html")
    return render_template("form.html")

#admin route
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if 'user' in session:
        All_data = db.child("All Data").get()
        return render_template("admin.html", data = All_data)
    return redirect("/login")

#respons route
@app.route("/response/<string:pushkey>", methods=["GET", "POST"])
def res(pushkey):
    if 'user' in session:
        res_data = dict(db.child("All Data").child(pushkey).get().val())
        return render_template("response.html", pushkey = pushkey, res_data = res_data)
    return redirect("/login")

#login route for admin
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        session.pop("user", None)
        if request.form.get("pass") == 'password' and request.form.get("uname") == "Bhaskar":
            session['user'] = request.form.get('uname')
            return redirect("/admin")
    if 'user' in session:
        return redirect("/admin")
    return render_template("login.html")

#logout form admin
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

#flask app running
if __name__ == "__main__":
    app.run(debug=True)

