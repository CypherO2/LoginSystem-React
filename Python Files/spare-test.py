import sqlite3
import json
from sqlite3 import Error

# Connect to the database
conn = sqlite3.connect("CustomerStaffLogin.db")
cu = conn.cursor()

# Execute the query to select the name of the user
cu.execute("SELECT name FROM users WHERE Username = ?")
user_name = cu.fetchone()[0]

# Close the connection to the database
conn.close()

# Create a dictionary to hold the user's name
user_data = {"name": user_name}

# Convert the dictionary to JSON
json_data = json.dumps(user_data)

# Write the JSON data to a file
with open("user_name.json", "w") as file:
    file.write(json_data)
