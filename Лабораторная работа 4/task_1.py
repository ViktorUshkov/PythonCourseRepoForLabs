# TODO решите задачу
import json


FILENAME = "input.json"


def task() -> float:
    with open(FILENAME, "r") as file:
        json_data = json.load(file)
        products = [item["score"] * item["weight"] for item in json_data]
        return round(sum(products), 3)


print(task())
