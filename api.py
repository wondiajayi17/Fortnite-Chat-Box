import requests
import json
from pprint import pprint
import datetime
import time

url = "https://fortniteapi.io/v2/items/list?lang=en"

headers = {
    "Authorization": "ed293dc1-752bb6b4-001822fc-2f11ed05"
}
#variables used to manipulate the Fortnite APi
response = requests.get(url, headers=headers)
response_json = response.json()
response_text = requests.get(url, headers=headers).text
response_info = json.loads(response_text)
#gets items from the api
response_items = response_json['items']
#length of list of items in the api
Item_Length = len(response_items)


#stores response from API in a file (used just for testing) 
f = open("ApiResponse.txt","w")
f.write(response_text)
f.close()

#adds names of items to a file (used just for the sake of testing)
itemfile = open("ApiResponse-Items.txt","w")
for x in range (len(response_json['items'])):
    
    itemfile.write(response_json['items'][x]['name'])
    #new line
    itemfile.write("\n")

#add the id of items to a file (to make it clear what we're searching for)/ No duplicates
h = open("ApiResponse-ItemsID.txt","w")
for x in range(Item_Length):
    h.write(response_json['items'][x]['type']['id'])
    h.write("\n")
h.close()   
lines_seen = set() # holds lines already seen
#Removes duplicates from file
with open("ApiResponse-ItemsID.txt","r+") as t:
    d = t.readlines()
    t.seek(0)
    for i in d:
        if i not in lines_seen:
            t.write(i)
            lines_seen.add(i)
    t.truncate()

#Calls name of all emotes
def AllEmotes():
    for x in range(Item_Length):
        if response_items[x]['type']['id'].lower() == "emote":
            print("\n",response_items[x]['name'])
            #helps for items to be printed out in a readable way
            time.sleep(1)
# calls name of all outfits(skins)
def AllSkins():
    for x in range(Item_Length):
        if response_items[x]['type']['id']=='outfit':
            print("\n",response_items[x]['name'])
            #helps for items to be printed out in a readable way
            time.sleep(1)

#Calls name of all gliders
def AllGliders():
    for x in range(Item_Length):
        if response_items[x]['type']['id']=='glider':
            print("\n",response_items[x]['name'])
            #helps for items to be printed out in a readable way
            time.sleep(1)

#Calls name of all the Pickaxes'
def AllPickaxes():
    for x in range(Item_Length):
        if response_items[x]['type']['id']=='pickaxe':
            print("\n",response_items[x]['name'])
            #helps for items to be printed out in a readable way
            time.sleep(1)

#function to get requested emote rarity
def GetEmoteRarity(Emote_Name):
    for i in range(Item_Length):
        if response_items[i]['type']['id']=='emote':
            if response_items[i]['name'].lower()== Emote_Name.lower():
                print("Rarity:",response_items[i]['rarity']['id'])

#function to get requested skin rarity
def GetSkinRarity(Skin_Name):
    for i in range(Item_Length):
        if response_items[i]['type']['id']=='outfit':
            if response_items[i]['name'].lower()== Skin_Name.lower():
                print("Rarity:", (response_items[i]['rarity']['id']))

#function to get requested glider rarity                
def GetGliderRarity(Glider_Name):
    for i in range(Item_Length):
        if response_items[i]['type']['id']=='glider':
            if response_items[i]['name'].lower()== Glider_Name.lower():
                print("Rarity:",response_items[i]['rarity']['id'])

#function to get requested pickaxe rarity   
def GetPickaxeRarity(Pickaxe_Name):
    for i in range(Item_Length):
        if response_items[i]['type']['id']=='pickaxe':
            if response_items[i]['name'].lower()== Pickaxe_Name.lower():
                print("Rarity:",response_items[i]['rarity']['id'])

#fuction to the call the requested emote release date
def GetEmoteReleaseDate(Emote_Name):
    for i in range(Item_Length):
        if response_items[i]['type']['id']=='emote':
            if response_items[i]['name'].lower()== Emote_Name.lower():
                if response_items[i]['releaseDate'] == None:
                    print ("Release date:",response_items[i]['added']['date'])
                else:
                    print("Release date:",response_items[i]['releaseDate'])  

#fuction to the call the requested skins release date
def GetSkinReleaseDate(Skin_Name):
    for i in range(Item_Length):
        if response_items[i]['type']['id']=='outfit':
            if response_items[i]['name'].lower() == Skin_Name.lower():
                if response_items[i]['releaseDate'] == None:
                    print ("Release date:",response_items[i]['added']['date'])
                else:
                    print("Release date:",response_items[i]['releaseDate'])

