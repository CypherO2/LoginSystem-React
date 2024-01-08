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


# app (see Line 10) with condition route @ "/staff", & method == "GET" ( Decoration of JSON - decribe a function '@' )
@app.route("/me", methods=["GET"])

# declare function to return JSON to client
def get_me():
    return jsonify(MyJson)


# if name == main ( proper industry practice )
if __name__ == "__main__":
    # app ( see Line 10 ) . run (0 variables)
    app.run()
