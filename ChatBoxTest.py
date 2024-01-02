#import classes/functions
import random
#adds All functions from api.py
from api import *

def readQuery_introQ(splitString_introQ):

    #get the length of the sentence and store it in length variable 
    length_introQ = len(splitString_introQ)
    pos_response = {"That's great", "That's cool", "That's awesome"}
    neg_response = {"That's sad to hear but I hope your day gets better", "That's not cool, but I'm sure you'll have a better day tommorow", "I'm sorry to hear that but hopefully your day will get better"}
    
    pos_keyword = {"good", "great", "awesome", "fine", "not bad", "ok", "decent"}
    neg_keyword = {"bad", "could be better", "horrible", "annoying", "sad"}
   
    mutual_response = {"Speachless? let's get into it","ALright fair enough","Understadable","ok ok","Alright","Interesting","oh ok","hmmm right"}
        
    for x in range(length_introQ):
        if splitString_introQ[x].lower() in pos_keyword:
            print(random.choice(tuple(pos_response)))
           
        elif splitString_introQ[x].lower() in neg_keyword:
            print(random.choice(tuple(neg_response)))
        else:
            print(random.choice(tuple(mutual_response)))

#Function that asks the user if they know what they're doing. If they don't it will explain each cosmetic type on fortnite
def readQuery_knowledgeQ(splitString_knowledgeQ):
        
    #get the length of the sentence and stor it in length variable 
    length_knowledgeQ = len(splitString_knowledgeQ)
    
    pos_keyword = {"yes", "for sure", "definitely", "yh", "of course", "yeah", "I do"}
    neg_keyword = {"nah", "no", "nope", "no clue", "i don't", "not really", "don't"}

    pos_response = {"That's great", "That's cool", "That's awesome", "Nice!", "Perfect!"}
    neg_response = {"That's ok, I can help you with that \n", "No problem, let me tell you about all the stuff fortnite has to offer \n", "Really?, well let me give you an insight to what there is to offer! \n", "Let me tell you what we've got \n", "I can give you a quick runthrough on what there is to offer \n"}
    
    for x in range(length_knowledgeQ):
        if splitString_knowledgeQ[x].lower() in pos_keyword:
            print(random.choice(tuple(pos_response)))
        
        #If they don't know what they're looking for, it will explain each cosmetic type on fortnite
        elif splitString_knowledgeQ[x].lower() in neg_keyword:
            title_FN_cosmetics = "These are all the cosmetics types that are in fortnite \n"
            title_FN_cosmetics_center = title_FN_cosmetics.center(150)
            print(random.choice(tuple(neg_response)))
            print(title_FN_cosmetics_center)
            print("Gliders: Gliders resemble characteristics of a parachute. Exiting the Battle Bus is just one of many instances where you can use your glider. \n")
            print("Outfits/Skins: Outfits are Cosmetic items obtainable in Battle Royale and Save the World. They may be purchased with V-Bucks and earned through the Battle Pass or granted by some unique events or promotions. They are purely cosmetic and do not grant the player any competitive advantage. Outfits are usually referred to as “Skins” by the Playerbase.\n")
            print("Emotes: Emotes are dance moves or other actions your character can perform in Battle Royale and Save the World.\n")
            print("Harvesting tools/Pickaxes: Harvesting Tools (commonly referred as pickaxes) are items used in Battle Royale and Save the World to break structures and obtain wood, stone, and metal for building. They can also be used to damage other players; however, they are quite weak and only deal twenty damage per hit.\n")
        else:
            wrongInputStrings()
            #Ask user if they know what they're looking for
            knowledge_question = str(input("Do you know what you're looking for? "))

            #call the funcition to split the string into an array - Knowledge question
            splitString = stringBreaker(knowledge_question)

            #call the fuction to sort out what key words have been said - Knowledge question
            readQuery_knowledgeQ(splitString)

            
#function that breaks a string and put its into an array no matter the length
def stringBreaker(sentence):
    #take the inpuitted string and split it by space and add it to an array
     splitString = sentence.split()
     return(splitString)


