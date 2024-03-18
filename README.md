# api_challenge

This repository is for testing the apis of wikimedia

Setup

1. Please install python in your machine, the version used was 3.11.4

2. Once python is installed download the repo from <github page>

3. Go inside the api_challenge folder

4. Execute the following command:
    pip install -r requirements.txt

5. create a file called credentials.yml inside the api_challenge folder and add the following information:
    client_id: <your_client_id>
    client_secret: <your_client_secret>

    Note: For getting that data you must register in https://api.wikimedia.org/wiki/Main_Page and create an API key  in here https://api.wikimedia.org/wiki/Special:AppManagement

6. You are ready to go!!

Execute tests

1. Go inside the api_challenge folder

2. Execute the following command to run the tests
    python tests.py