import requests

Youtube_api_key = 'blablabla' # Votre clé API

mot = 'how+to+scrape+title+in+youtube'
big_tab = []
response = requests.get('https://www.googleapis.com/youtube/v3/search?maxResults=200&key=' + Youtube_api_key + '&part=snippet&q=' + mot + '&type=video')
content = response.json()
for el in content['items']:
    big_tab.append(el['snippet']['title'])

f = open('youtube_title.txt', "w", encoding="utf8")
for el in big_tab:
    f.write(el + '\n')

f.close()