import requests
from bs4 import BeautifulSoup
from get_link_db import *
import urllib.request
import os
from urllib.parse import urlparse
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_SessionTracker_srchSess=2D73560C1137b1605CiUS2B19145',


    'Host': 'realtrack.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36'
}

payload = {
    'username': 'ali.abbas',
    'password': 'AA4774',
    'function': 'login'
}

create_table()

for i in range(0, 12153):
    url = 'http://realtrack.com/?page=details&skip=' + str(i)
    response = requests.get(url, headers=headers, params=payload)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract text data from different tags
        # header_nav = soup.find('div', id='headerNav').text.strip()
        address = soup.find('strong', id='address').text.strip()
        aerial_photos = soup.find_all('a', rel='shadowbox[aerials]')
        transferors = soup.find('font', color='#848484', string='Transferor(s)').find_next_siblings(string=True)
        transferee_title = soup.find('font', color='#848484', string='Transferee(s)').find_next_sibling('br').next_sibling
        site = soup.find('font', color='#848484', string='Site').find_next_siblings(string=True)
        # assessment_roll_number = soup.find('font', color='#848484', string='Assessment Roll Number').find_next_siblings(
        #     string=True)
        try:
            description_title = soup.find('font', color='#848484', string='Description')
            description = description_title.find_next_sibling('br').next_sibling.strip()
        except:
            description = ""

        consideration_title = soup.find('font', color='#848484', string='Consideration')
        consideration_text = consideration_title.find_next_sibling('br').next_sibling.strip()

        try:
            broker_agent = soup.find('font', color='#848484', string='Broker/Agent').next_sibling.find_next_sibling(
                'br').next_sibling
        except:
            broker_agent = ""

        photos =  ["http://realtrack.com" + a['href'] for a in aerial_photos]
        transferors_sql = [t.strip() for t in transferors][:4]
        site_sql = [s.strip() for s in site][:4]


        insert_data(str(i),address, photos, transferors_sql, transferee_title, site_sql, description, consideration_text,

                    broker_agent)  # Insert the data into the table

        if not os.path.exists("aerial_images/" + str(i)):
            os.makedirs("aerial_images/" + str(i))

        for photo in photos:

            parsed_url = urlparse(photo)
            image_path = parsed_url.path
            image_path = image_path.replace('/assets/files/', '')
            urllib.request.urlretrieve(photo, "aerial_images/"+str(i)+"/" + str(image_path.replace('/', '-')))

        print(i)

    else:
        print('Error:', response.status_code)