def readQuery(splitString):

    #get the length of the sentence and store it in length variable 
    length = len(splitString)

    #for loop to  loop each word and check it against criteria
    for x in range(length):

        #if statement to check if they mentioned any key words and set them to lower to ensure that the casing is the same when checking the considition
        if(splitString[x].lower() == "glider" or splitString[x].lower() == "gliders"):
            
            checkIfTwoKeyWords(splitString,splitString[x]) #pass in the array and the word glider/gliders
            print("I've got you buddy, grip tight to your glider!\n")
            processGliderQuery() #go to the function that processes the glider queries

        elif(splitString[x].lower() == "pickaxe" or splitString[x].lower() == "pickaxes"):
            
            checkIfTwoKeyWords(splitString,splitString[x]) #pass in the array and the word pickaxe/pickaxes
            print("Alright buddy, swinging into the part\n")
            processPickaxeQuery() #go to the function that processes the pickaxe queries
            
        elif(splitString[x].lower() == "skin" or splitString[x].lower() == "skins"):
            
            checkIfTwoKeyWords(splitString,splitString[x]) #pass in the array and the word skin or skins
            print("No problem! Lets find you a new style for your next battle!\n")
            processSkinQuery() #go to the function that processes the skin queries

        elif(splitString[x].lower() == "emote" or splitString[x].lower() == "emotes"):
            
            checkIfTwoKeyWords(splitString,splitString[x])#pass in the array and the word emote/emotes
            print("Dancing our way towards that, Dont trip!\n")
            processEmoteQuery() #go to the function that processes the emote queries

    else: #If the user types the name of a cosmetic imstead of the type, it asks the user to do so
        print("I need to know if it's a skin, emote, pickaxe or glider")
        sentence = str(input("\nWhat are you looking for today: "))
        stringBreaker(sentence)
        splitString = stringBreaker(sentence)
        readQuery(splitString)



    

#Function to check if the user has entered more than 1 keyword as we can only search 1 at a time
def checkIfTwoKeyWords(splitString,keyWord):
    length = len(splitString)
    doubleKeyWord = False
    keyWordFound = False
    dispose_Word = []

    #function to remove all the words from the array before the key word that was found 
    for x in range(length):
        if(keyWordFound == False): 
            if(splitString[x] != keyWord): #if the word being looked at is not the keyword then add it to the dispose array 
                dispose_Word.append(splitString[x])
            #if the keyword is found also add it to the dispose array so we dont cause an error in the code below
            elif(splitString[x] == keyWord):
                dispose_Word.append(splitString[x])
                #check the length of the new dispose array
                length2 = len(dispose_Word)
                for x in range(length2): #loop the dispose array
                    currentDisposedWord = dispose_Word[x] #use the dispose array to get rid of the words before the key word in the real splitstring array
                    splitString.remove(currentDisposedWord)
                    if (x == length2 - 1): #used to end the loop so the words after the keyword are not removed
                        keyWordFound = True


    #check the length of the new array
    length = len(splitString)

    #if the length is 0 (array is empty) then put a filler into the array so the next part doesnt crash with an empty array.
    if(length == 0):
        splitString.append("Filler")


   
    #imbedded for loop to check if the user has entered more than 1 keyword
    for y in range(length):

        #if the second keyword is glider then make doublekeyword variable true
        if(splitString[y].lower() == "glider" or splitString[y].lower() == "gliders"):
            doubleKeyWord = True

        #if the second keyword is pickaxe then make doublekeyword variable true
        elif(splitString[y].lower() == "pickaxe" or splitString[y].lower() == "pickaxes"):
            doubleKeyWord = True
                    
        #if the second keyword is skin then make doublekeyword variable true
        elif(splitString[y].lower() == "skin" or splitString[y].lower() == "skins"):
            doubleKeyWord = True
                    
        #if the second keyword is emote then make the doublekeyword variable true
        elif(splitString[y].lower() == "emote" or splitString[y].lower() == "emotes" ):
            doubleKeyWord = True
            
    #if the variable is true then the user has entered 2 keywords so make them only enter 1 word
    if(doubleKeyWord == True ):
        sentence = str(input("\nBuddy looks like you are looking for more than one cosmetic at a time.\nPlease only enter one cosmetic so our battle bus can search for it: "))
        splitString = stringBreaker(sentence) # call the function that split the new sentence
        readQuery(splitString)  # call back this function to check for keywords again


