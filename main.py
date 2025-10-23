import requests
from bs4 import BeautifulSoup
import pandas as pd

req = requests.get("https://www.yallakora.com/match-center?date=10/23/2025#days")
soup = BeautifulSoup(req.content, 'html.parser')
tittles = soup.find_all("div", {"class": "matchCard"})
all_matches = []  

for titt in tittles:
    title_name = (titt.contents[1]).find("h2").text.strip()
    match_items = titt.contents[3].find_all("div", {"class": "liItem"})  
    
    for match in match_items: 
        try:
            chhanels = match.find("div", {"class": "channel"}).text.strip()
        except:
            chhanels = "No channels"
        
        data = match.find("div", {"class": "date"}).text.strip()
        home_team = match.find("div", {"class": "teamA"}).find("p").text.strip()
        result = match.find("div", {"class": "MResult"}).find("span", {"class": "score"}).text.strip()
        away_team = match.find("div", {"class": "teamB"}).find("p").text.strip()
        Time_of_start = match.find("div", {"class": "MResult"}).find("span", {"class": "time"}).text.strip()
        
        match_data = [title_name, chhanels, data, home_team, result, away_team, Time_of_start]
        all_matches.append(match_data) 
df=pd.DataFrame(all_matches, columns=["Title", "Channels", "Date", "Home Team", "Result", "Away Team", "Start Time"])
df.to_csv("matches.csv", index=False)