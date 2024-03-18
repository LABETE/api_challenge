import requests
import json
from helpers import get_headers

headers = get_headers()

# This will search any text in the pages
def search(search_query):
    search_url = 'https://api.wikimedia.org/core/v1/wikipedia/en/search/page'
    parameters = {'q': search_query}
    response = requests.get(search_url, params=parameters)
    if response.status_code == 200:
        return response.json()
    assert False, response.json()

# This will search any page by key title
def get_page_by_title(key_title):
    page_url = 'https://api.wikimedia.org/core/v1/wikipedia/en/page/' + key_title + '/bare'
    response = requests.get(page_url)
    if response.status_code == 200:
        return response.json()
    assert False, response.json()

# This will create a page
def create_page(source, title, comment):
    create_page_url = 'https://api.wikimedia.org/core/v1/wikipedia/en/page'
    data = {
        'source': source,
        'title': title,
        'comment': comment
    }
    response = requests.post(create_page_url, headers=headers, data=json.dumps(data))
    return response
