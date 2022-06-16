import requests 
import os 
import dotenv

dotenv.load_dotenv()
tenor_key = os.environ['Tenor_api_key']

def getGif(term :str) -> str:
  """Returns a gif link based on the top searches for the given term as parameter"""
  url = "https://g.tenor.com/v1/random"
  params = {
    "key": tenor_key,
    "q": term,
    "contentfilter": "medium",
    "ar_range": "standard",
    "limit": 1
  }
  response = requests.get(url=url, params=params).json()
  gif_link = response["results"][0]["media"][0]["gif"]["url"]
  return gif_link
