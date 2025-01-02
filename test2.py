import json
import requests

url = "https://paid.pythonanywhere.com/api/validate-key/"

def check_licence_key(licence_key):
    try:
        response = requests.post(url, json={'key': licence_key})
        if response.status_code in [200, 202]:
            print("Access successfully.")
            return True
        elif response.status_code == 403:
            print("Key already in use.")
        elif response.status_code == 400:
            print("You entered the wrong key.")
        else:
            print("Please try again later.")
    except requests.exceptions.RequestException as error:
        print(f"Error connecting to the API: {error}")
    return False

def save_licence_key(licence_key):
    with open('saved_key.json', "w") as key_file:
        json.dump({'key': licence_key}, key_file)
    print("Licence key saved successfully.")

def check_existing_licence_key():
    try:
        with open('saved_key.json', 'r') as key_file:
            data = json.load(key_file)
            return data.get('key')
    except FileNotFoundError:
        return None

def run():
    licence_key = check_existing_licence_key()
    if licence_key:
        print("Licence key found.")
        if check_licence_key(licence_key):
            return
        else:
            print("The saved product key is invalid.")
    licence_key = input("Enter your key: ")
    if check_licence_key(licence_key):
        save_licence_key(licence_key)

run()