#function that processes the skin queries
def processSkinQuery():
    #ask the user if they know the name of the skin they're looking for
    query = str(input("\nDo you know what fancy skin your looking for today? "))

    #split the string to see if the keyword is positve or negative
    splitString_query = stringBreaker(query)
    
    #find the length od the string that has been split
    splitString_query_length = len(splitString_query)

    #declare the key words that are going to be checked against
    pos_keyword = {"yes", "for sure", "definitely", "yh", "of course", "yeah", "I do"}
    neg_keyword = {"nah", "no", "nope", "no clue", "i don't", "not really", "don't"}

    #check if the user says something that is a key word relating to yes or no
    for x in range(splitString_query_length):
        if(splitString_query[x].lower() in pos_keyword ): #if its a positive keyword then search for the skin straight up
            skin_Search = input("\nOk,please enter the name of the skin you want to search for: ") #let the user search for the skin using the API
            print("Skin: " + skin_Search)
            GetSkinRarity(skin_Search)
            GetSkinReleaseDate(skin_Search)
            GetSkinPrice(skin_Search) 
            exitMessage()
            
        elif(splitString_query[x].lower() in neg_keyword ): #if it is a negative keyword then help search for the skin
           print("\nIt's all good! Peely is here to help! ")
           skinSearch() #call the function that searches for a skin
           exitMessage()
        
        else:
            wrongInputStrings()
            processSkinQuery() # call the fuction again to repeat the process 
            exitMessage()
    
def skinSearch():
    #ask the user if they know the price, rarity or date of the skin
   #forces the uses to input a valid value 
    while True:
        skin_query = str(input("\nDo you want to the price, rarity or release date of the skin? "))
        if skin_query.lower() == "price":
            break
        if skin_query.lower() == "rarity":
            break
        if skin_query.lower() == "date" or skin_query.lower() == "release":
            break
        if skin_query.lower() == "all":
            break
        print ("\nplease enter either PRICE, RARITY, RELEASE (DATE) (you can see all skins by typing ALL)")
    
    

    #split the string to see if the keyword 
    splitString = stringBreaker(skin_query)
    
    #find the length od the string that has been split
    splitString_Skin_Query_length = len(splitString)

     #for loop to  loop each word and check it against criteria
    for x in range(splitString_Skin_Query_length):

     #if statement to check if they mentioned any key words and set them to lower to ensure that the casing is the same when checking the condition
        if(splitString[x].lower() == "price"):
            print("\nOk ok ok")
            skin_Price = int(input("Could you tell me the price of the skins please? "))
            GetSkinsFromPrice(skin_Price) #function to search for skins by price (changed input from string to int and now works)
            exitMessage()

        elif(splitString[x].lower() == "rarity"):
            print("\nThe rarity of your skin does NOT improve your gameplay by the way! HA HA")
            skin_Rarity = str(input("Please enter the rarity of the skins: "))
            GetSkinsFromRarity(skin_Rarity)
            exitMessage()

        elif(splitString[x].lower() == 'release' or splitString[x].lower() == 'date') :
            skin_Date = str(input("Please enter the date the skins were released(YYYY-MM-DD): "))
            GetSkinsFromReleaseDate(skin_Date) #function to search for skins by release date
            exitMessage()
        else:
            #if they dont enter one of the key words then suggest to display all skins
            print("\nYou didn't enter the Price, Rarity or Release Date.")
            display_all = str(input("Should we open the supply drop and see all the skins instead? "))

            #declare the key words that are going to be checked agaianst
            pos_keyword = {"yes", "for sure", "definitely", "yh", "of course", "yeah", "I do"}
            

            if(display_all in pos_keyword):
                AllSkins()
                exitMessage()
            else:
                print("Ok, Back to the lobby!")
                exit()    
    


