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
    employee_name = response.json()["name"]

    response = requests.get(base_url + "/todos?userId=" + str(employee_id))
    tasks = response.json(strict=False)

    completed_tasks = []
    for task in tasks:
        if task["completed"]:
            completed_tasks.append(task["title"])

    with open('{}.csv'.format(employee_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'.format(
                employee_id,
                employee_name,
                task.get('completed'),
                task.get('title')))
