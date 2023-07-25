#!/usr/bin/python3
"""This scripts exports the todo list information of a user by a given id
in csv file format.
"""

import json
import requests
import sys


if __name__ == "__main__":

    # api server
    api_url = "https://jsonplaceholder.typicode.com/"

    passed_id = sys.argv[1]

    # Get user by id through the api service in a json format
    user_id = requests.get(f"{api_url}users/{passed_id}").json()
    # Get the todo list of user by id parameter through api
    user_todo = requests.get(f"{api_url}todos",
                             params={"userId": passed_id}).json()

    name = user_id.get('username')
    tasks = {str(passed_id): []}

    with open(f"{passed_id}.json", "w", encoding="utf-8") as a_file:
        for task in user_todo:
            tasks[passed_id].append({"task": task.get("title"), "completed":
                                     task.get('completed'), "username": name})
        json.dump(tasks, a_file)
