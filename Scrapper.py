from bs4 import BeautifulSoup
import requests

# Gets the world covid-19 statistics with WebScrappy by using BeautifoulSoup and requests module. 
# We just need the world cases, total deaths and recovered covid-19 people to display it on the GUI.
# The list named Statistics gets the info from the divs with the id below. Each index of the list is 
# one variable of the statistics we need. Open the website to find more information.
def UpdateCovid19Info(t1, t2, t3):
    source = requests.get("https://www.worldometers.info/coronavirus/").text 
    soup = BeautifulSoup(source, "lxml")
    Statistics = soup.find_all("div", id = "maincounter-wrap")
    Counter = 0
    for Text in [t1, t2, t3]:
        Text.set(Statistics[Counter].div.span.text)
        Counter += 1