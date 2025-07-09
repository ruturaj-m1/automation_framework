import requests

BASE_URL = "https://reqres.in/api"
HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": "reqres-free-v1"
}

def create_user(name, job):
    payload = {"name": name, "job": job}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
    return response

def get_user(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}", headers=HEADERS)
    return response

def update_user(user_id, name, job):
    payload = {"name": name, "job": job}
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=payload, headers=HEADERS)
    return response

def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/users/{user_id}", headers=HEADERS)
    return response
