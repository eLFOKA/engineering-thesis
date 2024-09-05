import requests

def login_to_zerogpt(email, password):
    url = "https://api.zerogpt.com/api/auth/login"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "email": email,
        "password": password
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200 and response.json().get("success"):
        token = response.json()["data"]["token"]
        return token
    else:
        return None

def check_text_with_zerogpt(text, api_key):
    url = "https://api.zerogpt.com/api/detect/detectText"
    headers = {
        "ApiKey": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "text": text
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return f"Error: {response.status_code}, {response.text}"

email = input("Wprowadź swój e-mail: ")
password = input("Wprowadź swoje hasło: ")
token = login_to_zerogpt(email, password)

if token:
    print(f"Received Token: {token}")
    
    text = "Wprowadź swój tekst do analizy."
    result = check_text_with_zerogpt(text, token)
    print("Odpowiedź API:", result)
else:
    print("Login failed.")
