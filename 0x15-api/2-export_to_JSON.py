#!/usr/bin/python3
"""gather data from an api"""
import json
import requests
import sys


if __name__ == '__main__':
    """run the script as main file"""
    # get the id as a param
    if len(sys.argv) != 2:
        print("usage: app user_id")
        exit(1)

    # get the id and the urls
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user_data = f"{url}/users/{user_id}"
    todo_data = f"{url}/todos?userId={user_id}"

    # request data
    req_user_data = requests.get(user_data)
    req_todo_data = requests.get(todo_data)

    # convert requested date to dict
    dict_user_data = req_user_data.json()
    dict_todo_data = req_todo_data.json()

    # get neded data from dicts
    name = dict_user_data.get("username")
    print(name)
    tasks = len(dict_todo_data)

    # open file and convert data to json format
    file_name = f"{user_id}.json"
    with open(file_name, "w") as file:
        for i in dict_todo_data:
            json.dump({
                user_id: [
                    {
                        "task": i.get("title"),
                        "completed": i.get("completed"),
                        "username": name
                    }
                ]
            }, file)
