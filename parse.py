
import requests
from bs4 import BeautifulSoup
import json
import time
import datetime


def parseImage_2(request):
    doc = requests.get(request)

    soup = BeautifulSoup(doc.text, 'html.parser')
    body = soup.find('body')
    script_tag = body.find('script')
    raw_string = script_tag.text.strip().replace('window._sharedData =', '').replace(';', '')
    json_data=json.loads(raw_string)
    js=json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']
    photo_id = js['shortcode']
    img = js['display_url']
    account = js['owner']['username']
    date1 =  datetime.datetime.fromtimestamp(js['taken_at_timestamp'])

    return account, img, date1, photo_id
    
 
