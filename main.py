from datetime import date
import datetime
from email import message
from unittest import result
from fontTools import configLogger
import matplotlib.pyplot as plt
from os import listdir
import json
import configparser

def getInstagramMessages(fileName):
    
    #creates the list of the files
    listOfFiles = listdir(fileName) #puts the names of the files in a list
    listOfFiles =[ x[8:-5] for x in listOfFiles ] #removes the charachers in the name of the files, to be able to sort
    listOfFiles = list(map(int, listOfFiles))
    listOfFiles.sort()
    listOfFiles = ["message_"+str(x)+".json" for x in listOfFiles] #recreates the name of the files in order

    listOfDates, listOfMessages = [], [] #initialize 2 lists, the first one remembers the date of the messages, and the second one remembers the numbers of messages in the day with the same index

    #gets the date of first message
    currentDate = None
    with open(fileName+"/"+listOfFiles[len(listOfFiles)-1], "r", encoding="utf8") as file: #open the last file that contains the first messages
        file = json.load(file) #convert the file to json
        message = file["messages"][len(file["messages"])-1] #gets the first message
        timeOfMessage = message["timestamp_ms"] #gets the time of the message
        timeOfMessage = date.fromtimestamp(int(timeOfMessage/1000)) #transforms the timestamp to date format and also removes the miliseconds from timestamp
        currentDate = timeOfMessage

    #gets the date of last message
    finalDate = None
    with open(fileName+"/"+listOfFiles[0], "r", encoding="utf8") as file: #open the file that contains the last messages
        file = json.load(file) #convert the file to json
        message = file["messages"][0] #gets the last message
        timeOfMessage = message["timestamp_ms"] #gets the time of the message
        timeOfMessage = date.fromtimestamp(int(timeOfMessage/1000)) #transforms the timestamp to date format and also removes the miliseconds from timestamp
        finalDate = timeOfMessage

    #creates an empty list of dates from the date of the first message to the date of the last message
    while currentDate <= finalDate:
        listOfDates.append(currentDate)
        currentDate = currentDate + datetime.timedelta(days=1)
        listOfMessages.append(0) #also creates a list of 0's which represents the number of messages in the day with the same index
 
    for i in listOfFiles: #itarate all the files in the folder of messages
        with open(fileName+"/"+i, "r", encoding="utf8") as instagram:
            instagram = json.load(instagram) #convert the file to json

            for line in instagram["messages"]: #itarates all the messages
                timeOfMessage = int(line["timestamp_ms"]) #gets the timestamp of message
                
                timeOfMessage = date.fromtimestamp(int(timeOfMessage/1000)) #transforms the timestamp to date format and also removes the miliseconds from timestamp
                listOfMessages[listOfDates.index(timeOfMessage)] += 1 #counts the number of messages of timeOfMessage
    
    #plt.plot(listOfDates, listOfMessages)
    #plt.xlabel("data")
    #plt.ylabel("numar de mesaje")
    #plt.show()

    return[listOfDates, listOfMessages]

def getTelegramMesasges(fileName):
    #open the file that containts the telegram messages data
    with open('telegram-messages/{}'.format(fileName), "r", encoding="utf8") as telegram:
        telegram = json.load(telegram)

        listOfDates, listOfMessages = [], [] #initialize 2 lists, the first one remembers the date of the messages, and the second one remembers the numbers of messages in the day with the same index

        #gets the date of first message
        message = telegram["messages"][0] #gets the first message
        timeOfMessage = message["date_unixtime"] #gets the time of the message
        timeOfMessage = date.fromtimestamp(int(timeOfMessage)) #transforms the timestamp to date format
        currentDate = timeOfMessage

        #gets the date of the last message
        message = telegram["messages"][len(telegram["messages"])-1] #gets the last message
        timeOfMessage = message["date_unixtime"] #gets the time of the message
        timeOfMessage = date.fromtimestamp(int(timeOfMessage)) #transforms the timestamp to date format
        finalDate = timeOfMessage

        #creates an empty list of dates from the date of the first message to the date of the last message
        while currentDate <= finalDate:
            listOfDates.append(currentDate)
            currentDate = currentDate + datetime.timedelta(days=1)
            listOfMessages.append(0) #also creates a list of 0's which represents the number of messages in the day with the same index

        for line in telegram["messages"]: #itarates all the messages
                timeOfMessage = int(line["date_unixtime"]) #gets the timestamp of message
                
                timeOfMessage = date.fromtimestamp(int(timeOfMessage)) #transforms the timestamp to date format and also removes the miliseconds from timestamp
                listOfMessages[listOfDates.index(timeOfMessage)] += 1 #counts the number of messages of timeOfMessage
    

        #plt.plot(listOfDates, listOfMessages)
        #plt.xlabel("data")
        #plt.ylabel("numar de mesaje")
        #plt.show()

        return[listOfDates, listOfMessages]

