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
1. Make a copy of the `.env.example` with the name `.env`
2. Fill in data inside the `.env` file. (Charles Proxy from the App Store is recommended)
3. Locate the `Bereal_fetcher.py` file and run it
4. The result will be save inside the `/results` folder as a json file.
   1. The user is also prompted by the terminal in case an output inside the terminal is wanted.

### How it works
When the `main` method is run, the `getBRData()` method is called, which then calls `getAuth()` in order to fetch the access token needed for the method to send a http response with authentication to get the JSON data from BeReal. 
## BeReal Endpoints
### /api/feeds/discovery
Posts of users who choose to make their posts public 
### /api/feeds/friends
Posts of users who are connected with the user
### /scanContacts
Shows contact data 
### /friendSuggestions
Shows data about the profiles under the suggestions tab
