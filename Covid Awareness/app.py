from flask import Flask, render_template
app= Flask(__name__)


@app.route("/")
def homedef():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/myths")
def myths():
    return render_template('page2.html')

app.run(debug=True)