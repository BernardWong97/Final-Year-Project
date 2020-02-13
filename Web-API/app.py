from flask import Flask, render_template

app = Flask("__main__")


@app.route("/")
def home_page():
    return render_template("index.html", token="Test Flask + React")


app.run(debug=True)
