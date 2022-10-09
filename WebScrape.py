import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time
import random
import re

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# this is the most important
# I need to switch frames I think https://stackoverflow.com/questions/48895434/selecting-item-in-nested-html-frame-with-selenium-webdriver
# this gets into the frame where everything is

class Scraper:
    def __init__(self, building, day, startT, endT):
        self.building = building
        self.day = day
        self.startT = startT
        self.endT = endT
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    def start(self):
        self.driver.get("https://courses.osu.edu/psp/csosuct/EMPLOYEE/PUB/c/OSR_CUSTOM_MENU.OSR_ROOM_MATRIX.GBL?")
    
    def switchToCal(self):
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
            (By.XPATH, "//iframe[@id='ptifrmtgtframe']")))

    def switchToDefault(self):
        self.driver.switch_to.default_content()
    
    def quit(self):
        self.driver.quit()

def getClassrooms(scraper):
    room = scraper.driver.find_elements(By.XPATH, "//input[@id='OSR_DERIVED_RM_FACILITY_ID']") # this is the room number need to figure out a way to find all rooms especially classrooms
    room[0].send_keys(scraper.building)

    # gets into the room list so that we can scrape it
    search = scraper.driver.find_element(By.XPATH, "//a[@id='OSR_DERIVED_RM_FACILITY_ID$prompt']")
    search.click()

    # have to go back to the initial frame and change to this new frame, which is dumb but I got it!
    # so basically, these frames are in a tree structure
    scraper.driver.switch_to.default_content()
    WebDriverWait(scraper.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
        (By.XPATH, "//iframe[@id='ptModFrame_0']")))

    time.sleep(1)

    # name is RESULT0$#, where # is the number so they are unique, but I want all of them, so I just do that
    rooms = scraper.driver.find_elements(
        By.XPATH, "//a[starts-with(@name, 'RESULT0$')]")

    res = [r.get_attribute("innerHTML") for r in rooms]

    # click out of this frame
    cancel = scraper.driver.find_element(By.XPATH, "//input[@id='#ICCancel']")
    cancel.click()
    
    # this just gets the room number better? (I think)
    return res

    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[@id='PTSRCHRESULTS0']")))

def enterInformation(scraper):
    time.sleep(2)
    # entering all of the information
    startDate = scraper.driver.find_element(By.XPATH, "//input[@id='OSR_DERIVED_RM_START_DT']") # start date of the week
    startDate.clear()
    startDate.send_keys(scraper.day) # send it this date in this format, might need to tweak it later

    # time.sleep(random.randint(2,4))
    endDate = scraper.driver.find_element(By.XPATH, "//input[@id='OSR_DERIVED_RM_END_DT']") # end date of the week
    endDate.clear()
    endDate.send_keys(scraper.day) # send it this date in this format, might need to tweak it later

    # time.sleep(random.randint(3, 6))
    startTime = scraper.driver.find_element(By.XPATH, "//input[@id='DERIVED_CLASS_S_MEETING_TIME_START']")
    startTime.clear()
    startTime.send_keys(scraper.startT)
    
    endTime = scraper.driver.find_element(By.XPATH, "//input[@id='DERIVED_CLASS_S_MEETING_TIME_END']")
    endTime.clear()
    endTime.send_keys(scraper.endT)

def changeRooms(scraper, r):
    time.sleep(2.5)
    room = scraper.driver.find_elements(By.ID, "OSR_DERIVED_RM_FACILITY_ID") # this is the room number need to figure out a way to find all rooms especially classrooms
    room[0].clear()
    room[0].send_keys(r)

    refreshCalendar = scraper.driver.find_element(By.ID, "DERIVED_CLASS_S_SSR_REFRESH_CAL") # this finds the refresh calendar button
    refreshCalendar.click() # acually refreshes it, but need sometime to access the actual calendar

    #time.sleep(10)

    #print(driver.page_source)

    # need to wait for this to show up and I need to find the other colors which is just one other one
    redCourses = scraper.driver.find_elements(By.XPATH, "//span[@style='color:rgb(0,0,0);background-color:rgb(222,184,135);']")

    # this gets the red colored calendar elements
    greenCourses = scraper.driver.find_elements(By.XPATH, "//span[@style='color:rgb(0,0,0);background-color:rgb(182,209,146);']")

    # driver.Wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@style='color:rgb(0,0,0);background-color:rgb(222,184,135);']"))

    if len(redCourses) == len(greenCourses) and len(redCourses) == 0:
        return True
    return False

''' This can be used for when I need to find what times a room are free
    not necessarily if a room is free during a certain time
    So I will save this for later'''
def regexStuff():
    # \d\d, \d*, \d+, \d. all work for finding the minutes of the clock time
    # so without the r, the string is a cooked string? and with the r, this becomes a raw string literal.
    times = re.compile(r'(1?\d:\d\d)+')

    # these are the start and end times for the week
    startEnd = set()

    with open("Dump.txt") as f:
        for line in f.readlines():
            test = times.findall(line)
            if test:
                # I know that there will only be a start and an end time for each class
                # so there this only be two entries, if they exist
                startEnd.add((test[0], test[1]))

    print(startEnd)

# I can use regex to make sure that the dates are correct!

# might have to do some other shit when I have to see the calendar stuff but it shouldn't be too hard

