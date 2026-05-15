#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install requests')


# In[22]:


import requests
import datetime
from urllib.parse import urlencode # to turn dictionary into a url ({"q": "Time", "type": "track"}) --> (q=Time&type=track)


# In[23]:


import base64


# In[30]:


# client_id = '234d56555aa14d96a811661dfcf00d64'
# client_secret = '0fb68f689a0c4faabbadc9f88571d739'

client_id = '7131e680b1a7410db76dc664a5d1f4e8'
client_secret = 'caeb543cae33409ebc58ff5cd0ab860c'


# In[32]:


class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        """
        Returns a base64 encoded string
        """
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_id == None:
            raise Exception("You must set client_id and client_secret")
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()

    def get_token_headers(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            "Authorization": f"Basic {client_creds_b64}"
        }

    def get_token_data(self):
        return {
            "grant_type": "client_credentials"
        } 

    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)
        if r.status_code not in range(200, 299):
            return False
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in'] # seconds
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True



# In[33]:


spotify = SpotifyAPI(client_id, client_secret)


# In[34]:


spotify.perform_auth()


# In[35]:


access_token = spotify.access_token
access_token


# In[36]:


headers = {
    "Authorization": f"Bearer {access_token}"
}
endpoint = "https://api.spotify.com/v1/search"
data = urlencode({"q": "Time", "type": "track"})
print(data)

lookup_url = f"{endpoint}?{data}"
print(lookup_url)
r = requests.get(lookup_url, headers=headers)
print(r.status_code)


# In[37]:


r.json()


# In[21]:


data = urlencode({"q": "A Lannister ALways pays his debts", "type": "track"})
lookup_url = f"{endpoint}?{data}"
r = requests.get(lookup_url, headers=headers)
r.json()


# In[ ]:





# In[31]:


import base64
import requests

# Your Spotify API credentials
# client_id = "YOUR_CLIENT_ID"
# client_secret = "YOUR_CLIENT_SECRET"

# Create and encode credentials
client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode()).decode()

# Prepare the request
token_url = "https://accounts.spotify.com/api/token"
headers = {
    "Authorization": f"Basic {client_creds_b64}",
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials"
}

# Make the request with proper error handling
try:
    response = requests.post(token_url, data=data, headers=headers)

    # Print status code and raw response for debugging
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    print(f"Response Headers: {dict(response.headers)}")

    # Check if request was successful
    if response.status_code == 200:
        # Try to parse JSON
        try:
            token_info = response.json()
            access_token = token_info.get('access_token')
            print(f"✅ Success! Access Token: {access_token[:50]}...")
            print(f"Token Type: {token_info.get('token_type')}")
            print(f"Expires In: {token_info.get('expires_in')} seconds")
        except requests.exceptions.JSONDecodeError:
            print("❌ Response was not valid JSON")
            print(f"Raw response: {response.text}")
    else:
        print(f"❌ Request failed with status code: {response.status_code}")
        if response.text:
            print(f"Error details: {response.text}")
        else:
            print("No error details provided in response body")

except requests.exceptions.RequestException as e:
    print(f"❌ Request failed: {e}")


# In[ ]:





# In[38]:


import requests
from urllib.parse import urlencode

# First, verify your token is still valid
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Test with a simple, safe endpoint
test_url = "https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb"  # Radiohead
test_response = requests.get(test_url, headers=headers)

print(f"Test Status Code: {test_response.status_code}")
if test_response.status_code == 200:
    print("✅ Token is valid!")
    print(f"Artist: {test_response.json()['name']}")
else:
    print(f"❌ Token issue: {test_response.status_code}")
    print(f"Response: {test_response.text}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


import base64
import requests
import urllib.parse

# Your app credentials
# client_id = "YOUR_CLIENT_ID"
# client_secret = "YOUR_CLIENT_SECRET"
redirect_uri = "http://localhost:8888/callback"

# Step 1: Get authorization code
auth_url = "https://accounts.spotify.com/authorize?" + urllib.parse.urlencode({
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": redirect_uri,
    "scope": "user-read-private user-read-email",
    "show_dialog": "true"
})

print("=== Spotify Authorization ===")
print("1. Open this URL in your browser:")
print(auth_url)
print("\n2. Log in and approve the app")
print("3. After approval, you'll be redirected to a URL containing a 'code' parameter")
print("4. Copy the entire code from the redirect URL")

# The redirect URL will look like:
# http://localhost:8888/callback?code=AQ...

# Let's assume you get the code and paste it here
authorization_code = input("\nPaste the authorization code from the URL: ")

# Step 2: Exchange code for access token
auth_string = f"{client_id}:{client_secret}"
auth_bytes = auth_string.encode('utf-8')
auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')

token_url = "https://accounts.spotify.com/api/token"
headers = {
    "Authorization": f"Basic {auth_base64}",
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "authorization_code",
    "code": authorization_code,
    "redirect_uri": redirect_uri
}

response = requests.post(token_url, headers=headers, data=data)

if response.status_code == 200:
    token_data = response.json()
    access_token = token_data['access_token']
    refresh_token = token_data.get('refresh_token')

    print("\n✅ Token obtained successfully!")
    print(f"Access Token: {access_token[:50]}...")

    # Step 3: Use the token to make API calls
    headers = {"Authorization": f"Bearer {access_token}"}

    # Test with a simple API call
    test_response = requests.get(
        "https://api.spotify.com/v1/me",  # Gets user info
        headers=headers
    )

    if test_response.status_code == 200:
        user_info = test_response.json()
        print(f"\n✅ Authenticated as: {user_info['display_name']}")
        print(f"Email: {user_info.get('email', 'Not available')}")
        print(f"Subscription: {user_info.get('product', 'Not available')}")

        # Now you can search
        search_response = requests.get(
            "https://api.spotify.com/v1/search",
            headers=headers,
            params={"q": "Time", "type": "track", "limit": 5}
        )

        if search_response.status_code == 200:
            tracks = search_response.json()['tracks']['items']
            print("\n=== Search Results ===")
            for track in tracks:
                print(f"🎵 {track['name']} - {track['artists'][0]['name']}")
        else:
            print(f"Search failed: {search_response.status_code}")
    else:
        print(f"Failed to get user info: {test_response.status_code}")
else:
    print(f"Failed to get token: {response.status_code}")
    print(response.text)


# In[ ]:




