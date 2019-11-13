import flask


app = falsk.Flask("__main__")



@app.route("/")
def my_index():
    return flask.render_template("index.html", token="Hello")


app.run(debug=True)