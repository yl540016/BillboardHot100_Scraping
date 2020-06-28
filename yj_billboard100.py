
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests
import time
import csv
import re

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.implicitly_wait(3)

url = "https://www.billboard.com/charts/hot-100"
driver.get(url)

csv_filename= "Billboard_Hot100.csv"
csv_open= open(csv_filename, 'w+', encoding = 'utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow(("Rank", "Title", "Artist", "Image"))

body = driver.find_element_by_css_selector("body")
for i in range(25):
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(1)

html = driver.page_source
bs = BeautifulSoup(html, "html.parser")
total_list = bs.find_all("button", {"class":"chart-element__wrapper"})

for content in total_list:
	song_rank = content.find("span", {"class":"chart-element__rank__number"}).text
	song_title = content.find("span",{"class":"chart-element__information__song text--truncate color--primary"}).text
	song_artist = content.find("span",{"class":"chart-element__information__artist text--truncate color--secondary"}).text
	song_image = content.find("span", {"class":"chart-element__image"})["style"]
	csv_writer.writerow((song_rank, song_title, song_artist, song_image[23:-3]))

driver.close()
