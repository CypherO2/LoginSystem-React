import sqlite3
from sqlite3 import Error
import datetime
from datetime import datetime
import pandas as pd
import json as J
import flask as F
from flask import jsonify

# Imports ^^^^ #

Query = []
Result = []

# ~~~~~~~~~~ Functions ~~~~~~~~~~ #


# Open supplied json - parse data - return result
def jsonCheck():
    with open("query.json") as jsonFile:
        jsonDict = J.load(jsonFile)
        # print(jsonDict)
    query = ""
    for el in jsonDict:
        query += el + " "
        searchValue = ""
        temp = []
        for el2 in jsonDict[el]:
            temp.append(el2)
        searchValue += temp[0]
        query += searchValue + "."
        # print(searchValue)
        for el3 in jsonDict[el][searchValue]:
            query += el3 + " "
            # print(query)
        sortValue = ""
        for el4 in jsonDict[el][temp[1]]:
            sortValue += el4
            # print(sortValue)
        for el1 in jsonDict[el][temp[1]][sortValue]:
            query += temp[1] + " " + el1
        #     print(query)
        # print(query)
        operator = ""
        for el5 in jsonDict[el][temp[2]]:
            operator += el5
        where = ""
        for el6 in jsonDict[el][temp[2]][operator]:
            where += el6[0] + " " + operator + " " + el6[1] + " and "
        where = where[:-1].rsplit(" ", 1)[0]
        query += " " + temp[2] + " " + where
        print(query)
    QueryDB(query)


#
def QueryDB(query):
    cursor.execute(query)
    result = cursor.fetchall()
    JsonFile(result[0])


#
def JsonFile(result):
    jsonCreate = "{" + '"UserName"' + ":" + '"' + str(result[0]) + '"' + "}"
    with open("jsonResults.json", "w") as newJsonFile:
        newJsonFile.write(jsonCreate)

    with open("jsonResults.json", "r") as jsonTestFile:
        data = jsonTestFile.read()
        data = data.replace("'", '"')
        jsonTestFile.close()

    with open("jsonResults.json", "w") as jsonTestFile:
        jsonTestFile.write(data)
        jsonTestFile.close()

    with open("jsonResults.json", "r") as testFile:
        jsonDict2 = J.load(testFile)
        print(jsonDict2)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


# Code ~ Below #

# Establish Connection with Database
conn = None
try:
    conn = sqlite3.connect("CustomerStaffLogin.db")
    print("Connection Achieved")
except Error as e:
    print("An error has occured:", e)

# Create Cursor
try:
    cursor = conn.cursor()
    print("Cursor Successfully Created")
except Error as e:
    print("An error has occured:", e)

jsonCheck()
