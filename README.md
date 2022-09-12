# Analyze-messages-over-time

This project was build for educational purposes.

The purpose of this program is to visualize the evolution of messages with a person, by using the data from 3 apps: WhatsApp, Instagram and Telegram. The final output is a csv file that splits the number of messages in each app by the date. The exemple can be seen in the dataOfMessages.csv file.
After you get the .csv file, you can visualize/plot the data in a specific app (Tableau Public, Google Sheets, Microsoft Excel etc).

The input format of the files: 
All the files that are in the #-messages folders are for examples and need to be deleted.

By default, the scan for messages is enabled for all apps, if you want to disable or don't have messages from one of three apps, you need to disable the configuration in config.ini.

#Instagram

    Folder: instagram-messages

    The Instagram messages files can be downloaded from their platform.

    You need to drag and drop the files that can be found in the folder which contains your conversation with a person (downloaded from Instagram). Just the .json file/s needs to be in instagram-messages folder.

    !Can be one or multiple files in the folder

The Instagram folder can look in the both ways:

![instagram2](https://user-images.githubusercontent.com/22797278/189763641-02e93960-606b-42ad-aa6c-c86a512b1c0b.PNG)
![instagram1](https://user-images.githubusercontent.com/22797278/189763640-3372d7c0-8c42-42b6-8ab0-8151714cf4e9.PNG)


#Whatsapp
    
    Folder: whatsapp-messages
    
    The conversation with a person on Whatsapp can be downloaded from the WhatsApp app.
    
    Just drag and drop the .txt file in whatsapp-messages folder.
    
    !The .txt file needs to be named whatsapp.txt, otherwise change the file name in config.ini

WhatsApp folder:

![whatsapp](https://user-images.githubusercontent.com/22797278/189763895-4e1e6210-91a1-48b9-992e-4a5cf4d713ee.PNG)

#Telegram
    
    Folder: telegram-messages
    
    The conversation with a person on Telegram can be downloaded from Telegram Desktop app.
    
    Just drag and drop the .json file in telegram-messages folder.
    
    !You need to use the .json version of the conversation file
    
    !The .json file needs to be named result.json, otherwise change the file name in config.ini

Telegram folder:

![telegram](https://user-images.githubusercontent.com/22797278/189763922-d58fe1a5-bb59-4210-a4cb-b6296d0fac5d.PNG)

    
Example of plotted data: (Google Sheets)
![Example of plotted data](https://user-images.githubusercontent.com/22797278/189762866-70638a0b-1430-47fb-ba31-ef9234da1465.png)
