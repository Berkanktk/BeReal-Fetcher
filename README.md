# BeReal Data Fetcher
A simple script to scrape data from BeReal without posting anything.

This tool will gather the following data in a JSON format from your Dashboard by default:
- Posted pictures (Primary and secondary)
- Location details
- Realmojis and comments made on a post
- Information about if a post was late or not
- User region
- Time posted
- And many other user specific things

## Running the Script
1. Install the required packages with `pip install -r requirements.txt`
2. Make a copy of the `.env.example` with the name `.env`
3. Fill in data inside the `.env` file. (Charles Proxy from the App Store is recommended)
4. Locate the `Bereal_fetcher.py` file and run it
5. The result will be save inside the `/results` folder as a json file.
   1. The user is also prompted by the terminal in case an output inside the terminal is wanted.

### How it works
When the `main` method is run, the `getBRData()` method is called, which then fires `getAuth()` in order to fetch an access token, which is needed to send an HTTP response with authentication to get the JSON data from a specified BeReal endpoint. 

# Charles Proxy (Getting the required tokens)
Charles Proxy is a tool that can be used to intercept and modify HTTP requests and responses. It is a great tool to use when you want to see what is going on behind the scenes of an app.

To get the `REFRESH_TOKEN` and `SECURE_TOKEN` used withing the `.env` file, you need to intercept the request that is sent to the BeReal API. This can be done by using Charles Proxy.

## How to use Charles Proxy
1. Download Charles Proxy from the App Store.
2. Open the app and click on the `Settings` button in the top left corner.
3. Click on `SSL Proxying` and enable it.
4. You can also create a CA certificate if you want. Just follow the instructions on the screen.
5. Go back to the main screen and click on the `Status` button to start recording the traffic.
6. Open the BeReal app and click around a bit. 
7. Go back to the main screen and click on the `Status` button to stop recording the traffic.
8. Now, go into the recorded session and locate https://securetoken.googleapis.com.
9. Click on the request and copy the URL from the overview tab. This is the `SECURE_TOKEN`.
10. Next, go to the bottom of the same page and find the Request Body tab, and click on "View Body". The refreshToken here is the `REFRESH_TOKEN` you should insert into the `.env` file.

# BeReal Endpoints
In case you want to use a specific endpoint, simply change it inside the Bereal_fetcher.py script at line 70. 

**Example**:  
From the /friends endpoint   
```python
response = requests.get('https://mobile.bereal.com/api/feeds/friends', headers=headers,  params=params, verify=False)
```

to the /memories endpoint  
```python
response = requests.get('https://mobile.bereal.com/api/feeds/memories', headers=headers, params=params, verify=False)
```

## Discovery Feed endpoint
Posts of users who choose to make their posts public  

**Endpoint:** `/api/feeds/discovery`  

## Friends Feed endpoint
Posts of users who are connected with the user.

**Endpoint:** `/api/feeds/friends`  

## Scan Contacts endpoint
Shows contact data.

**Endpoint:** `/scanContacts`  

## Friend Suggestions endpoint
Shows data about the profiles under the suggestions tab.

**Endpoint:** `/friendSuggestions`  

## Memories endpoint
Shows all of your memories.

**Endpoint:** `/memories`  

