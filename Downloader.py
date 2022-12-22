import os

#invput variables
DownloadName=input("Name of file: ")
ClientId=input("What is the client id?: ")
ClientSecret=input("What is the client secret?: ")

#get file download path
print("Which Directory Do you want to use?")
print('"Default" will create a subdirectory in the directory that this file is placed in and download the bot')
print('"Dump" will just throw the file in the current directory this is in, this is only recommended if it is already placed in the directory you want to use')

DirectoryCreationDone="False"
while DirectoryCreationDone=="False":
    DirectoryInput=input()

#create directory based off input
    if DirectoryInput=="Default":
        if not os.path.exists("UnsaveBot"): #check if directory exsits
            os.mkdir("UnsaveBot") #create directory if it does not exist
        os.chdir("UnsaveBot/") #change to directory
        DirectoryCreationDone="True"

    elif DirectoryInput=="Dump":
        print("File will be dumped in current directory")
        DirectoryCreationDone="True"
        #Code does not do anything with directories because it is being "dumped" into the current working directory

    else:
        print("String did not meet the required paramiters please try again")

#create bot file
FileHandler = open(DownloadName+".py", "w")

#write code!!
FileHandler.write(str("import praw"+"\n"))
FileHandler.write(str("import json"+"\n"))
FileHandler.write(str("from importlib import import_module"+"\n"))
FileHandler.write(str("import sys"+"\n"))
FileHandler.write(str("import os"+"\n"))
FileHandler.write(str("\n"))
FileHandler.write(str("# insert the logins directory into the system path to allow importing of login modules"+"\n"))
FileHandler.write(str("sys.path.insert(0, 'logins/')"+"\n"))
FileHandler.write(str("\n"))
FileHandler.write(str("# read the accounts list from the accounts.json file"+"\n"))
FileHandler.write(str('with open("logins/accounts.json", "r") as f:'+"\n"))
FileHandler.write(str("    accounts = json.load(f)"+"\n"))
FileHandler.write(str("\n"))
FileHandler.write(str("# initialize variables for the login prompt loop and unsave loop"+"\n"))
FileHandler.write(str("login_prompt_complete = False"+"\n"))
FileHandler.write(str("unsave_complete = False"+"\n"))
FileHandler.write(str("\n"))
FileHandler.write(str("# loop until a valid login is provided"+"\n"))
FileHandler.write(str("while not login_prompt_complete:"+"\n"))
FileHandler.write(str("    # ask the user to input the account name"+"\n"))
FileHandler.write(str('    account_input = input("Which account to use? (Must start with capital letter): ")'+"\n"))
FileHandler.write(str("\n"))
FileHandler.write(str("    # if the account name is in the accounts list, import the login module"+"\n"))
FileHandler.write(str("    if account_input in accounts:"+"\n"))
FileHandler.write(str("        Login = import_module(account_input)"+"\n"))
FileHandler.write(str("        login_prompt_complete = True"+"\n"))
FileHandler.write(str("    else:"+"\n"))
FileHandler.write(str("        # ask the user if they want to create a new account"+"\n"))
FileHandler.write(str('        print("Incorrect string, do you wish to make an account?")'+"\n"))
FileHandler.write(str('        make_new_account = input("y,n:")'+"\n"))
FileHandler.write(str("\n"))
FileHandler.write(str("        # if the user wants to create a new account"+"\n"))
FileHandler.write(str('        if make_new_account == "y":'+"\n"))
FileHandler.write(str("            # create the logins directory if it does not already exist"+"\n"))
FileHandler.write(str('            if not os.path.exists("logins"):'+"\n"))
FileHandler.write(str('                os.mkdir("logins")'+"\n"))
FileHandler.write(str("\n"))
FileHandler.write(str("            # create a new login file"+"\n"))
FileHandler.write(str('            FileHandler = open("logins/" + account_input + ".py", "w")  # Change the file extension to .py'+"\n"))
FileHandler.write(str("            # ask the user for their username and passcode"+"\n"))
FileHandler.write(str('            username_input = input("What is your username?: ")'+"\n"))
FileHandler.write(str('            passcode_input = input("What is your passcode?: ")'+"\n"))
FileHandler.write(str('            # write the login information to the file'+"\n"))

#syntax shinanigans, if you are trying to understand this I hope it hurts you as much as it did me writing it. sections corespond to the 5 file writing steps and require odd syntaxes to work properly
#section 1
FileHandler.write(str("            FileHandler.write(str('Username='+"))
FileHandler.write(str("'"))
FileHandler.write(str('"'))
FileHandler.write(str("'+(username_input)+'"))
FileHandler.write(str('"'))
FileHandler.write(str("'+"))
FileHandler.write(str('"\ n"))'+"\n"))

#section 2
FileHandler.write(str("            FileHandler.write(str('UserPassword='+'"))
FileHandler.write(str('"'))
FileHandler.write(str("'+(passcode_input)+'"))
FileHandler.write(str('"'))
FileHandler.write(str("'+"))
FileHandler.write(str('"\ n"))'+"\n"))

#section 3
FileHandler.write(str('            FileHandler.write(str(ClientId='+"'"+ClientId+"'"+'+"\ n"))'+"\n"))

#section 4
FileHandler.write(str('            FileHandler.write(str(ClientSecret='+"'"+ClientSecret+"'"+'+"\ n"))'+"\n"))

#section5
FileHandler.write(str("            FileHandler.write(str('UserAgent="))
FileHandler.write(str('"MassDelete"'))
FileHandler.write(str("'))"+"\n"))

FileHandler.write(str("            # close the file to save system resources"+"\n"))
FileHandler.write(str('            FileHandler.close()'+"\n"))
FileHandler.write(str())
FileHandler.write(str('            # use the credentials from the created file'+"\n"))
FileHandler.write(str('            Login = import_module(account_input)'+"\n"))
FileHandler.write(str('            login_prompt_complete = True'+"\n"))
FileHandler.write(str())
FileHandler.write(str('            # add the new account to the accounts list and write the updated list to the accounts.json file'+"\n"))
FileHandler.write(str('            accounts.append(account_input)'+"\n"))
FileHandler.write(str('            with open("logins/accounts.json", "w") as f:'+"\n"))
FileHandler.write(str('                json.dump(accounts, f)'+"\n"))
FileHandler.write(str('# create a Reddit instance using the specified login'+"\n"))
FileHandler.write(str('reddit = praw.Reddit('+"\n"))
FileHandler.write(str('    client_id=Login.ClientId,'+"\n"))
FileHandler.write(str('    client_secret=Login.ClientSecret,'+"\n"))
FileHandler.write(str('    password=Login.UserPassword,'+"\n"))
FileHandler.write(str('    user_agent=Login.UserAgent,'+"\n"))
FileHandler.write(str('    username=Login.Username,'+"\n"))
FileHandler.write(str(')'+"\n"))
FileHandler.write(str('#While all posts are not unsaved loop'+"\n"))
FileHandler.write(str('while unsave_complete==0:'+"\n"))
FileHandler.write(str("\n"))
FileHandler.write(str('    #Unsaves all saved items'+"\n"))
FileHandler.write(str('    for item in reddit.user.me().saved(limit=None):'+"\n"))
FileHandler.write(str('        reddit.submission(item.id).unsave()'+"\n"))
FileHandler.write(str("\n"))
FileHandler.write(str('    #If done unsaving stop loop'+"\n"))
FileHandler.write(str('    else: '+"\n"))
FileHandler.write(str('        unsave_complete=1'+"\n"))
FileHandler.write(str("\n"))
FileHandler.write(str('print("done")'+"\n"))