#fuction to the call the requested glider release date
def GetGliderReleaseDate(Glider_Name):
    for i in range(Item_Length):
        if response_items[i]['type']['id']=='glider':
            if response_items[i]['name'].lower()== Glider_Name.lower():
                if response_items[i]['releaseDate'] == None:
                    print ("Release date:",response_items[i]['added']['date'])
                else:
                    print("Release date:",response_items[i]['releaseDate'])

#fuction to the call the requested pickaxe release date
def GetPickaxeReleaseDate(Pickaxe_Name):
    for i in range(Item_Length):
        if response_items[i]['type']['id']=='pickaxe':
            if response_items[i]['name'].lower()== Pickaxe_Name.lower():
                if response_items[i]['releaseDate'] == None:
                    print ("Release date:",response_items[i]['added']['date'])
                else:
                    print("Release date:",response_items[i]['releaseDate'])

#function to return the price of a emote
def GetEmotePrice(Emote_Name):
    for i in range(Item_Length):
        if response_items[i]['type']['id']=='emote':
            if response_items[i]['name'].lower()== Emote_Name.lower():
                if response_items[i]['price'] == 0:
                    print ("Price: cannot be priced as it is a Battlepass/free/exclusive item")
                else:
                    print("Price:",response_items[i]['price'])

#function to return the price of a skin 
def GetSkinPrice(Skin_Name):
    for i in range(Item_Length):
        if response_items[i]['type']['id']=='outfit':
            if response_items[i]['name'].lower()== Skin_Name.lower():
                if response_items[i]['price'] == 0:
                    print ("Price: cannot be priced as it is a Battlepass/free/exclusive item")
                else:
                    print("Price:",response_items[i]['price'])

#function to return the price of a glider
def GetGliderPrice(Glider_Price):
    for i in range(Item_Length):
        if response_items[i]['type']['id']=='glider':
            if response_items[i]['name'].lower() == Glider_Price.lower():
                if response_items[i]['price'] == 0:
                    print ("Price: cannot be priced as it is a Battlepass/free/exclusive item")
                else:
                    print("Price:",response_items[i]['price'])
#function to return the price of a pickaxe
def GetPickaxePrice(Pickaxe_Name):
    for i in range(Item_Length):
        if response_items[i]['type']['id']=='pickaxe':
            if response_items[i]['name'].lower() == Pickaxe_Name.lower():
                if response_items[i]['price'] == 0:
                    print ("Price: cannot be priced as it is a Battlepass/free/exclusive item")
                else:
                    print("Price:",response_items[i]['price'])


#function to get the skin from the price
def GetSkinsFromPrice(Skin_Price):
    for i in range(Item_Length):
        if response_items[i]['type']['id'] == 'outfit':
            if response_items[i]['price'] == Skin_Price:
                if response_items[i]['price'] == 0:
                    print ("Price: cannot be priced as it is a Battlepass/free/exclusive item")
                else:
                    print("Skin:",response_items[i]['name'])
                    print("Rarity:",response_items[i]['rarity']['id'])
                    print("Release date:",response_items[i]['releaseDate'])
                    print("Price:",response_items[i]['price'],"\n")

#function to get the skin from the rarity
def GetSkinsFromRarity(Skin_Rarity):
    if Skin_Rarity.lower() == 'epic': #this is because for somereason all the other rarities but epic are saved in uppercase. Just fixes a formatting logical error
        Skin_Rarity = 'Epic'
    else:
        Skin_Rarity = Skin_Rarity.upper()

    for i in range(Item_Length):
        if response_items[i]['type']['id']=='outfit':
            if response_items[i]['rarity']['name'] == Skin_Rarity:
                print("Skin:",response_items[i]['name'])
                print("Rarity:",response_items[i]['rarity']['id'])
                print("Release date:",response_items[i]['releaseDate'])
                if response_items[i]['price'] == 0:
                    print ("Price: cannot be priced as it is a Battlepass/free/exclusive item","\n")
                else:
                     print("Price:",response_items[i]['price'],"\n")
                        


