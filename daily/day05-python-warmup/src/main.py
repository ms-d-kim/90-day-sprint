import requests

def  fetch_todo():
    """Fetch a sample todo item from a free test API."""
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    todo = fetch_todo()
    print(todo)