#function that processes the pickaxe queries
def processPickaxeQuery():
    #ask the user if they know the name of the pickaxe they're looking for
    query = str(input("\nDo you know what pickaxe you're looking for? "))

    #split the string to see if the keyword is positve or negative
    splitString_query = stringBreaker(query)
    
    #find the length od the string that has been split
    splitString_query_length = len(splitString_query)

    #declare the key words that are going to be checked against
    pos_keyword = {"yes", "for sure", "definitely", "yh", "of course", "yeah", "I do"}
    neg_keyword = {"nah", "no", "nope", "no clue", "i don't", "not really", "don't"}

    #check if the user says something that is a key word relating to yes or no
    for x in range(splitString_query_length):
        if(splitString_query[x].lower() in pos_keyword): #if its a positive keyword then search for the pickaxe straight up
            pickaxe_Search = str(input(("\nCool, could you tell me the name of the pickaxe? "))) #let the user search for the pickaxe using the API
            print("Pickaxe: " + pickaxe_Search)
            GetPickaxeRarity(pickaxe_Search)
            GetPickaxeReleaseDate(pickaxe_Search)
            GetPickaxePrice(pickaxe_Search)
            exitMessage()
            
        elif(splitString_query[x].lower() in neg_keyword): #if it is a negative keyword then help search for the pickaxe
           print("\nNo worries, we'll find it in no time ")
           pickaxeSearch() #call the function that searches for a pickaxe
           exitMessage()
        
        else:
            wrongInputStrings()
            processPickaxeQuery() # call the fuction again to repeat the process
            exitMessage()     

def pickaxeSearch():
    #ask the user if they know the price, rarity or date of the pickaxe
    
    while True:
        pickaxe_query = str(input("\nDo you want to the price, rarity or release date of the pickaxe? "))
        if pickaxe_query.lower() == "price":
            break
        if pickaxe_query.lower() == "rarity":
            break
        if pickaxe_query.lower() == "date" or pickaxe_query.lower() == "release":
            break
        if pickaxe_query.lower() == "all":
            break
        print ("\nplease enter either PRICE, RARITY, RELEASE (DATE) (you can see all pickaxes' by typing ALL)")

    #split the string to see if the keyword 
    splitString = stringBreaker(pickaxe_query)
    
    #find the length od the string that has been split
    splitString_pickaxe_Query_length = len(splitString)

     #for loop to loop each word and check it against criteria
    for x in range(splitString_pickaxe_Query_length):

     #if statement to check if they mentioned any key words and set them to lower to ensure that the casing is the same when checking the condition
        if(splitString[x].lower() == "price"):
            print("\nYou're trying to be cautious with how much you spend huh")
            pickaxe_Price = int(input("Please enter the price of the pickaxe: "))
            GetPickaxesFromPrice(pickaxe_Price)
            exitMessage()
        elif(splitString[x].lower() == "rarity"):
            print("\nOk")
            pickaxe_Rarity = str(input("Please tell me the rarity of the pickaxe "))
            GetPickaxesFromRarity(pickaxe_Rarity)
            exitMessage()
        elif(splitString[x].lower() == 'release' or splitString[x].lower() == 'date'):
            pickaxe_Date = str(input("Please enter the date the pickaxe was released(0000-00-00): "))
            GetPickaxesFromReleaseDate(pickaxe_Date)
            exitMessage()
        else:
            #if they dont enter one of the key words then suggest to display all pickaxes
            print("\nYou didn't enter the Price, Rarity or Release Date.")
            display_all = str(input("Would it be easier if I showed you all the pickaxes? "))
            
            #declare the key words that are going to be checked against
            pos_keyword = {"yes", "for sure", "definitely", "yh", "of course", "yeah", "I do"}

            if(display_all in pos_keyword ):
                AllPickaxes()
                exitMessage()
            else:
                print("Ok, Back to the lobby!")
                exit()    


#function that processes the emote queries
def processEmoteQuery():
    #ask the user if they know the name of the emote they're looking for
    query = str(input("\nDo you know what emote you're looking for? "))

    #split the string to see if the keyword is positve or negative
    splitString_query = stringBreaker(query)
    
    #find the length od the string that has been split
    splitString_query_length = len(splitString_query)

    #declare the key words that are going to be checked against
    pos_keyword = {"yes", "for sure", "definitely", "yh", "of course", "yeah", "I do"}
    neg_keyword = {"nah", "no", "nope", "no clue", "i don't", "not really", "don't"}

    #check if the user says something that is a key word relating to yes or no
    for x in range(splitString_query_length):
        if(splitString_query[x].lower() in pos_keyword): #if its a positive keyword then search for the pickaxe straight up
            emote_Search = str(input(("\nCool, could you tell me the name of the emote? "))) #let the user search for the emotes using the API
            print("Emote: "+ emote_Search)
            GetEmoteRarity(emote_Search)
            GetEmoteReleaseDate(emote_Search)
            GetEmotePrice(emote_Search)
            exitMessage()
            
        elif(splitString_query[x].lower() in neg_keyword): #if it is a negative keyword then help search for the emote
           print("\nNo worries, we'll find it in no time ")
           emoteSearch() #call the function that searches for a emote
           exitMessage()
        else:
            wrongInputStrings()
            processEmoteQuery() # call the fuction again to repeat the process
            exitMessage()     