#function to get the skin from the release date
def GetSkinsFromReleaseDate(Release_Date):
   for i in range(Item_Length):
        if response_items[i]['type']['id']=='outfit':
            if response_items[i]['releaseDate']== None and response_items[i]['added']['date'] == Release_Date:
                    print("Skin:",response_items[i]['name'])
                    print("Rarity:",response_items[i]['rarity']['id'])
                    if response_items[i]['price'] == 0:
                        print ("Price: cannot be priced as it is a Battlepass/free/exclusive item","\n")
                    else:
                        print("Price:",response_items[i]['price'],"\n")
                        
            elif response_items[i]['releaseDate']== Release_Date:  
                print("Skin:",response_items[i]['name'])
                print("Rarity:",response_items[i]['rarity']['id'])
                if response_items[i]['price'] == 0:
                    print ("Price: cannot be priced as it is a Battlepass/free/exclusive item","\n")
                else:
                    print("Price:",response_items[i]['price'],"\n")


#function to get the Pickaxe from the price
def GetPickaxesFromPrice(Pickaxe_Price):
    for i in range(Item_Length):
        if response_items[i]['type']['id'] == 'pickaxe':
            if response_items[i]['price'] == Pickaxe_Price:
                if response_items[i]['price'] == 0:
                    print ("Price: cannot be priced as it is a Battlepass/free/exclusive item")
                else:
                    print("Pickaxe:",response_items[i]['name'])
                    print("Rarity:",response_items[i]['rarity']['id'])
                    print("Release date:",response_items[i]['releaseDate'])
                    print("Price:",response_items[i]['price'],"\n")

#function to get the Pickaxe from the rarity
def GetPickaxesFromRarity(Pickaxe_Rarity):
    if Pickaxe_Rarity.lower() == 'epic': #this is because for somereason all the other rarities but epic are saved in uppercase. Just fixes a formatting logical error
        Pickaxe_Rarity = 'Epic'
    else:
        Pickaxe_Rarity = Pickaxe_Rarity.upper()

    for i in range(Item_Length):
        if response_items[i]['type']['id']=='pickaxe':
            if response_items[i]['rarity']['name'] == Pickaxe_Rarity:
                print("Pickaxe:",response_items[i]['name'])
                print("Rarity:",response_items[i]['rarity']['id'])
                print("Release date:",response_items[i]['releaseDate'])
                if response_items[i]['price'] == 0:
                    print ("Price: cannot be priced as it is a Battlepass/free/exclusive item","\n")
                else:
                     print("Price:",response_items[i]['price'],"\n")
                        
#function to get the pickaxe from the release date
def GetPickaxesFromReleaseDate(Release_Date):
   for i in range(Item_Length):
        if response_items[i]['type']['id']=='pickaxe':
            if response_items[i]['releaseDate']== None and response_items[i]['added']['date'] == Release_Date:
                    print("Pickaxe:",response_items[i]['name'])
                    print("Rarity:",response_items[i]['rarity']['id'])
                    if response_items[i]['price'] == 0:
                        print ("Price: cannot be priced as it is a Battlepass/free/exclusive item","\n")
                    else:
                        print("Price:",response_items[i]['price'],"\n")
                        
            elif response_items[i]['releaseDate']== Release_Date:  
                print("Pickaxe:",response_items[i]['name'])
                print("Rarity:",response_items[i]['rarity']['id'])
                if response_items[i]['price'] == 0:
                    print ("Price: cannot be priced as it is a Battlepass/free/exclusive item","\n")
                else:
                    print("Price:",response_items[i]['price'],"\n")


#function to get the Emote from the price
def GetEmotesFromPrice(Emote_Price):
    for i in range(Item_Length):
        if response_items[i]['type']['id'] == 'emote':
            if response_items[i]['price'] == Emote_Price:
                if response_items[i]['price'] == 0:
                    print ("Price: cannot be priced as it is a Battlepass/free/exclusive item")
                else:
                    print("Emote:",response_items[i]['name'])
                    print("Rarity:",response_items[i]['rarity']['id'])
                    print("Release date:",response_items[i]['releaseDate'])
                    print("Price:",response_items[i]['price'],"\n")

#function to get the emote from the rarity
def GetEmotesFromRarity(Emote_Rarity):
    if Emote_Rarity.lower() == 'epic': #this is because for somereason all the other rarities but epic are saved in uppercase. Just fixes a formatting logical error
        Emote_Rarity = 'Epic'
    else:
        Emote_Rarity = Emote_Rarity.upper()

    for i in range(Item_Length):
        if response_items[i]['type']['id']=='emote':
            if response_items[i]['rarity']['name'] == Emote_Rarity:
                print("Emote:",response_items[i]['name'])
                print("Rarity:",response_items[i]['rarity']['id'])
                print("Release date:",response_items[i]['releaseDate'])
                if response_items[i]['price'] == 0:
                    print ("Price: cannot be priced as it is a Battlepass/free/exclusive item","\n")
                else:
                     print("Price:",response_items[i]['price'],"\n")
                        
