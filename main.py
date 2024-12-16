from flask import render_template, redirect, url_for, request, Flask

app = Flask(__name__, template_folder="templates")
@app.route("/")
def home_page():
    if request.method == "POST":
        pass
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)