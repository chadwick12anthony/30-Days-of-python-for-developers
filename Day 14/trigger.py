import requests


# ngrok_url = "https://abbie-unmummified-overreflectively.ngrok-free.dev"
ngrok_url = "https://abbie-unmummified-overreflectively.ngrok-free.dev"
endpoint = f"{ngrok_url}/flask-scrape"

r = requests.post(endpoint, json={})

print(r.json()["data"])
#print(r.text)