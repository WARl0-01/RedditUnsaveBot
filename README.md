# This is like very WIP and I'm going to get around to fixing this and making it more usable, I'm just busy
# read me is getting fixed as well
### Features planned:
1. Log file output
2. Restore from log file
3. Smoother transition between every 100 posts (current solution is brute force sorta)
4. Work on anti/mitigating rate limiting
5. Encrypt login info (yeah I know I should have done that forever ago...)
6. Like those things where you type -thing in the command and you can make it do stuff. I want the python run command to include an account thingy so you dont need to specify it after the program starts.
7. i forgor

# RedditUnsaveBot
This is a bot that allows you to easily remove all of your saved posts on Reddit. It supports multiple accounts, so you can choose which account you want to use. The main advantage of using this bot is that you don't have to give your account information to a third party. I am also very much an amateur and new to this whole github thingy

# THIS CODE STORES YOUR REDDIT PASSCODE(S) IN PLAINTEXT
### You gotta edit this horrendus code if you want any level of security
  Yeah, honestly I know... I'll find some way to encrypt the stuff later, I'm planning on that but just like, at the moment for me its not a priority, and if you have 2 factor it should be fine? I mean it's not like storing a token, just your login details. (which is silly to say becasuse a bunch of people use the same email and passcode so like if your stuff got leaked for this then a bunch of your accounts could be compromised.) Again sorry I'll fix this sometime in the future.

## How to download and use the bot:
1. Go to the website https://www.reddit.com/prefs/apps
  
2. Scroll to the bottom and click "create another app".
  
  ![create_another_app](https://user-images.githubusercontent.com/113136419/209197749-1e630349-cf59-4e70-b80e-0f49b1c1beee.PNG)
  
3. Fill out the form to create a new app. Make sure to select "script" as the type of app, and provide a name and description. For the "about url" and "redirect url", you can use something like "http://localhost:8000".
  
4. Once you have created your app, you will be given a "client id" and a "client secret". Make note of these, as you will need them later. Note that for the bot to work on any account it must be credited in the developer section of the bot page
  
  ![id and secret](https://user-images.githubusercontent.com/113136419/209197919-b5f34d2c-e5fe-4901-b17f-816e7a44dca6.PNG)
  

5. Find the newest version of the RedditUnsaveBot in the releases section of this repository. Download the bot and run it using Python 3.
  
6. When prompted, enter the name of the file that you want to save the bot as.
  
7. Enter the client id and client secret that you obtained in step 4.
  
8. Specify the directory where you want to save the bot.

9. Go to the file produced by the downloader and replace all occurences of \ n with \n. There will be four occurences in lines: 44, 45, 46, and 47
    Gonna be totally honest I just read this again (10/23/23, initial comit was like early this year, I have no clue why i wrote this but this must mean I really messed up on my downloader. I know my method of downloading was already horrendus but like, jeez. I think Im going to just upload the raw python file instead of trying to be fancy when I have no clue how :3 sorry.)
  
10. Once the setup is complete, you can run the bot by using the file that was created in step 6.
  
## Use case:
  This bot is useful for quickly removing a large number of saved posts. It can be used in conjunction with the Bulk Downloader for Reddit (BDFR) to first download all of your saved posts, and then remove them using this bot. To do this, you could create a batch file that runs BDFR to download all of your saved posts, and then runs this bot to remove them. This allows you to have a backup of your saved posts before deleting them.