def emoteSearch():
    #ask the user if they know the price, rarity or date of the emote release
    
    while True:
        emote_query = str(input("\nDo you want to the price, rarity or release date of the emotes? "))
        if emote_query.lower() == "price":
            break
        if emote_query.lower() == "rarity":
            break
        if emote_query.lower() == "date" or emote_query.lower() == "release":
            break
        if emote_query.lower() == "all":
            break
        print ("\nplease enter either PRICE, RARITY, RELEASE (DATE) (you can see all emotes by typing ALL)")
    #split the string to see if the keyword 
    splitString = stringBreaker(emote_query)
    
    #find the length od the string that has been split
    splitString_emote_Query_length = len(splitString)

     #for loop to loop each word and check it against criteria
    for x in range(splitString_emote_Query_length):

     #if statement to check if they mentioned any key words and set them to lower to ensure that the casing is the same when checking the condition
        if(splitString[x].lower() == "price"):
            print("\nYou're trying to be cautious with how much you spend huh")
            emote_Price = int(input("Please enter the price of the emote: "))
            GetEmotesFromPrice(emote_Price)
            exitMessage()
        elif(splitString[x].lower() == "rarity"):
            print("\nOk")
            emote_Rarity = str(input("Please tell me the rarity of the emote: "))
            GetEmotesFromRarity(emote_Rarity)
            exitMessage()
        elif(splitString[x].lower() == 'release' or splitString[x].lower() == 'date'):
            emote_Date = str(input("Please enter the date the emote was released(0000-00-00): "))
            GetEmotesFromReleaseDate(emote_Date)
            exitMessage()
        else:
            #if they dont enter one of the key words then suggest to display all emotes
            print("\nYou didn't enter the Price, Rarity or Release Date.")
            display_all = str(input("Would it be easier if I showed you all the emotes? "))

            #declare the key words that are going to be checked against
            pos_keyword = {"yes", "for sure", "definitely", "yh", "of course", "yeah", "I do"}
            
            if(display_all in pos_keyword):
                AllEmotes()
                exitMessage()
            else:
                print("Ok, Back to the lobby!")
                exit()    
    


# functions that processes the glider queries.
def processGliderQuery():
    #ask the user if they know the name of the glider they are looking for
    query = str(input("\nDo you know what glider your looking for today? "))

    #split the string to see if the keyword is positve or negitive
    splitString_query = stringBreaker(query)
    
    #find the length od the string that has been split
    splitString_query_length = len(splitString_query)

    #declare the key words that are going to be checked agaianst
    pos_keyword = {"yes", "for sure", "definitely", "yh", "of course", "yeah", "I do"}
    neg_keyword = {"nah", "no", "nope", "no clue", "i don't", "not really", "don't"}

    #check if the user says something that is a key word relating to yes or no
    for x in range(splitString_query_length):
        if(splitString_query[x].lower() in pos_keyword): #if its a positive keyword then search for the glider straight up
            glider_Search = str(input(("\nOk,please enter the name of the glider you want to search for: "))) #let the user search for the glider using the API
            print("Glider: "+ glider_Search)
            GetGliderRarity(glider_Search)
            GetGliderReleaseDate(glider_Search)
            GetGliderPrice(glider_Search)
            exitMessage()
            
        elif(splitString_query[x].lower() in neg_keyword): #if it is a negative keyword then help search for the glider
           print("\nIt's all good! jonsey is here to help! ")
           gliderSearch() #call the function that searches for a glider
           exitMessage()
        
        else:
            wrongInputStrings()
            processGliderQuery() # call the fuction again to repeat the process 
            exitMessage()



