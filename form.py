from flask import Flask, render_template, request, flash

app=Flask(__name__)
app.secret_key="hfoiufhqeuf"

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        form = request.form
        flash("Your form submited")
        return render_template('form2.html') 
    return render_template("main.html")

@app.route("/form")
def start():
    return render_template('form2.html')

if __name__ == "__main__":
    app.run(debug=True)