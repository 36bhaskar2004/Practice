from flask import Flask, render_template, request, redirect, url_for

app= Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "<h1>Welcome to chanel</h1>"

@app.route("/pass/<int:score>")
def pass1(score):
    return f"<h1>Your have Pass the exam</h1> Score is {score}"

@app.route("/fail/<int:score>")
def fail(score):
    return f"<h1>Your have Fail the exam</h1> Score is {score}"

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method=="GET":
        return render_template("form.html")
    else:
        math=float(request.form["math"])
        science=float(request.form["science"])
        history=float(request.form["history"])
        geography=float(request.form["geography"])
        english=float(request.form["english"])
        hindi=float(request.form["hindi"])

        avg_marks=(math + science + history + geography + english + hindi)/6
        res=""
        if avg_marks >= 40:
            res="pass1"
        else:
            res="fail"

        return redirect(url_for(res,score=int(avg_marks)))

if __name__ == "__main__":
    app.run(debug=True)