from textwrap import shorten
from flask import Flask, jsonify, redirect, render_template, request

import my_util
import my_db

LOCAL_HOST_PORT = 5000
app = Flask(__name__)
myDb = my_db.sqDb("url_db.db")


@app.route("/", methods=["GET", "POST"])
def home():
    print("Inside home")
    if request.method == "GET":
        print("Hello")
        return render_template("index.html", name="Hello World")
        # return my_util.generate_shorten_url()
    elif request.method == "POST":
        input_url = request.form["input"]
        print("Input Receives", input_url)

        # Remove http or https at the start
        input_url = my_util.removeHttp(input_url)

        # Insert the url into the db.
        res = (
            "http://localhost:"
            + str(LOCAL_HOST_PORT)
            + "/"
            + myDb.insertOrReturn(input_url)
        )
        print("Shorten URL", res)

        # return render_template("index.html", shorten_url=res)
        return jsonify({"input": input_url, "shorten": res})
    else:
        print("Unexepceted Path taken")


@app.route("/<shorten_url>", methods=["GET", "POST"])
def url_redirect(shorten_url):
    print("shorten_url", shorten_url)
    result = myDb.reverse_lookup(shorten_url)
    if result == False:
        return "URL Not Found"
    return redirect("https://" + result)


if __name__ == "__main__":
    app.run()
