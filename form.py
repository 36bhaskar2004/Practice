from flask import Flask, render_template, request, flash, redirect,url_for

#create variable for flask app
app=Flask(__name__)
app.secret_key="hfoiufhqeuf"

#route the page
@app.route("/", methods=['GET', 'POST'])
def main():
    #Check the requests 
    if request.method == 'POST':

        #take the values from the HTML 
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        
        #open page by direct route name
        #return redirect("/sum"+"/"+num1+"/"+num2)

        #open page by route function()
        return redirect(url_for("sum", int1 = num1, int2 = num2))
    return render_template("main.html")

@app.route("/sum/<int:int1>/<int:int2>")
def sum(int1, int2):
    sum_ = int1 + int2

    #flash message
    flash(f"Sum: {sum_}")
    return render_template("form2.html")

@app.route("/form")
def start():
    return render_template('form2.html')

if __name__ == "__main__":
    app.run(debug=True)

