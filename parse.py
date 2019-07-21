import requests
from bs4 import BeautifulSoup
import json
import time
import datetime


def parseImage_v(request):
    doc = requests.get(request)
    soup = BeautifulSoup(doc.text, 'html.parser')
    img1 = soup.find("meta", property="og:image")
    type_p = soup.find("meta", property="og:type")

    if img1 and type_p:
        if type_p['content'] == "instapp:photo":
            v_link = True
        else:
            v_link = False
    else:
        v_link = False

    return v_link
    

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
    account_id = js['owner']['id']
    date1 =  datetime.datetime.fromtimestamp(js['taken_at_timestamp'])

    return account, img, date1, photo_id, account_id
    
 
