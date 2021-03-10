# GmailBruterV2 :dizzy:
 - **Simple Tool Written In Python3 To Perform Limited Brute-Force Attacks On Gmail Accounts.**


Table of Contents
=================

- [Installation](#installation)
- [CLI Commands](#cli-commands)
- [How To Create a Config?](#how-to-create-a-config)
- [When GmailBruter Creates a Successful Brute-Force Attack?](#when-gmailbruter-creates-a-successful-brute-force-attack)
- [What Should I Do If The SMTP Conncetion Disconnectes?](#what-should-i-do-if-the-smtp-connection-disconnects)
- [How To Execute a Shell Command?](#how-to-execute-a-shell-command)
- [How To Make a Successful Brute-Forcing Attack?](#how-to-make-a-successful-brute-forcing-attack)
- [What's New?](#whats-new)

<br>
## Installation
```
git clone https://github.com/DEMON1A/GmailBruterV2
cd GmailBruterV2
```
## CLI Commands
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

## When GmailBruter Creates a Successful Brute-Force Attack?
- @Alvin-22 did point out that. GmailBruter will only work only on accounts with "less secure apps" option enabled on your account. at the current time to protect your gmail account from brute-force attacks all you need to disable this option if it's enabled on your account. for full details about disabling "less secure apps" option. please follow this article: https://support.google.com/accounts/answer/6010255?hl=en

## What Should I Do If The SMTP Conncetion Disconnectes?
- You Should Wait Sometime Until You Get Unblock From Gmail SMTP. Or Use Any VPN But I Would Suggest Using VPNs While Brute-Forcing.
- Also, Don't Try a Lot Of Attemps On a Specefic Gmail Account. Even If You Got a Valid Password For It, Google Will Send a Waring Email Into Him/Her

## How To Execute a Shell Command?
- You Just Need To Add Your Command After `s-` For Example You Want To List The Files In The Current Directory. So You Gonna Add `ls` After `s-`, It Will Look Like This `s-ls`. Then The Program Will Return The Files In The Current Directory.

## How To Make a Successful Brute-Forcing Attack?
- I Did Increase The Attemps Of The Passowrd Brute-Force Here By Closing The Connection Everytime You Get *10* Bad Passwords. Then Create a New Conncetion. But That Isn't Gonna Help With Gmail That Much. You Have To Use a VPN Or Wait Sometime Between Every SMTP Server Disconnection. If You Kept Brute-Forcing Without STOP. Even If You Got The Valid Password Google Will Stop You And Send a Crtitcal Alert To The Account Owner. Telling Him To Change His Password.

## What's New?
- Fixing Some Issues With The Authentication
- Increasing The SMTP Login Attemps By ReCreating The Connection and Sleeping
- Shell Command Execution Using The Tool
- Loading Local Config To Aviod Adding The Same Setting Everytime.
- Solving Extra Spaces Issue By Replacing Them And Edit The Commands.
- Cleaner Code!
