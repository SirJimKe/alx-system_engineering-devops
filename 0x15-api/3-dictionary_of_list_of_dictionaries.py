#!/usr/bin/python3
"""
A script that fetch all employee todo list progress
and exports it to json
"""
import json
import requests

base_url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    response = requests.get(base_url + "/todos")
    tasks = response.json(strict=False)

    employee_tasks = {}
    for task in tasks:
        user_id = task.get("userId")
        task_data = {
            "username": task.get("title"),
            "task": task.get("title"),
            "completed": task.get("completed")
            }
        if user_id not in employee_tasks:
            employee_tasks[user_id] = []
        employee_tasks[user_id].append(task_data)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(employee_tasks, json_file)
