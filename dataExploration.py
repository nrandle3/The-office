# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:47:31 2019

@author: nrandle
"""

import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


df = pd.read_csv("file:///H:/The-office/Office-scripts.csv")

mainCharacters = df.speaker.value_counts()[:22].index.values
print(mainCharacters[1])


for character in mainCharacters[:1]:
    print(character)
    print()
    for line in df[df.speaker==character].line.values:
        print(line.split(" "))





