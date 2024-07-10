# Currently this works fine, its just missing some features to be perfect
### Features planned:
1. Log file output
2. Restore saved posts from log file
3. Smoother transition between every 100 posts. [Find out why this is here](https://github.com/WARl0-01/RedditUnsaveBot/blob/main/BruteForceDownloading.txt)
4. ~~Work on anti/mitigating rate limiting~~ currently I have not seen this be an issue, but I will keep paying attention to it
5. Encrypt login info (yeah I know I should have done that forever ago...)
6. I want to add run commands to my program so you can specify which account you want to use in one command, I've seen some programs do stuff like this with -(something) at the end of their commands, I just need to research this and then impliment it

# RedditUnsaveBot
This is a bot that allows you to easily remove all of your saved posts on Reddit. It supports multiple accounts, so you can choose which account you want to use. The main advantage of using this bot is that you don't have to give your account information to a third party (and even though my bot isnt the best the third party solution is much worse, only removing posts by subreddit.)

# THIS CODE STORES YOUR REDDIT PASSCODE(S) IN PLAINTEXT
I understand that this is really bad, but I dont think its a huge issue for two reasons. One, any MFA will prevent this from being a major issue, and if someone tries to login but doesnt pass MFA reddit should still notify you anyways, so you can change your passwords. Two, depending on where you save this bot the passwords can be stored in a very obscure place, any password stealer finding it would have to search the entire system and also be able to recongnize different formats of passwords, instead of just looking in the same places and finding saved webbroswer logins that are consistantly formatted. I will eventually get around to encypting login info properly, for me I dont care if my reddit account is lost, I understand that you may not be the same. My apologies.

## How to download and use the bot:
1. Go to the website https://www.reddit.com/prefs/apps
  
2. Scroll to the bottom and click "create another app".
  
  ![create_another_app](https://user-images.githubusercontent.com/113136419/209197749-1e630349-cf59-4e70-b80e-0f49b1c1beee.PNG)
  
3. Fill out the form to create a new app. Make sure to select "script" as the type of app, and provide a name and description. For the "about url" and "redirect url", you can use something like "http://localhost:8000". Make sure you dont use any port you use if you are into selfhosting.
  
4. Once you have created your app, you will be given a "client id" and a "client secret". Make note of these, as you will need them later. Note that for the bot to work on any account it must be credited in the developer section of the bot page
  
  ![id and secret](https://user-images.githubusercontent.com/113136419/209197919-b5f34d2c-e5fe-4901-b17f-816e7a44dca6.PNG)
  

5. Find the newest version of the RedditUnsaveBot in the releases section of this repository. Download the bot and run it using Python 3

6. When prompted, enter the name of the file that you want to save the bot as.
  
7. Enter the client id and client secret that you obtained in step 4.
  
8. Specify the directory where you want to save the bot.

9. Go to the file produced by the downloader and replace all occurences of \ n with \n. There will be four occurences in lines: 44, 45, 46, and 47
    ~~Gonna be totally honest I just read this again (10/23/23, initial comit was like early this year, I have no clue why i wrote this but this must mean I really messed up on my downloader. I know my method of downloading was already horrendus but like, jeez. I think Im going to just upload the raw python file instead of trying to be fancy when I have no clue how :3 sorry.)~~ As of 7/10/24 I do not know if this is an issue. The reason this is an issue is because I have no clue how to do a proper, and nice, download aside from having a program that writes a new program line by line. I understand how hard it must be to look at this code, I am sorry.
  
10. Once the setup is complete, you can run the bot by using the file that was created in step 6.

10.5. When running the bot you will be told you need to add your account. You'll do this by creating a name that you will use to specify which account to work on, and adding your username and password. Again this is stored in plaintext, refer to my earlier comment about why I havent fixed this yet. Also the code is written in python by a beginner, its less then 100 lines. If you'd like to audit this code go ahead.
  
## Use case:
  This bot is useful for quickly removing a large number of saved posts. It can be used in conjunction with the Bulk Downloader for Reddit ([BDFR](https://github.com/aliparlakci/bulk-downloader-for-reddit)) to first download all of your saved posts, and then remove them using this bot. To do this, you could create a batch file that runs BDFR to download all of your saved posts, and then runs this bot to remove them. This allows you to have a backup of your saved posts before deleting them. This is what I do and why I made this bot. Note that currently a batch file will work, but you will have to specify which account to use meaning it wont be completely automated. I will add the modifier command thingies soon. I dont know what they are called but If you are using bdfr you'll see that you add a bunch of -(command)'s to each command to change how BDFR behaves. I am very excited to do this because I am lazy, but I also haven't done this because i'm lazy.
