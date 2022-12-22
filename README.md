# RedditUnsaveBot
This is a bot that will un-save all your saved posts! It supports multiple accounts and allows you to easily specify which account to use!
I made this because RedditManager is super annoying to work with and very slow.

## How to download:
  First navigate to the website https://www.reddit.com/prefs/apps 
  
  Then Create a bot, to do this scroll all the way to the bottom and click "create another app"
  
  ![create_another_app](https://user-images.githubusercontent.com/113136419/209192264-f2a83c72-20ea-4fd7-acc0-7099b4d309d7.PNG)
  
  Once you have created your app, select script and provide a name and description, for the about and redirect url just make it something like "http://localhost:8000"
  ![created app](https://user-images.githubusercontent.com/113136419/209192738-eb8e4488-d592-4141-b1e3-e3c3a0830e26.PNG)

  Now we can run the download script! Download(link to file) and run it using python3.
  
  Specify the name of the file, it can be anything you want. 
  Specify the Client Id next. We get this by going back to our reddit app and finding the first string 
  
  ![id](https://user-images.githubusercontent.com/113136419/209193593-026d537a-72b4-4bda-8753-94ceee22ddbd.PNG)
  
  Specify the Client Secret next, this is labled as "secret" 
  
  ![secret](https://user-images.githubusercontent.com/113136419/209193699-a8a1465d-013e-45b7-a4b5-2025d2dc4a3f.PNG)
  
  Then specify directory as prompted to.
  Finnally you can run the program it creates!

  
## Use case:
  To automatically remove mass amounts of saved posts easily, with the adddit benifit of not giving your account over/access to some third party

## Recommendations:
  This is best used with [BDFR](https://github.com/aliparlakci/bulk-downloader-for-reddit) as BDFR downloads all your saved posts and this bot removes them. You could create a batch file that runs BDFR and downloads all your posts, then removes all your posts with this bot :3
