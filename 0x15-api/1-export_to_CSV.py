#!/usr/bin/python3
"""this for create csv file and write inside"""
import csv
import json
import sys
import requests
url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
fetch_user = requests.get(url)
file_name = f'{sys.argv[1]}.csv'
todos = requests.get('https://jsonplaceholder.typicode.com/todos')
list = []
nest_list = []
count = 0
todos_dic = json.loads(todos.content)
dic = json.loads(fetch_user.content)
for todo in todos_dic:
    if todo["userId"] == int(sys.argv[1]):
        list.append("{}".format(sys.argv[1]))
        list.append(f'{dic["name"]}')
        list.append(todo["completed"])
        list.append(todo["title"])
        nest_list.append(list)
        list = []
with open(file_name, 'w') as f:
    writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
    new_list = writer.writerows(nest_list)
