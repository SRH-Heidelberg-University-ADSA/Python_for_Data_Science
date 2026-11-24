import requests  # need pip install beofre

url = "https://api.example.com/weather?weather=Berlin"
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(response.status_code)
data = response.json()
print(data)
