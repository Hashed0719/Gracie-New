import requests
import os
import dotenv


dotenv.load_dotenv()
Unsplash_key = os.environ["Unsplash_access_key"]

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
  
