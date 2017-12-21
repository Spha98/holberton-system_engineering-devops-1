#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com to return information about all
employee's todo list progress
"""

import json
import requests

if __name__ == '__main__':
    users = requests.get("https://jsonplaceholder.typicode.com/users",
                         verify=False).json()
    jsonobj = {}
    for user in users:
        userId = user.get("id")
        todo = requests.get("https://jsonplaceholder.typicode.com/todos?{}={}".
                            format("userId", userId), verify=False).json()
        username = user.get('username')
        tasks = []
        for task in todo:
            task_dict = {}
            task_dict["task"] = task.get('title')
            task_dict["completed"] = task.get('completed')
            task_dict["username"] = username
            tasks.append(task_dict)
        jsonobj[userId] = tasks
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(jsonobj, jsonfile)
