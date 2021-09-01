from bs4 import BeautifulSoup
from bs4.element import ResultSet
import requests
import re

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

def scrape_weather(city):
    result = dict()

    city = city.replace(" ", "+")
    url = "https://www.google.com/search?q=weather+" + city
    
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            result['temp'] = soup.find('span', attrs = {'id':'wob_tm'}).text
            result['location'] = soup.find('div', attrs = {'id':'wob_loc'}).text # TODO: find country
            result['humidity'] = soup.find('span', attrs = {'id':'wob_hm'}).text
            result['precipitation'] = soup.find('span', attrs = {'id':'wob_pp'}).text
            result['wind'] = soup.find('span', attrs = {'id':'wob_ws'}).text
            now = soup.find('img', attrs = {'id':'wob_tci'})
            result['now_svg'] = "http://" + re.findall(r'src=\"//(.*?)\"',str(now))[0]
            
            d0 = soup.find('div', attrs = {'data-wob-di':'0'})
            result['d0_day'] = re.findall(r'aria-label=\"(.*?)\"',str(d0))[0]
            result['d0_max_temp'] = re.findall(r'style=\"display:inline\">(.*?)<',str(d0))[0]
            result['d0_min_temp'] = re.findall(r'style=\"display:inline\">(.*?)<',str(d0))[1]
            result['d0_svg'] = "http://" + re.findall(r'src=\"//(.*?)\"',str(d0))[0]

            d1 = soup.find('div', attrs = {'data-wob-di':'1'})
            result['d1_day'] = re.findall(r'aria-label=\"(.*?)\"',str(d1))[0]
            result['d1_max_temp'] = re.findall(r'style=\"display:inline\">(.*?)<',str(d1))[0]
            result['d1_min_temp'] = re.findall(r'style=\"display:inline\">(.*?)<',str(d1))[1]
            result['d1_svg'] = "http://" + re.findall(r'src=\"//(.*?)\"',str(d1))[0]

            d2 = soup.find('div', attrs = {'data-wob-di':'2'})
            result['d2_day'] = re.findall(r'aria-label=\"(.*?)\"',str(d2))[0]
            result['d2_max_temp'] = re.findall(r'style=\"display:inline\">(.*?)<',str(d2))[0]
            result['d2_min_temp'] = re.findall(r'style=\"display:inline\">(.*?)<',str(d2))[1]
            result['d2_svg'] = "http://" + re.findall(r'src=\"//(.*?)\"',str(d2))[0]

            d3 = soup.find('div', attrs = {'data-wob-di':'3'})
            result['d3_day'] = re.findall(r'aria-label=\"(.*?)\"',str(d3))[0]
            result['d3_max_temp'] = re.findall(r'style=\"display:inline\">(.*?)<',str(d3))[0]
            result['d3_min_temp'] = re.findall(r'style=\"display:inline\">(.*?)<',str(d3))[1]
            result['d3_svg'] = "http://" + re.findall(r'src=\"//(.*?)\"',str(d3))[0]

            d4 = soup.find('div', attrs = {'data-wob-di':'4'})
            result['d4_day'] = re.findall(r'aria-label=\"(.*?)\"',str(d4))[0]
            result['d4_max_temp'] = re.findall(r'style=\"display:inline\">(.*?)<',str(d4))[0]
            result['d4_min_temp'] = re.findall(r'style=\"display:inline\">(.*?)<',str(d4))[1]
            result['d4_svg'] = "http://" + re.findall(r'src=\"//(.*?)\"',str(d4))[0]

            d5 = soup.find('div', attrs = {'data-wob-di':'5'})
            result['d5_day'] = re.findall(r'aria-label=\"(.*?)\"',str(d5))[0]
            result['d5_max_temp'] = re.findall(r'style=\"display:inline\">(.*?)<',str(d5))[0]
            result['d5_min_temp'] = re.findall(r'style=\"display:inline\">(.*?)<',str(d5))[1]
            result['d5_svg'] = "http://" + re.findall(r'src=\"//(.*?)\"',str(d5))[0]

            d6 = soup.find('div', attrs = {'data-wob-di':'6'})
            result['d6_day'] = re.findall(r'aria-label=\"(.*?)\"',str(d6))[0]
            result['d6_max_temp'] = re.findall(r'style=\"display:inline\">(.*?)<',str(d6))[0]
            result['d6_min_temp'] = re.findall(r'style=\"display:inline\">(.*?)<',str(d6))[1]
            result['d6_svg'] = "http://" + re.findall(r'src=\"//(.*?)\"',str(d6))[0]

            d7 = soup.find('div', attrs = {'data-wob-di':'7'})
            result['d7_day'] = re.findall(r'aria-label=\"(.*?)\"',str(d7))[0]
            result['d7_max_temp'] = re.findall(r'style=\"display:inline\">(.*?)<',str(d7))[0]
            result['d7_min_temp'] = re.findall(r'style=\"display:inline\">(.*?)<',str(d7))[1]
            result['d7_svg'] = "http://" + re.findall(r'src=\"//(.*?)\"',str(d7))[0]
    except:
        print("Error in scraping!")

    return result