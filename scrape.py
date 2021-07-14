from selenium import webdriver 
from bs4 import BeautifulSoup 
import request
import time 
import csv 
start_url='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser.get(start_url)
time.sleep(2)
def Scrap():
    headers=['name','distance','mass','radius']
    stars_data=[]
            stars_data.append(temp_list)
    with open('scraper1.csv','w') as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)
Scrap()
