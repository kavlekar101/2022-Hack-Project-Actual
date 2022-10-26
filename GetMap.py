import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scrappy:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def start(self):
        self.driver.get("https://www.google.com/maps")

    def enterPlace(self, building):
        inputBuilding = self.driver.find_element(By.XPATH, "//input[@id='searchboxinput']")
        inputBuilding.send_keys(building)

        search = self.driver.find_element(By.XPATH, "//button[@id='searchbox-searchbutton']")
        search.click()

    def getHTML(self):
        share = self.driver.find_element(By.XPATH, "//button[@data-value='Share']")
        share.click()


        time.sleep(5)
        embed = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/button[2]")
        embed.click()
        
        text = self.driver.find_element(By.XPATH, "//input[@class='yA7sBe']")
        return text.get_attribute("value")

    
    def quit(self):
        self.driver.quit()

def getInfo(building):
    s = Scrappy()

    s.start()
    s.enterPlace("Baker Systems")
    time.sleep(3)
    res = s.getHTML()
    s.quit()
    return res

#print(getInfo("Baker Systems")[13:-132])