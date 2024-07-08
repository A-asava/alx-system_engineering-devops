#!/usr/bin/python3
"""Python script to export data in the
    CSV format.
"""
import csv
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
    with open("{}.csv".format(userId), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
                         [userId, username, task.get("completed"),
                          task.get("title")]
         ) for task in todo_list]
