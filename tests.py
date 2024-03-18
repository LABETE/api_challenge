from pages import *

def test_title_sesame_street_found():
    search_response = search('furry rabbits')
    title_found = False
    for page in search_response['pages']:
        if page['title'] == 'Sesame Street':
            title_found = True
            break
    assert title_found, "The Sesame Street title was not found in the search of furry rabbits"
        
def test_details_sesame_street():
    search_response = search('furry rabbits')
    for page in search_response['pages']:
        if page['title'] == 'Sesame Street':
            page_key_title = page['key']
            break
    title_response = get_page_by_title(page_key_title)
    title_timestamp = title_response['latest']['timestamp'] 
    minimum_expected_date = '2023-08-17'
    assert title_timestamp > minimum_expected_date, f'The timestamp: {title_timestamp} is older that: {minimum_expected_date}'

def test_create_page():
    response = create_page('Hello, world!', 'User:Eddievalv/Sandbox', 'Creating a test page with the Wikimedia API')
    assert response.status_code == 201, f'The creation failed with code: {response.status_code} and the message: {response.json()}'


test_title_sesame_street_found()
test_details_sesame_street()
test_create_page()



############### Other possible tests #########################
"""
Test Creation
    - Verify that you can create a page with all the different options of content_model
Test creation with empty fields
    - Verify that when you send empty strings as follows: "" the page will not be created
    - Verify that if you miss the source the page will not be created
    - Verify that if you miss the title the page will not be created
    - Verify that if you miss the description the page will not be created
Test Edit page
    - Verify that modifying all the fields that are allowed to modify will be modified successfully
Test delete page (if possible, I don't see any endpoint in the page for deleting)
    - Verify that a page can be deleted
Test Returning empty search
    - Verify that if you search for some random string that doesn't exist in any page you will get an empty list
Test failed creation
    - Verify that if you try to create a page with long strings in the title it will fail
    - Verify that if you set a wrong content model the page will not be created
Test failed edition
    - Verify that if set a long string as title it will fail
Test search including special characters
    - Verify that search with special characters can be done
Test page creation with special characters in the title
    - Verify that a page can be created using special characters
Test empty search
    - Verify that search is not breaking when you use empty string: "" for searching
Test creating same page 2 times
    - Verify if it is possible to create 2 times the same page
Test search by title a page that was created with same title 2 times
    - Verify that search by title is not broken if it is possible to create 2 pages with same title
Test images linked to the page
    - Verify the images that are linked to the pages like thumbnails
"""




