#!/usr/bin/python3
"""This script uses a REST API, to return the todo list progress of a
given employee based on a specified id of
the employee given as argument to the script
"""

import requests
import sys


if __name__ == "__main__":

    api_url = "https://jsonplaceholder.typicode.com/"

    # Get user by id through the api service in a json format
    user_id = requests.get(f"{api_url}users/{sys.argv[1]}").json()
    # Get the todo list of user by id parameter through api
    user_todo = requests.get(f"{api_url}todos",
                             params={"userId": sys.argv[1]}).json()
    completed_task = []
    for task in user_todo:
        if task.get("completed") is True:
            completed_task.append(task.get("title"))

    print(f"""Employee {user_id.get('name')} is done with tasks({
    len(completed_task)}/{len(user_todo)}):""")

    for task_title in completed_task:
        print(f"\t {task_title}")
