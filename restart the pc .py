import os
restart=input ("do you wish to restart your computer ?(yes/no):")
if restart =='no':
    exit()
else:
        os.system("shutdown /r /t 1")
