#!/usr/bin/python3
"""
A script that fetch employee todo list progress
and exports it to CSV
"""
import json
import requests
import sys

base_url = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    response = requests.get(base_url + "/users/" + str(employee_id))
    employee_name = response.json().get("name")

    response = requests.get(base_url + "/todos?userId=" + str(employee_id))
    tasks = response.json(strict=False)

    data = {}
    for task in tasks:
        user_id = task.get('userId')
        username = employee_name
        completed = task.get('completed')
        title = task.get('title')
        task_data = {"task": title, "completed": completed,
                     "username": username}
        data.setdefault(user_id, []).append(task_data)

    with open("{}.json".format(employee_id), "w") as f:
        json.dump(data, f)
