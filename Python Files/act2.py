# act2
from flask import Flask, jsonify, request
from flask_cors import CORS

#
#
#
#

# app = Flask function - name as variable fed into function
app = Flask(__name__)
# Cross Origin Resourse Sharing - manually define who can send information to server
# CORS function from flask_cors : (see line 10), resource = {regex"anywhere/thing" : {(data can be sent from anywhere)}}
CORS(app, resources={r"/*": {"origins": "*"}})

MyJson = {"MyJson": {"Forename": "CJ", "Surname": "Presley", "Age": 17}}

staff = {
    "staff": [
        {"firstName": "Alex", "surname": "Bowker", "age": 22},
        {"firstName": "Nic", "surname": "Grigore", "age": 23},
        {"firstName": "Barry", "surname": "Brown", "age": 26},
        {"firstName": "Allan", "surname": "Duggan", "age": 72},
        {"firstName": "Mo", "surname": "Abdul", "age": 35},
    ]
}

pets = {
    "Breed": {
        "Cats": [
            {"Name": "Stardust", "Colour": "Orange", "Personality": "Playful"},
            {"Name": "Sally", "Colour": "Black", "Personality": "Skittish"},
            {"Name": "Gerald", "Colour": "Pink", "Personality": "Cute"},
            {"Name": "Estus", "Colour": "White", "Personality": "Shy"},
            {"Name": "Gwyn", "Colour": "Black", "Personality": "Fluffy"},
        ],
        "Dogs": [
            {"Name": "Carrie", "Colour": "White", "Personality": "Bity"},
            {"Name": "Harry", "Colour": "Pink", "Personality": "Loud"},
            {"Name": "Jerry", "Colour": "Black", "Personality": "Clingy"},
            {"Name": "Barry", "Colour": "Yellow", "Personality": "Playful"},
            {"Name": "Larry", "Colour": "Brown", "Personality": "Excited"},
        ],
        "Rabbits": [
            {"Name": "Nibbles", "Colour": "Yellow", "Personality": "Cute"},
            {"Name": "Cassiopiea", "Colour": "Red", "Personality": "Fluffy"},
            {"Name": "Orion", "Colour": "Brown", "Personality": "Adorable"},
            {"Name": "Raijin", "Colour": "White", "Personality": "Shy"},
            {"Name": "Cork", "Colour": "Black", "Personality": "World Killer"},
        ],
        "Snakes": [
            {"Name": "Sallylina", "Colour": "Yellow", "Personality": "Escapist"},
            {"Name": "Sally", "Colour": "Green", "Personality": "Clingy"},
            {"Name": "Bathasar", "Colour": "Pink", "Personality": "Regal"},
            {"Name": "Belephagor", "Colour": "White", "Personality": "Bity"},
            {
                "Name": "Balemog The Great Annihilator",
                "Colour": "Red",
                "Personality": "Lovely",
            },
        ],
    }
}

temp = []


# app (see Line 10) with condition route @ "/staff", & method == "GET" ( Decoration of JSON - decribe a function '@' )
@app.route("/pets", methods=["GET"])
# declare function to return JSON to client
def get_pets():
    name = request.args.get("name")
    responses = []
    for breed in pets["Breed"]:
        for animal in pets["Breed"][breed]:
            # print(animal)
            if name == animal["Name"]:
                responses.append(animal)

            # if pets["Breed"][el][el2]["Name"] == name:
            # return jsonify(pets["Breed"][el]["Name"])
    #     if name in names:
    #     return jsonify(names[name])
    return responses


# if name == main ( proper industry practice )
if __name__ == "__main__":
    # app ( see Line 10 ) . run (0 variables)
    app.run()
