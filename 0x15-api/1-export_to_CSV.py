#!/usr/bin/python3
""" convert data to csv file to store"""
import csv
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
    name = dict_user_data.get("name")
    tasks = len(dict_todo_data)

    # list the output as csv
    list_data = []
    for i in range(len(dict_todo_data)):
        row_data = [
            f'{dict_todo_data[i].get("userId")}',
            f'{name}',
            f'{dict_todo_data[i].get("completed")}',
            f'{dict_todo_data[i].get("title")}'
        ]
        
        list_data.append(row_data)

    # write data in csv file
    file_name = f"{user_id}.csv"

    with open(file_name, "w", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(list_data[0:])
