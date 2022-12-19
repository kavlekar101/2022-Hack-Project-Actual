import requests
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import uncurl

import pycurl
from urllib.parse import urlencode

c = pycurl.Curl()
#initializing the request URL
c.setopt(c.URL, 'https://courses.osu.edu/psc/csosuct/EMPLOYEE/PUB/c/OSR_CUSTOM_MENU.OSR_ROOM_MATRIX.GBL')
#the data that we need to Post
post_data = {'OSR_DERIVED_RM_FACILITY_ID': 'BE0128', 
    'DERIVED_CLASS_S_START_DT': '11/02/2022', 
    'DERIVED_CLASS_S_MEETING_TIME_START': '8:00AM', 
    'DERIVED_CLASS_S_MEETING_TIME_END': '10:00PM', 
    'OSR_DERIVED_RM_START_DT': '11/01/2022', 
    'OSR_DERIVED_RM_END_DT': '11/01/2022'}
# encoding the string to be used as a query
postfields = urlencode(post_data)
#setting the cURL for POST operation
c.setopt(c.POSTFIELDS, postfields)
# perform file transfer
c.perform()

print(c)

#Ending the session and freeing the resources
c.close()