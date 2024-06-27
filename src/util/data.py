from urllib import parse
from urllib.request import urlopen
import json
import os

def dataURL(url):
    lang = int(parse.parse_qs(parse.urlparse(url).query)['lang'][0])
    if lang != 1:
        url = url.replace(f'lang={lang}', 'lang=1')
    body = urlopen(url).read()
    data = json.loads(body)
    key_id = int(parse.parse_qs(parse.urlparse(url).query)['key_id'][0])
    return data, key_id

def saveData(data, game_version, path=""):
    print(f"Saving {game_version}...")
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path+game_version, 'w') as f:
        json.dump(data, f, indent=4)