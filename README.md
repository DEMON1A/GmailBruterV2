# GmailBruterV2
 - **Simple Tool Written In Python3 To Perform Limited Brute-Force Attacks On Gmail Accounts.**
 
# Download And Run This Tool
```
git clone https://github.com/DEMON1A/GmailBruterV2
cd GmailBruterV2
python3 GmailBruterV2.py
```
# Commands
```
help -- To Show Help Message 
set target -- To Set The Victim Email Address
set time -- To Set Time Between Every 10 Faild Passwords
set list -- To Set PassList Name
show target -- To Show You Current Target
show time -- To Show You Current Time
show list -- The Show You Current List
start -- To Start Brute Force Attack
load -- Load Local Config For Settings

exit -- Close The Shell

s-{CMD} -- Executing Shell Command
```
# Usage
- Set The Target Address
- Set The Time Between Every 10 Fails
- Set The WordList
- Start The Brute Froce

# What's New?
- Fixing Some Issues With The Autnetication
- Increasing The SMTP Login Attemps By Closing The Connection And Sleeping
- More Cleaner Code.
- Shell Command Execution Using The Tool
- Loading Local Config To Aviod Adding The Settings Everytime

## How To Create a Config?
- It's Pretty Easy Here. You Just Need To Create a Local File Looks Like This:

```
email:{TARGET}
list:{LIST-PATH}
time:{TIME}
```

- Here's a Simple Example Of The Config

```
email:example@gmail.com
list:PassList.txt
time:10
```

## What Should I Do The SMTP Conncetion Disconnected
- You Should Wait Sometime Until You Get Unblock From Gmail SMTP. Or Use Any VPN But I Would Suggest Using VPNs While Brute-Forcing.
- Also, Don't Try a Lot Of Attemps On a Specefic Gmail Account. Even If You Got a Valid Password For It, Google Will Send a Waring Email Into Him/Her
