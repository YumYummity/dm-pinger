# DM-pinger v0.3
Mass ping one of your friends.
For quick use, I recommend looking at the [latest release](https://github.com/YumYummity/dm-pinger/releases/latest) <br />
This was made for Windows. Feel free to fork it and make a Mac, Linux, or iOS version! (You could honestly just remove `Auto-detect accounts` and have the user manually input their token.) <br />

This program gets false detected by anti-malware, and VirusTotal returns 7 hits. **This program is not malware, it contains code to find tokens on your computer to automatically get accounts (feature #1), and *optional* webhook logging.**

# Disclaimer
Selfbotting is against Discord's TOS. This repository is a POC (proof of concept)!

# Features
- DM-pinger will automatically find discord accounts on your computer, so you can quickly spam your friend's DMs without getting your token
- DM-pinger includes optional webhook logging, including ETA, and amount pinged
- Auto-Stop when your ex-friend blocks you (this is probably the biggest risk, as long as you set a reasonable delay. I recommend 1.5 second delay)
- Modes! Choose from 5 different modes to spam ping your friend with.
- PyPresence! <br />
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

# To-Do
- Ping counter at bottom of ping text
- Custom message
- Fix "friend blocked" message when rate-limited

# Prompts
`A guide to all the prompts. Everything is caps-sensitive!` *Update soon about v0.3*

<details><summary> Show Prompts </summary>

- Account <br />
![image](https://user-images.githubusercontent.com/103061664/196053461-48526aa9-680d-46f2-9313-4b01a571f660.png) <br />
Choose an account from the list (the list includes every account found on your computer), or CustomToken. <br />
**This is caps-sensitive, and you must include the discriminator!** <br />

- Friend <br />
![image](https://user-images.githubusercontent.com/103061664/196053685-2ed6041f-02f4-4401-b746-12794d09a211.png) <br />
list of friends <br />
![image](https://user-images.githubusercontent.com/103061664/196053727-b9f1368a-36e4-4b96-8f40-043c2a90eaed.png) <br />
Choose a friend from the list (the list includes every account you are friends with. Does not include groups) <br />
**Again, this is caps-sensitive and you must include the discriminator!** <br />

- Webhook <br />
![image](https://user-images.githubusercontent.com/103061664/196053791-19ff3be1-c5d5-4145-af23-00413dc32e7e.png) <br />
Input a discord webhook link. Logs will be sent there! Input anything that's not a link for no logging.<br />
**Invalid links will cause an exception, and the script will reset** <br />
**Look at [Making a Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks#:~:text=%C2%A0%20Facebook-,MAKING%20A%20WEBHOOK,-With%20that%20in)** <br />

- Webhook Interval <br />
If you inputted a webhook: <br />
![image](https://user-images.githubusercontent.com/103061664/196053985-198e0e44-2737-46e2-b20f-b814f024a569.png) <br />
Input a number from 1-∞. Every time you ping your friend that many times, a log is sent to the webhook. <br />
**This option does not show up if you're not logging.** <br />
- Maximum Pings <br />
![image](https://user-images.githubusercontent.com/103061664/196054060-8412bbc4-af68-4a35-8833-980a6d6acecf.png) <br />
Input the amount of pings you want. <br />
- Ping Delay <br />
![image](https://user-images.githubusercontent.com/103061664/196054196-dc084b5e-2d94-4612-89be-a800e6285aeb.png) <br />
Input the delay you want between pings. <br />
**This was updated. The minimum delay is now 1.5**
*I recommend 1.5 for less pings, 7.5 if you're using it for more than an hour, and 20 if you're doing it overnight.*

</details>

**That's it! Your friend should be mass pinged!**

# Compiling
Set the variable 'EXE' to True in the code
**Make sure you have discord.py-self installed while compiling, and not discord.py**

# Crediting
You must credit me if you use this code anywhere else. More info in [LICENSE.md](https://github.com/YumYummity/dm-pinger/blob/main/LICENSE.md)
