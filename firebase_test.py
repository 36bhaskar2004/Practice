#this is old configuration technique
import pyrebase
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

firebase_ = pyrebase.initialize_app(Config)

#from firebase import firebase
#this is new technique
#from firebase import firebase
#firebase = firebase.FirebaseApplication('https://my-first-flask-app-8519a-default-rtdb.firebaseio.com/', None)

db = firebase_.database()

data={
    "name": "Bhaskar",
    "email": "@bhaskar",
    "phone": 123456
}

#db.set(data)

#db.push(data)

#db.child("first child").set(data)

#db.child("first child").push(data)

#db.child("First child").child("Child of child").child("child of c").set(data)

"""db.update({
    "address": "Kolhapur"
})"""

data1 = db.get()

for i in data1.each():
    print(i.key())
    print(i.val())
