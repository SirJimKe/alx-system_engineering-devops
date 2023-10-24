#!/usr/bin/python3
"""
A script that fetch all employee todo list progress
and exports it to json
"""
import json
import requests

base_url = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    response = requests.get(base_url + "/users/")
    users = response.json(strict=False)

    response = requests.get(base_url + "/todos")
    tasks = response.json(strict=False)

    data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("name")

        user_tasks = []

        for task in tasks:
            task_user_id = task.get('userId')
            completed = task.get('completed')
            title = task.get('title')

            if task_user_id == user_id:
                task_data = {"username": username, "task":title,
                             "completed":completed}
                user_tasks.append(task_data)

        data[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
