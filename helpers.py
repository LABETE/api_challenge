import requests
import os
import yaml

ACCESS_URL = "https://meta.wikimedia.org/w/rest.php/oauth2/access_token"


# This function is for getting the credentials from credentials.yml
def get_credentials():
    credentials_path = os.path.join(os.getcwd(), "credentials.yml")
    with open(credentials_path) as f:
        credentials = yaml.safe_load(f)
    return credentials


# This function is for getting the token
def get_token():
    credentials = get_credentials()
    files = {
        'grant_type': (None, 'client_credentials'),
        'client_id': (None, credentials['client_id']),
        'client_secret': (None, credentials['client_secret']),
    }

    res = requests.post(
        ACCESS_URL, files=files
    )
    if res.status_code == 200:
        return res.json()['access_token']
    assert False, res.json()


# This function is for getting the headers
def get_headers():
    token = get_token()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    return headers
