import requests

URL = "http://127.0.0.1:8000/ask-llm"

for i in range(6):
    response = requests.get(URL)

    print(f"Request {i+1}")
    print(response.json())
    print("Headers:", response.headers.get("X-Student-ID"))
    print("----------------------")