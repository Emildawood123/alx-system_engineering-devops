#!/usr/bin/python3=
"""gather_data_from_an_API"""
import json
import requests
if __name__ == "__main__":
    url = f'https://jsonplaceholder.typicode.com/users'
    fetch_api = requests.get(url)
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_dic = json.loads(todos.content)
    dic = json.loads(fetch_api.content)
    big_dic = {}
    small_dic = {}
    list = []
    print(len(dic))
    for i in range(0, 10):
        for todo in todos_dic:
            if todo["userId"] == i + 1:
                small_dic["username"] = dic[i]["username"]
                small_dic["task"] = todo["title"]
                small_dic["completed"] = todo["completed"]
                list.append(small_dic)
                small_dic = {}
        big_dic[str(i + 1)] = list
        list = []
    with open("todo_all_employees.json", "w") as f:
        json.dump(big_dic, f)
