from bs4 import BeautifulSoup
import requests
import re
from bs4.element import Tag

def getSoup(url):
    return BeautifulSoup(requests.get(url).text, "html.parser")

# gets the names of the academic buildings
soup = getSoup("https://odee.osu.edu/classroom-search")

# print(soup.prettify())
# prints all of the rooms in the building
'''for div in soup.find_all('div', 'views-accordion-grouped-row'):
    print(div.text)'''

# gets all of the academic building names with classrooms in them
# probably add the other buildings as a feature later
buildings = []
for div in soup.find_all('h3', 'views-accordion-classroom_browse-block_1-header views-accordion-header'):
    buildings.append(div.text[1:-1])

soup = getSoup("https://www.osu.edu/map/buildingindex.php#U")

listOfNames = []
shortMap = {}

# gets all of the li with the building names
for li in soup.find_all('li'):
    for child in li.childGenerator():
        if isinstance(child, Tag):
            if child.get('href') and child['href'][:22] == "building.php?building=":
                listOfNames.append(child)
            if re.match(r'^\([A-Z]{2,3}\)', child.get_text()):
                listOfNames.append(child)
                # eventually we might not need this if because we can just support all of the buildings
                if listOfNames[-2].get_text()[:-8] in buildings:
                    shortMap[listOfNames[-2].get_text()[:-8]] = listOfNames[-1].get_text()[1:-1]