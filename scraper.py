import requests
from bs4 import BeautifulSoup

# URL of the page containing the video
url = "https://pstream.org/e7c654c7-3a75-4103-9c81-dd9a302cf8e2"

# Send a GET request to fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the div with class 'panel-player'
panel_player_div = soup.find('div', class_='panel-player')

# If the div is found, find the iframe or video tag inside it
if panel_player_div:
    iframe = panel_player_div.find('iframe')
    print("HI")
    
    if iframe:
        # Extract the 'src' URL from the iframe tag
        video_url = iframe['src']
        print(f"Video URL: {video_url}")
    else:
        print("No iframe found inside the panel-player div.")
else:
    print("No div with class 'panel-player' found.")
