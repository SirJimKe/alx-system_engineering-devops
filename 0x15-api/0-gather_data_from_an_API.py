#!/usr/bin/python3
"""A script that fetch employee todo list progress"""
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)
    user_url = "https://jsonplaceholder.typicode.com/users?id={}".format(
        employee_id)

    response = requests.get(todo_url)
    user_res = requests.get(user_url)

    todos = response.json()
    users = user_res.json()

    completed_tasks = [todo for todo in todos if todo['completed']]
    total_tasks = len(todos)
    completed_tasks_count = len(completed_tasks)
    employee_name = users[0]['name']

    print("Employee {} is done with tasks ({}/{}):".format(
        employee_name, completed_tasks_count, total_tasks))

    for task in completed_tasks:
        print("\t{}".format(task['title']))
