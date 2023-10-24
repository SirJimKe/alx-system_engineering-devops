#!/usr/bin/python3
"""A script that fetch employee todo list progress"""
import requests
import sys

base_url = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    response = requests.get(base_url + "/users/" + str(employee_id))
    employee_name = response.json().get("name")

    response = requests.get(base_url + "/todos?userId=" + str(employee_id))
    tasks = response.json(strict=False)

    completed_tasks = []
    for task in tasks:
        if task.get("completed"):
            completed_tasks.append(task.get("title"))

    total_tasks = len(tasks)
    completed_tasks_count = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_tasks_count, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task))
