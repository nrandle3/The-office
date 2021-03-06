# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:59:52 2019

@author: Nathan Randle

This is a program that web scrapes transcripts.foreverdreaming to gather all of the
office quotes into one output file

"""

import requests

import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

import numpy as np
import bs4 
data = []

for i in range(25301,25499): #goes to (25301,25499)
    print("getting page")
    page = requests.get(
            "http://transcripts.foreverdreaming.org/viewtopic.php?f=574&t=%d" % i 
            ,headers = {"user-agent": 
                        "web scrapping to generate markov chains"})
    print("getting soup")
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    
    if ("00") in soup.find("h2").get_text():
        continue
    
    if ("99") in soup.find("h2").get_text():
        continue
    
    if ("Happy Hour") in soup.find("h2").get_text():
        continue
    
    print(soup.find("h2").get_text())
    
    transcript = soup.find_all("p")[1:-3]
    
    transcript = [ line for line in transcript if "ad=doc" not in line.get_text() ]
    
    speakers = []
    
    for i in transcript:
        speakers.append(i.find("strong"))
    
    for (speaker,line) in zip(speakers,transcript):
        
        episode_title = soup.find("h2").get_text()
        # speaker is already done
        
        if speaker:
            speaker = speaker.get_text()
            cleaned_line = line.get_text().replace(speaker + ": ","")
        else:
            continue
            
        data.append([episode_title,
                     speaker,
                     cleaned_line])
    
    
    
npData = np.array(data)
npDataHeaders = {"episode": npData[:,0],"speaker":npData[:,1],"line": npData[:,2]}

df = pd.DataFrame(npDataHeaders)


df.to_csv("Office-scripts.csv")   
    
    
