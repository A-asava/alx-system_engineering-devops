#!/usr/bin/python3
"""Python script to export data in the
    CSV format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(url + "users/{}"
                        .format(userId)).json()
    username = user.get("username")
    todo_list = requests.get(url + "todos",
                             params={"userId": sys.argv[1]}).json()
    with open("{}.json".format(userId), "w") as jsonfile:
        json.dump({userId: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            } for task in todo_list]}, jsonfile)
