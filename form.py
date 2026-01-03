from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        form = request.form
        return form
    return render_template('form2.html')

if __name__ == "__main__":
    app.run(debug=True)