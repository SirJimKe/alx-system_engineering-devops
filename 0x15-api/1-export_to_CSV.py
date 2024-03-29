#!/usr/bin/python3
"""
A script that fetch employee todo list progress
and exports it to CSV
"""
import csv
import requests
import sys

base_url = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    response = requests.get(base_url + "/users/" + str(employee_id))
    employee_name = response.json().get("name")

    response = requests.get(base_url + "/todos?userId=" + str(employee_id))
    tasks = response.json(strict=False)

    data = []
    for task in tasks:
        user_id = task.get('userId')
        username = employee_name
        completed = task.get('completed')
        title = task.get('title')
        row = [user_id, username, completed, title]
        data.append(row)

    with open("{}.csv".format(employee_id), "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
