import requests

data = {
    "carat": 0.25,
    "cut": "Premium",
    "color": "E",
    "clarity": "SI1",
    "depth": 61.5,
    "table": 55,
    "x": 3.95,
    "y": 3.98,
    "z": 2.43,
    "volume": 38.20
}

response = requests.post(
    "http://127.0.0.1:8000/predict",
    json=data
)

print(response.json())
