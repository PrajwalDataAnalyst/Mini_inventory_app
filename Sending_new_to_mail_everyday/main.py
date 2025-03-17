import requests
from urllib3 import request
api_key="31527cb11f50415889deb214f7fcf92f"
url =("https://newsapi.org/v2/top-headlines?sources=the-hindu&"\
      "apiKey=31527cb11f50415889deb214f7fcf92f")
re=requests.get(url)
content=re.json()
for i in content['articles']:
    print("title:= ",i['title'],2*"\n")
    print(i['description'])