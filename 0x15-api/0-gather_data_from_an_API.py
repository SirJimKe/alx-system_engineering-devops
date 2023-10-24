#!/usr/bin/python3
"""A script that fetch employee todo list progress"""
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)

    user_res = requests.get(user_url)
    response = requests.get(todo_url)

    users = user_res.json()
    todos = response.json(strict=False)

    employee_name = users.get('name')

    tasks = list(filter(lambda x: x.get('userId') == employee_id, todos))
    completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
    total_tasks = len(tasks)
    completed_tasks_count = len(completed_tasks)

    print("Employee {} is done with tasks ({}/{}):".format(
        employee_name, completed_tasks_count, total_tasks))

    for task in completed_tasks:
        print("\t{}".format(task['title']))
