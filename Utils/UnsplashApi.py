import requests

import os


Unsplash_key = os.getenv("Unsplash_access_key")

def RandomImage(term):
  url="https://api.unsplash.com/photos/random"
  params={
    "client_id": Unsplash_key,
    "query": term,
    "orientation": "landscape"
  }
  response = requests.get(url=url, params=params).json()
  image_url = response["urls"]["raw"]
  return image_url
  
