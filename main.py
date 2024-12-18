from flask import render_template, redirect, url_for, request, Flask
import json
import os
import time

t = time.sleep(0.30)

app = Flask(__name__, template_folder="templates")

cards_number = 0 #The number of the cards.


# Takes two inputs and adds them to data.json.
def save(front:str, back:str):
    """
    Saves a key-value pair to a JSON file.

    Args:
        front (str): The key to be added to the JSON data.
        back (str): The value to be associated with the key.

    Returns:
        bool: True if the data was successfully saved.
    """

    with open("data.json", "r") as data_file:
        data = json.load(data_file)
    
    data[front] = back
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    return True

def json_check():
    """
    Checks if a JSON file exists and loads its contents.

    If the file exists, it reads the JSON data into a dictionary.
    If the file does not exist, it returns an empty dictionary.

    Returns:
        dict: The JSON data as a dictionary, or an empty dictionary if the file does not exist.
    """

    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            stored_dict = json.load(file)
    else:
        stored_dict = {}
        
    return stored_dict

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
    return render_template("flashcards.html", data=json_check(), t=t)

@app.route("/Error")
def empty_input():
    return '<h2 style="color: red;">Missed Input</h2>'

if __name__ == "__main__":
    app.run(debug=True)
