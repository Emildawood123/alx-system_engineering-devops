#!/usr/bin/python3
"""gather_data_from_an_API"""
import json
import requests
import sys
num = int(sys.argv[1])
fetch_api = requests.get(f'https://jsonplaceholder.typicode.com/users/{num}')
todos = requests.get('https://jsonplaceholder.typicode.com/todos')
list_of_tasks = []
count = 0
todos_dic = json.loads(todos.content)
dic = json.loads(fetch_api.content)
for todo in todos_dic:
    if todo["userId"] == num:
        if todo["completed"] is True:
            list_of_tasks.append("\t{}".format(todo["title"]))
            count += 1
print("Employee {} is done with tasks({}/20):".format(dic["name"], count))
for task in list_of_tasks:
    print(task)
