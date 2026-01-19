#Flask required moduls
from flask import Flask, render_template, request, flash
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
    return render_template("form.html")

#admin route
@app.route("/admin", methods=["GET", "POST"])
def admin():
    All_data = db.child("All Data").get()
    return render_template("admin.html", data = All_data)

#respons route
@app.route("/response/<string:pushkey>", methods=["GET", "POST"])
def res(pushkey):
    res_data = dict(db.child("All Data").child(pushkey).get().val())
    return render_template("response.html", pushkey = pushkey, res_data = res_data)

#flask app running
if __name__ == "__main__":
    app.run(debug=True)

