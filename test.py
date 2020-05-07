import json
import random
#kanjiList
kotd=[]
with open('E:/Projects/KOTD//KOTD/dict/JMDict.json',encoding="utf8") as f:
    data=json.load(f)

rndK=random.choice(data)
kotd.append(rndK['k_ele'][0]['keb'][0])
kotd.append(rndK['r_ele'][0]['reb'][0])
kotd.append(rndK['sense'][0]['gloss'][0])


