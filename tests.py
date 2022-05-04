from random import randint
import requests


def create_test():
    counts = [100]
    for i in counts:
        response = requests.post("http://127.0.0.1:8000/api/questions/", json={"questions_num": i})
        print(response.text)


def delete_test():
    counts = [randint(3, 100) for i in range(10)]
    for i in counts:
        response = requests.delete(f"http://127.0.0.1:8000/api/questions/delete/{i}")
        print(response.text)


def get_test():
    response = requests.get("http://127.0.0.1:8000/api/questions/get")
    for i in response.json():
        print(i)


def get_single_test():
    counts = [randint(3, 100) for i in range(10)]
    for i in counts:
        response = requests.get(f"http://127.0.0.1:8000/api/questions/get/{i}")
        print(response.json())

create_test()
print(" ")