def clickDays(driver, days):
    daysOfWeek = {"MONDAY": "//input[@id='DERIVED_CLASS_S_MONDAY_LBL$30$$chk']",
                  "TUESDAY": "//input[@id='DERIVED_CLASS_S_TUESDAY_LBL$chk']",
                  "WEDNESDAY": "//input[@id='DERIVED_CLASS_S_WEDNESDAY_LBL$chk']",
                  "THURSDAY": "//input[@id='DERIVED_CLASS_S_THURSDAY_LBL$chk']",
                  "FRIDAY": "//input[@id='DERIVED_CLASS_S_FRIDAY_LBL$chk']",
                  "SATURDAY": "//input[@id='DERIVED_CLASS_S_SATURDAY_LBL$chk']",
                  "SUNDAY": "//input[@id='DERIVED_CLASS_S_SUNDAY_LBL$chk']"}
    for day in days:
        currDay = None
        currDayCheck = None
        if day.upper() == "MONDAY":
            currDay = driver.find_element(
                By.XPATH, "//input[@id='DERIVED_CLASS_S_MONDAY_LBL$30$$chk']")
        else:
            currDay = driver.find_element(
                By.XPATH, f"//input[@id='DERIVED_CLASS_S_{day.upper()}_LBL$chk']")

        if day.upper() == "MONDAY":
            currDayCheck = driver.find_element(
                By.XPATH, "//input[@id='DERIVED_CLASS_S_MONDAY_LBL$30$']")
        else:
            currDayCheck = driver.find_element(
                By.XPATH, f"//input[@id='DERIVED_CLASS_S_{day.upper()}_LBL']")

        # value = driver.execute_script('return arguments[0].type', currDay)
        
        # might be in a different frame?, but it still works........
        # maybe print out html

        # print(f"Before value: {value}\n")
        
        # this unhides the hidden input
        driver.execute_script('var elem = arguments[0]; var value = arguments[1]; elem.type = value;', currDay, "")

        # value = driver.execute_script('return arguments[0].type', currDay)   

        # print(f"After value: {value}\n")

        # waits until the element is visible
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, daysOfWeek[day.upper()])))
        
        driver.execute_script('arguments[0].click();', currDay)

        driver.execute_script('arguments[0].click();', currDayCheck)

        currDay.click()
    
    refresh = driver.find_element(By.XPATH, "//a[@id='DERIVED_CLASS_S_SSR_REFRESH_CAL$38$']")
    refresh.click()
    time.sleep(1)

def test(building, day, startT, endT):
    s = Scraper(building, day, startT, endT)

    s.start()

    # go to the calendar frame
    s.switchToCal()

    # enters the initial information
    enterInformation(s)

    time.sleep(1)
    # gets the classrooms by switching frames
    rooms = getClassrooms(s)

    # gets the calendar again
    s.switchToDefault()
    s.switchToCal()

    availRooms = []
    time.sleep(1)
    for r in rooms:
        if changeRooms(s, r):
            availRooms.append(r)
    s.quit()
    return availRooms
    

# have to get to the frame with all of the textboxes so that I can enter the stuff
# so first switch back to the original frame, then I can switch to the frame holding all the text input frames

'''startD = input("Enter the start date (properly formatted XX/XX/XXXX):\n")
endD = input("Enter the start date (properly formatted XX/XX/XXXX):\n")
startT = input("Enter the start time (properly formatted XX:XXAM or XX:XXPM):\n")
endT = input("Enter the end time (properly formatted XX:XXAM or XX:XXPM):\n")'''


'''There have been a lot of other cases
Initally apple refused in murder case in san bernidino
FBI just wanted to get all access into
There have been FBI people going to other companies to break open iphones

-> would it be permissible of the CSE experts at the company to break into iphones

-> does Apple have a moral obligation to abide by the law'''


'''
    So basically what I need to do now is
    (For current, which is needed)
    -> Refactoring the code
        -> it should only changes the room number
        -> perhaps adding more documentation for the code
        -> separate into different files so that it is more readable
    -> add inputs for the user to find certain timings and days
    -> implement the checkbox feature so that we can do multiple days
    -> add a sleep timer so that we can make it more "human like"
    -> test the code to make sure that it works as intended

    (Future features)
    -> maybe add something to allow you to find the short form of a building name
        -> figure out how to do this so that I can do the next one
    -> provide the amenities of the room by going to the classroom search thingy (this would be very cool to do)
        -> do a search based on what are needed (this would also be interesting)
    -> maybe add regex to make sure that the inputs are correct
    -> reach out to the people that handle this website and talk to them about this thing
    -> split up the list and create n drivers that run concurrently on different websites
    -> maybe talk to max about it
    -> create a GUI that visualizes the information
    -> make a web app that allows other users to put in which rooms they have reserved (FCFS basis)
        -> could change this to make a need basis (for interview or something)
        -> allow people/teachers to say when their classes are closed so that those rooms are marked as open
    -> something location based (i.e. I want an open room within a x mile radius/5 min walk because of my schedule)
        -> This is also interesting!
        -> say distance from your current location or future location
    -> classroom hopping if you are about to get kicked out of a current one
        -> chain together the searches so that you can find ones for a certain time block
    -> something that allows you to find multiple buildings and give you all of the results
    -> ranking system of the available rooms (based on whatever you want)
        -> could be based on amenities, location, time period available, etc.
    -> merge the availablity based on holidays, so if there is a holiday or a weekend, then the buildings are probably not open
    -> could extend this to more study spots in general for example the library

    (For a different implementation)
    -> implement something that allows users to find what rooms are open during what times
        -> We can use the leetcode question for the intervals
    -> try to implement in javascript for webapp or even in ruby
'''


'''(0,2,2)
(1,1,2)
(1,1,3)
(0,2,2)'''
