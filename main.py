from flask import render_template, redirect, url_for, request, Flask
import json

app = Flask(__name__, template_folder="templates")

cards_number = 0


def save(front:str, back:str):

    with open("data.json", "r") as data_file:
        data = json.load(data_file)
    
    data[front] = back
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    return True


@app.route("/", methods=["GET", "POST"])
def home_page():

    global cards_number
    
    front = ""
    back = ""

    if request.method == "POST":

        front_card = request.form.get("front")
        back_card = request.form.get("back")

        if front_card and back_card:
            save(front=front_card, back=back_card)
        # else:
        #     return redirect(url_for("empty_input"))

        if "add" in request.form:
            cards_number += 1

        elif "finish" in request.form:
            return redirect(url_for("flashcards"))

    return render_template("index.html", cards_number=cards_number, front=front, back=back)

@app.route("/Flashcards")
def flashcards():
    if request.method == "POST":
        pass
    
    return render_template("flashcards.html")

@app.route("/Error")
def empty_input():
    return '<h2 style="color: red;">Missed Input</h2>'

if __name__ == "__main__":
    app.run(debug=True)
