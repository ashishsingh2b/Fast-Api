import requests

res =requests.get("http://127.0.0.1:8000/items/")
print("Text",res.text)
print("JSON",res.json())
print("Status Code",res.status_code)