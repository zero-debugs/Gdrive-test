import os

class Creds():
    # ENTER Your bot Token Here
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    AUTH_CHANNEL = int(os.environ.get("AUTH_CHANNEL", -100))
    # Enter Your Mega email And Pass (Required)
    Mega_Email = os.environ.get("Mega_Email", "")
    Mega_pass = os.environ.get("Mega_pass", "")
    
    
    #  Make Sure You Are Providing both value if you need Teamdrive upload
    # Because of pydrive And pydrive v2 Api
    
    #Folder Id Of Teamdrive
    TEAMDRIVE_FOLDER_ID = os.environ.get("TEAMDRIVE_FOLDER_ID", None)
    
    # Id of Team drive 
    TEAMDRIVE_ID = os.environ.get("TEAMDRIVE_ID", None)
    
    
    
    #Example 
    #TG_TOKEN = "dkjfksdkffdkfdkfdj"
    #TEAMDRIVE_FOLDER_ID = "13v4MaZnBz-iEHlZ0gFXk7rh"
    #TEAMDRIVE_ID = "0APh6R4WVvguEUk9PV"
