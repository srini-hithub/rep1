import os
import crypt

def addnewuser():

    uname=input("Select Username: ")
    upass=input("Select Password: ")

    #The encryption module seems to solve the obvious security leak,
    #but I still don't know whether even the exposed encrypted password is safe or not.
    ucrypt=crypt.crypt(upass,"123")
    os.system("useradd -m -p "+ucrypt+" "+uname)

addnewuser()