def gliderSearch():
    #ask the user if they know the price, rarity or chapter/season of the glider
    
    while True:
        glider_query = str(input("\nDo you want to the price, rarity or release date of the gliders? "))
        if glider_query.lower() == "price":
            break
        if glider_query.lower() == "rarity":
            break
        if glider_query.lower() == "date" or glider_query.lower() == "release":
            break
        if glider_query.lower() == "all":
            break
        print ("\nplease enter either PRICE, RARITY, RELEASE (DATE) (you can see all gliders by typing ALL)")

    #split the string to see if the keyword 
    splitString = stringBreaker(glider_query)
    
    #find the length od the string that has been split
    splitString_glider_Query_length = len(splitString)

     #for loop to loop each word and check it against criteria
    for x in range(splitString_glider_Query_length):

     #if statement to check if they mentioned any key words and set them to lower to ensure that the casing is the same when checking the condition
        if(splitString[x].lower() == "price"):
            print("\nYou're trying to be cautious with how much you spend huh")
            glider_price = int(input("Please enter the price of the glider: "))
            GetGlidersFromPrice(glider_price)
            exitMessage()
        elif(splitString[x].lower() == "rarity"):
            print("\nOk")
            glider_rarity = str(input("Please tell me the rarity of the glider: "))
            GetGlidersFromRarity(glider_rarity)
            exitMessage()
        elif(splitString[x].lower() == 'release' or splitString[x].lower() == 'date'):
            glider_Date = str(input("Please enter the date the glider was released(0000-00-00): "))
            GetGlidersFromReleaseDate(glider_Date)
            exitMessage()
        else:
    
            #if they dont enter one of the key words then suggest to display all gliders
            print("\nYou didn't enter the Price, Rarity or Release Date.")
            display_all = str(input("Would it be easier if I showed you all the gliders? "))

            #declare the key words that are going to be checked against
            pos_keyword = {"yes", "for sure", "definitely", "yh", "of course", "yeah", "I do"}
            
            if(display_all in pos_keyword):
                AllGliders()
                exitMessage() 
            else:
                print("Ok, Back to the lobby!")
                exit() 

#Procedure to just print a random message when the user enters the wrong input
def wrongInputStrings():
    wrong_Input_Message = {"Do you want to find your cosmetic?\n","We wont find your cosmetic with that reply\n","Even the Llamas dont understand what your trying to say!\n","Fishsticks is fustrated. He doesnt undersand what your saying.\n","Jonsey has a scar to his head! What are you trying to say?\n","ERROR 404: We dont understand\n","Try again, I cannot process your request\n","My small brain is stuggling with that input.\n" }

    print(random.choice(tuple(wrong_Input_Message)))

def exitMessage():
    answer = input("\nAre you satisfied without your findings? ")

    #split the string to see if the keyword is positve or negitive
    splitString_query = stringBreaker(answer)
    
    #find the length od the string that has been split
    splitString_query_length = len(splitString_query)

    #declare the key words that are going to be checked agaianst
    pos_keyword = {"yes", "for sure", "definitely", "yh", "of course", "yeah", "I do"}
    neg_keyword = {"nah", "no", "nope", "no clue", "i don't", "not really", "don't"}

    #check if the user says something that is a key word relating to yes or no
    for x in range(splitString_query_length):
        if(splitString_query[x].lower() in pos_keyword): #if its a positive keyword then end the program
           print("Thanks for visiting me! Back to the lobby!")
           exit()
            
        elif(splitString_query[x].lower() in neg_keyword): #if it is a negative keyword then restart the program
            print("\nIt's all good! jonsey is here to help! ")
           #ask the user what theyre looking for
            sentence = str(input("\nWhat are you looking for today: "))

            #call the funcition to split the string into an array
            splitString = stringBreaker(sentence)

            #function that filters what the user is looking for via the key words they have said
            readQuery(splitString)
        
        else:
            wrongInputStrings()
            exitMessage()


#----------------------------------------------MAIN----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ask the user how their day went
intro_question = str(input("What's up buddy, how's your day? "))

#call the funcition to split the string into an array
splitString = stringBreaker(intro_question)

#call the fuction to sort out what key words have been said
readQuery_introQ(splitString)


#Ask user if they know what they're looking for
knowledge_question = str(input("Do you know what you're looking for? "))

#call the funcition to split the string into an array - Knowledge question
splitString = stringBreaker(knowledge_question)

#call the fuction to sort out what key words have been said - Knowledge question
readQuery_knowledgeQ(splitString)

#ask the user what theyre looking for
sentence = str(input("\nWhat are you looking for today: "))

#call the funcition to split the string into an array
splitString = stringBreaker(sentence)

#function that filters what the user is looking for via the key words they have said
readQuery(splitString)