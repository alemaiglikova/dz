import multiprocessing
import random
import threading
import time
import json
import requests


def download_json():
    int1 = random.randint(1, 99)
    url = f"https://jsonplaceholder.typicode.com/todos/{int1}/"
    response = requests.get(url=url)
    print(response, type(response))
    json_dict = response.json()
    print(json_dict)

    with open(f"files/new{int1}.json", "w") as json_file:
        json.dump(json_dict, json_file)


if __name__ == '__main__':

    process_list = []
    for i in range(1, 10 + 1):
        process_list.append(threading.Thread(target=download_json))

    for process in process_list:
        process.start()
    for process in process_list:
        process.join()
