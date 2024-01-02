#!/usr/bin/python3=
"""gather_data_from_an_API"""
import json
if __name__ == "__main__":
    import json
    import requests
    import sys
    num = int(sys.argv[1])
    url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
    fetch_api = requests.get(url)
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_dic = json.loads(todos.content)
    dic = json.loads(fetch_api.content)
    big_dic = {}
    small_dic = {}
    list = []
    for todo in todos_dic:
        if todo["userId"] == num:
            small_dic["task"] = todo["title"]
            small_dic["completed"] = todo["completed"]
            small_dic["username"] = dic["username"]
            list.append(small_dic)
            small_dic = {}
    big_dic[sys.argv[1]] = list
    with open(f'{dic["id"]}.json', "w") as f:
        json.dump(big_dic, f)
