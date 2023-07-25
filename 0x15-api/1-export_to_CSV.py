#!/usr/bin/python3
"""This scripts exports the todo list information of a user by a given id
in csv file format.
"""

import csv
import requests
import sys


if __name__ == "__main__":

    # api server
    api_url = "https://jsonplaceholder.typicode.com/"

    # Get user by id through the api service in a json format
    user_id = requests.get(f"{api_url}users/{sys.argv[1]}").json()
    # Get the todo list of user by id parameter through api
    user_todo = requests.get(f"{api_url}todos",
                             params={"userId": sys.argv[1]}).json()

    name = user_id.get('username')
    tasks = []

    with open(f"{sys.argv[1]}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in user_todo:
            tasks.append([sys.argv[1], name, task.get('completed'), task.get(
                "title")])
        for row in tasks:
            writer.writerow(row)
