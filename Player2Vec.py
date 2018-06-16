
# coding: utf-8

# In[10]:


import requests
import json


# In[11]:


pos2index = {'CAM':19, 'CDM':18, 'LF': 16, 'RWB': 2, 'DM': 7, 'LB': 5, 'CM': 12, 'CB': 6, 'AM': 13, 'LM': 10, 'SW': 1, 'CF': 14, 'ST': 17, 'LW': 9, 'RF': 15, 'RW': 8, 'RB': 4, 'LWB': 3, 'RM': 11, 'GK': 0}
foot2index = {"Right":0, "Left":1}


# In[12]:





# In[13]:
import torch


def player2vec(id):
    if not id:
        return torch.tensor([])
    resp = requests.get('http://www.easports.com/fifa/ultimate-team/api/fut/item?jsonParamObject={"id":"' + str(id) + '"}')
    obj = json.loads(resp.text)
    if obj["items"]:                           # if player data exists in sofifa
        player = obj["items"][0]
        return torch.tensor([pos2index[player["position"]],
            int(player["birthdate"].split("-", 1)[0]),
            foot2index[player["foot"]],
            player["height"],
            player["weight"],
            player["age"],
            player["acceleration"],
            player["aggression"],
            player["agility"],
            player["balance"],
            player["ballcontrol"],
            player["crossing"],
            player["curve"],
            player["dribbling"],
            player["finishing"],
            player["freekickaccuracy"],
            player["gkdiving"],
            player["gkhandling"],
            player["gkkicking"],
            player["gkpositioning"],
            player["gkreflexes"],
            player["headingaccuracy"],
            player["interceptions"],
            player["jumping"],
            player["longpassing"],
            player["longshots"],
            player["marking"],
            player["penalties"],
            player["positioning"],
            player["potential"],
            player["reactions"],
            player["shortpassing"],
            player["shotpower"],
            player["slidingtackle"],
            player["sprintspeed"],
            player["standingtackle"],
            player["stamina"],
            player["strength"],
            player["vision"],
            player["volleys"],
            player["weakFoot"],
            player["rating"]]).unsqueeze(0)
    return torch.tensor([])
    


# In[ ]:


if __name__ == "__main__":
    player2vec(20801)

