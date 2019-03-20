import requests
from bs4 import BeautifulSoup

page = requests.get("http://transcripts.foreverdreaming.org/viewtopic.php?f=574&t=25442",
                    headers = {'User-Agent': 'Script Gathering'})

soup = BeautifulSoup(page.content, 'html.parser')

transcript = list(soup.find_all("p"))[1:-3]
speakers = list(soup.find_all("strong"))


for line in transcript:
    if "ad=document" in line.get_text():
        transcript.remove(line)
lines=[]
for (line,speaker) in zip(transcript,speakers):
    lines.append(line.get_text().replace(speaker.get_text() + ": ", ""))
print(lines[-1])