def getWhatsappMessages(fileName):
    with open('whatsapp-messages/{}'.format(fileName), "r", encoding="utf8") as whatsapp:
        whatsapp = whatsapp.readlines()

        listOfDates, listOfMessages = [], [] #initialize 2 lists, the first one remembers the date of the messages, and the second one remembers the numbers of messages in the day with the same index

        #gets the date of first message
        line = whatsapp[0].split() #reads the first line
        dateMessage = line[0].split(".") #transforms first element of message in time
        dateMessage[2] = dateMessage[2][:-1] #removes last element of year, to be a number
        dateMessage = list(map(int, dateMessage)) #convert time to int
        currentDate = date(dateMessage[2], dateMessage[1], dateMessage[0]) #date format

        #gets the date of the last message
        line = whatsapp[len(whatsapp)-1].split() #reads the last line
        dateMessage = line[0].split(".") #transforms first element of message in time
        dateMessage[2] = dateMessage[2][:-1] #removes last element of year, to be a number
        dateMessage = list(map(int, dateMessage)) #convert time to int
        finalDate = date(dateMessage[2], dateMessage[1], dateMessage[0]) #date format

        #creates an empty list of dates from the date of the first message to the date of the last message
        while currentDate <= finalDate:
            listOfDates.append(currentDate)
            currentDate = currentDate + datetime.timedelta(days=1)
            listOfMessages.append(0) #also creates a list of 0's which represents the number of messages in the day with the same index

        #starts to iterate the file
        for line in whatsapp:
            if line.isspace(): #checks if the line is empty
                continue
            line = line.split()
            
            if line[0][:2].isnumeric() and line[0][3:5].isnumeric() and line[0][7:11]: #check if the line is a message (message starts with a date, which is a number)
                dateMessage = line[0].split(".")           #transforms first element of message in time
                dateMessage[2] = dateMessage[2][:-1]       #removes last element of year, to be a number
                dateMessage = list(map(int, dateMessage))  #convert time to int
                timeOfMessage = date(dateMessage[2], dateMessage[1], dateMessage[0]) #date format

                listOfMessages[listOfDates.index(timeOfMessage)] += 1 #counts the number of messages of timeOfMessage

        # for i in range(len(listOfMessages)):
        #     print(listOfDates[i])
        #     print(listOfMessages[i])
        
        
        #plt.plot(listOfDates, listOfMessages)
        #plt.xlabel("data")
        #plt.ylabel("numar de mesaje")
        #plt.show()
        
        return [listOfDates, listOfMessages]

