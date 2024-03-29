import requests
import urllib3
import json
import os.path
import datetime
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Add contents from the .env file
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
SECURE_TOKEN = os.getenv('SECURE_TOKEN')

# Disable log warnings
urllib3.disable_warnings()


def get_auth():
    # Preparing payload
    headers = {
        'Host': 'securetoken.googleapis.com',
        'User-Agent': 'FirebaseAuth.iOS/8.15.0 AlexisBarreyat.BeReal/0.22.4 iPhone/15.5 hw/iPhone13_3',
        'Accept': 'application/json',
    }

    body = {
        "grantType": "refresh_token",
        "refreshToken": REFRESH_TOKEN
    }

    # Create response
    response = requests.post(SECURE_TOKEN, headers=headers, json=body, verify=False)

    if response.status_code == 200:
        print('Access token fetched!')
    else:
        print('Could not get access token')

    # Deserialize byte to json
    json_object = json.loads(response.text)

    # Extracting the access token from the json object
    token = json_object["access_token"]

    return token


def fetch_data():
    # Fetching the access token
    print('Fetching access token...')
    access_token = get_auth()

    # Preparing payload
    print('Preparing Payload...')

    headers = {
        'Host': 'mobile.bereal.com',
        'User-Agent': 'BeReal/7242 CFNetwork/1333.0.4 Darwin/21.5.0',
        'Accept': 'application/json',
        'Authorization': access_token,
    }

    params = {
        'limit': '20',
    }

    # Sending response
    print('Sending response...')
    response = requests.get('https://mobile.bereal.com/api/feeds/friends', headers=headers, params=params, verify=False)

    # Deserialize byte to json
    json_object = json.loads(response.text)

    # File data
    name_of_file = str(datetime.datetime.now().strftime("%Y-%m-%d-%H.%M"))
    save_path = './results/'
    complete_name = os.path.join(save_path, name_of_file + ".json")

    if response.status_code == 200:
        print('Successfully fetched data...')

        # Write the response to a file
        print('Writing to file...')
        with open(complete_name, 'w') as outfile:
            outfile.writelines(json.dumps(json_object, indent=4))
        print('File saved. See:', complete_name)

        print('*******************************')

        specific = input('Do you wanna see some specific data? (y/n)\n> ')

        if specific == 'y':
            print("Choose an option:\n"
                  "1. Get images\n"
                  "2. Get usernames\n"
                  "3. Get user locations\n"
                  "4. See the full output")

            option = input('> ')

            if option == '1':
                get_images(json_object)
            elif option == '2':
                get_users(json_object)
            elif option == '3':
                get_locations(json_object)
            elif option == '4':
                get_full_output(json_object)
            else:
                print('Quitting...')

    elif response.status_code == 404:
        print('Update your access token')
        # print(json.dumps(json_object, indent=4))
    else:
        print('An error has occurred.')


def get_images(json_object):
    dataset = []
    for key in json_object:
        dataset.append([key['userName'], [key['photoURL'], key['secondaryPhotoURL']]])
    print('Images fetched\n' + json.dumps(dataset, indent=4))


def get_users(json_object):
    dataset = []
    for key in json_object:
        dataset.append([key['userName']])
    print('Users fetched\n' + json.dumps(dataset, indent=4))


def get_locations(json_object):
    dataset = []
    for key in json_object:
        if 'location' in key:
            dataset.append([key['userName'], key.get('location')])
    print('Locations fetched\n' + json.dumps(dataset, indent=4))


def get_full_output(json_object):
    print(json.dumps(json_object, indent=4))


if __name__ == '__main__':
    print('Starting script...')
    fetch_data()