#function to get the Emote from the release date
def GetEmotesFromReleaseDate(Release_Date):
   for i in range(Item_Length):
        if response_items[i]['type']['id']=='emote':
            if response_items[i]['releaseDate']== None and response_items[i]['added']['date'] == Release_Date:
                    print("Emote:",response_items[i]['name'])
                    print("Rarity:",response_items[i]['rarity']['id'])
                    if response_items[i]['price'] == 0:
                        print ("Price: cannot be priced as it is a Battlepass/free/exclusive item","\n")
                    else:
                        print("Price:",response_items[i]['price'],"\n")
                        
            elif response_items[i]['releaseDate']== Release_Date:  
                print("Emote:",response_items[i]['name'])
                print("Rarity:",response_items[i]['rarity']['id'])
                if response_items[i]['price'] == 0:
                    print ("Price: cannot be priced as it is a Battlepass/free/exclusive item","\n")
                else:
                    print("Price:",response_items[i]['price'],"\n")
                




#function to get the Glider from the price
def GetGlidersFromPrice(Glider_Price):
    for i in range(Item_Length):
        if response_items[i]['type']['id'] == 'glider':
            if response_items[i]['price'] == Glider_Price:
                if response_items[i]['price'] == 0:
                    print ("Price: cannot be priced as it is a Battlepass/free/exclusive item")
                else:
                    print("Glider:",response_items[i]['name'])
                    print("Rarity:",response_items[i]['rarity']['id'])
                    print("Release date:",response_items[i]['releaseDate'])
                    print("Price:",response_items[i]['price'],"\n")

#function to get the Glider from the rarity
def GetGlidersFromRarity(Glider_Rarity):
    if Glider_Rarity.lower() == 'epic': #this is because for somereason all the other rarities but epic are saved in uppercase. Just fixes a formatting logical error
        Glider_Rarity = 'Epic'
    else:
        Glider_Rarity = Glider_Rarity.upper()

    for i in range(Item_Length):
        if response_items[i]['type']['id']=='glider':
            if response_items[i]['rarity']['name'] == Glider_Rarity:
                print("Glider:",response_items[i]['name'])
                print("Rarity:",response_items[i]['rarity']['id'])
                print("Release date:",response_items[i]['releaseDate'])
                if response_items[i]['price'] == 0:
                    print ("Price: cannot be priced as it is a Battlepass/free/exclusive item","\n")
                else:
                     print("Price:",response_items[i]['price'],"\n")
                        
#function to get the Glider from the release date
def GetGlidersFromReleaseDate(Release_Date):
   for i in range(Item_Length):
        if response_items[i]['type']['id']=='glider':
            if response_items[i]['releaseDate']== None and response_items[i]['added']['date'] == Release_Date:
                    print("Glider:",response_items[i]['name'])
                    print("Rarity:",response_items[i]['rarity']['id'])
                    if response_items[i]['price'] == 0:
                        print ("Price: cannot be priced as it is a Battlepass/free/exclusive item","\n")
                    else:
                        print("Price:",response_items[i]['price'],"\n")
                        
            elif response_items[i]['releaseDate']== Release_Date:  
                print("Glider:",response_items[i]['name'])
                print("Rarity:",response_items[i]['rarity']['id'])
                if response_items[i]['price'] == 0:
                    print ("Price: cannot be priced as it is a Battlepass/free/exclusive item","\n")
                else:
                    print("Price:",response_items[i]['price'],"\n")
                    
                

 

#Test (for the funtions above):
#GetGlidersFromPrice(800)
#GetGlidersFromRarity("uncommon")
#GetGlidersFromReleaseDate("2022-05-29")
#GetEmotesFromPrice(500)
#GetEmotesFromRarity("rare")
#GetEmotesFromReleaseDate("2022-11-05")
#GetPickaxesFromPrice(800)
#GetPickaxesFromRarity("LeGnEdArY")
#GetPickaxesFromReleaseDate("2022-11-01")
#GetSkinsFromRarity("EpIc")
#GetSkinsFromPrice(800)
#GetSkinsFromReleaseDate("2022-08-16")
#GetEmoteReleaseDate("orange justice")
#GetEmoteRarity("orange justice")
#GetEmotePrice("orange justice")
#AllEmotes()
#GetSkinReleaseDate("carbide")
#GetSkinPrice("Carbide")
#GetSkinRarity("absolute zero")
#GetSkinRarity("john cena")
#AllPickaxes()
#AllGliders()
#AllOutfits()
#SkinRarity()