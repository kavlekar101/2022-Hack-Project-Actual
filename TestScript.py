import WebScrape

building = "BE"
startD = "10/06/2022"
endD = "10/06/2022"
startT = "08:00AM"
endT = "10:00PM"

s = WebScrape.Scraper(building, startD, endD, startT, endT)

s.switchToCal()

rooms = WebScrape.getClassrooms(driver)

time.sleep(10)
for r in rooms:
    if enterInformation(driver, r):
        availRooms.append(r)

print("The available rooms are")
for ar in availRooms:
    print(ar)