# GmailBruterV2 - Disabled
 - **Simple Tool Written In Python3 To Perform Limited Brute-Force Attacks On Gmail Accounts.**
 - It Turns Out That Gmail SMTP Is Adding Extra Layer Of Protection For Brute-Force Attacks. Even When You Have The Valid Password On Your Wordlist It Won't Allow You To Login That Will Flag Valid Results To Bad. I'm Sure All Of The Tools Suffers From The Same Issue. Until The New Update That Includes The Bypass I Will Mark This Tool As Disabled. So You Won't Waste Your Time With It Or With Any Other Tool.
 
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
- Solving Extra Spaces Issue By Replacing Them And Edit The Commands.

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

## What Should I Do If The SMTP Conncetion Disconnectes?
- You Should Wait Sometime Until You Get Unblock From Gmail SMTP. Or Use Any VPN But I Would Suggest Using VPNs While Brute-Forcing.
- Also, Don't Try a Lot Of Attemps On a Specefic Gmail Account. Even If You Got a Valid Password For It, Google Will Send a Waring Email Into Him/Her

## How To Execute a Shell Command?
- You Just Need To Add Your Command After `s-` For Example You Want To List The Files In The Current Directory. So You Gonna Add `ls` After `s-`, It Will Look Like This `s-ls`. Then The Program Will Return The Files In The Current Directory.

## How To Make a Successful Brute-Forcing Attack?
- I Did Increase The Attemps Of The Passowrd Brute-Force Here By Closing The Connection Everytime You Get *10* Bad Passwords. Then Create a New Conncetion. But That Isn't Gonna Help With Gmail That Much. You Have To Use a VPN Or Wait Sometime Between Every SMTP Server Disconnection. If You Kept Brute-Forcing Without STOP. Even If You Got The Valid Password Google Will Stop You And Send a Crtitcal Alert To The Account Owner. Telling Him To Change His Password.
