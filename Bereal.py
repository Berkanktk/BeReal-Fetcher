import requests
import urllib3
import json
import os.path
import datetime
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Add contents from the .env file
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

# Disable log warnings
urllib3.disable_warnings()

# Prepare Payload
headers = {
    'Host': 'mobile.bereal.com',
    'User-Agent': 'BeReal/7242 CFNetwork/1333.0.4 Darwin/21.5.0',
    'Accept': 'application/json',
    'Authorization': AUTH_TOKEN,
}

params = {
    'limit': '20',
}

# Create response
response = requests.get('https://mobile.bereal.com/api/feeds/friends', headers=headers, params=params, verify=False)

# Deserialize byte to json
json_object = json.loads(response.text)

# File data
name_of_file = str(datetime.datetime.now().strftime("%Y-%m-%d-%H.%M"))
save_path = './results/'
completeName = os.path.join(save_path, name_of_file + ".json")


if response.status_code == 200:
    print('Successfully fetched data.')

    # Write the response to a file
    print('Writing to file')
    with open(completeName, 'w') as outfile:
        outfile.writelines(json.dumps(json_object, indent=4))

    # Terminal output
    print_response = input('Do you wanna see the result in the terminal? y/n\n> ')

    if print_response == 'y':
        # Printing the response
        print(json.dumps(json_object, indent=4))

elif response.status_code == 404:
    print('Update your access token')
    # print(json.dumps(json_object, indent=4))
else:
    print('An error has occurred.')