if __name__ ==  "__main__":

    config = configparser.RawConfigParser()
    config.read('config.ini')

    if config.getboolean('APPS', 'analyzeWhatsapp'):
        whatsappMessages = getWhatsappMessages(config['FILES']['nameOfWhatsappFile']) 
    else:
        whatsappMessages = [ [date.fromtimestamp(int(4092761509)), date.fromtimestamp(int(653004709))], [0, 0] ] #if the app is disabled it creates a list with *far away* dates that can't affect the data 

    if config.getboolean('APPS', 'analyzeInstagram'):
        instagramMessages = getInstagramMessages("instagram-messages")
    else:
        instagramMessages = [ [date.fromtimestamp(int(4092761509)), date.fromtimestamp(int(653004709))], [0, 0] ] #if the app is disabled it creates a list with *far away* dates that can't affect the data 

    if config.getboolean('APPS', 'analyzeTelegram'):
        telegramMessages = getTelegramMesasges(config['FILES']['nameOfTelegramFile'])
    else:
        telegramMessages = [ [date.fromtimestamp(int(4092761509)), date.fromtimestamp(int(653004709))], [0, 0] ] #if the app is disabled it creates a list with *far away* dates that can't affect the data 

    #if all the apps are disabled the program is closing
    if config.getboolean('APPS', 'analyzeWhatsapp') == False and config.getboolean('APPS', 'analyzeInstagram') == False and config.getboolean('APPS', 'analyzeTelegram') == False:
        print("all apps are disabled\ncheck config.ini")
        exit()

    #after the program receives all the data from the files, it will create two new lists:
    #1st list (listOfDates): will contain n elements, that represent the dates from the date of the first message (regardless of the application) to the date if the last message (regardless of the application)
    #2nd list (listOfMessages): will have n lists, which contain the number of messages from every app in the index that corresponds with the date of the messages

    #finds the date of the first message
    firstDay = min(whatsappMessages[0][0], 
                    instagramMessages[0][0], 
                    telegramMessages[0][0])

    #finds the date of the last message
    lastDay = max(
        whatsappMessages[0][-1],
        telegramMessages[0][-1],
        instagramMessages[0][-1]
    )

    listOfDates = []
    listOfMessages = []

    #creates an empty list of dates from the date of the first message to the date of the last message
    currentDate = firstDay 
    while currentDate <= lastDay: #iterates all the dates from the first to the last and appends them to the listOfDates
        listOfDates.append(currentDate)
        currentDate = currentDate + datetime.timedelta(days=1) #increases the date with a day
        #adds to the listOfMessages a list which will store the number of messages from every app
        #1st element: Whatsapp messages
        #2nd element: Instagram messages
        #3rd element: Telegram messages
        listOfMessages.append( [0,0,0] )

    #adds the number of messages from whatsapp to the corespondent collumn
    if config.getboolean('APPS', 'analyzeWhatsapp'):
        for i in range(len(whatsappMessages[0])):
            listOfMessages[listOfDates.index(whatsappMessages[0][i])][0] = whatsappMessages[1][i] #updates the number of messages in listOfMessages (1st position[0]) that corresponds with the date on i position in the whatsappMessages

    #adds the number of messages from instagram to the corespondent collumn
    if config.getboolean('APPS', 'analyzeInstagram'):
        for i in range(len(instagramMessages[0])):
            listOfMessages[listOfDates.index(instagramMessages[0][i])][1] = instagramMessages[1][i] #updates the number of messages in listOfMessages (2nd position[1]) that corresponds with the date on i position in the instagramMessages

    #adds the number of messages from telegram to the corespondent collumn
    if config.getboolean('APPS', 'analyzeTelegram'):
        for i in range(len(telegramMessages[0])):
            listOfMessages[listOfDates.index(telegramMessages[0][i])][2] = telegramMessages[1][i] #updates the number of messages in listOfMessages (3rd position[2]) that corresponds with the date on i position in the telegramMessages
    
    #creates a new csv file which will store all the data
    with open(config['FILES']['nameOfResultsFile']+".csv", "w", encoding="utf8") as results:
        results.write("date, whatsapp, instagram, telegram \n") #headers
        for i in range(len(listOfDates)):
            results.write(str(listOfDates[i]) + ", " + str(listOfMessages[i][0])  + ", " + str(listOfMessages[i][1]) + ", " + str(listOfMessages[i][2]) + "\n")
    
    print("completed")