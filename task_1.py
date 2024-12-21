import json

with open('input.json', 'r') as file:
    data = json.load(file)

    result = sum(d["score"] * d["weight"] for d in data)
    result = round(result, 3)
    print(result)

