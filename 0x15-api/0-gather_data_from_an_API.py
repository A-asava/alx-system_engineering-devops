#!/usr/bin/python3
"""Python script that, using this REST API.
    for a given employee ID,
    returns information about his/her TODO
    list progress.
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}"
                        .format(sys.argv[1])).json()
    todo_list = requests.get(url + "todos",
                             params={"userId": sys.argv[1]}).json()
    completed = [task.get("title") for task
                 in todo_list
                 if task.get("completed")
                 is True]
    print("Employee {} is done with tasks({}/{}):".
          format(user.get("name"),
                 len(completed),
                 len(todo_list)))
    [print("\t {}".format(c)) for c in completed]
