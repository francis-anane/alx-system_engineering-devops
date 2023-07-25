#!/usr/bin/python3
"""This scripts exports the todo list information of all employees to a
json file format.
"""

import json
import requests
import sys


if __name__ == "__main__":

    # api server
    api_url = "https://jsonplaceholder.typicode.com/"

    # Get users
    users = requests.get(f"{api_url}users").json()

    with open("todo_all_employees.json", "w") as a_file:
        # dump the data with dictionary and list comprehension
        json.dump({user.get("id"): [
            {"task": todo.get("title"), "completed": todo.get("completed"),
             "username": user.get("username")}
            for todo in requests.get(f"{api_url}todos",
                                     params={"userId": user.get("id")})
            .json()] for user in users}, a_file)
