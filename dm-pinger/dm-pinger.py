try:
    from requests import get
    from urllib.request import urlopen
    from random import uniform, choice
    from string import ascii_letters
    from os import system, listdir, getenv, mkdir, remove
    from os.path import exists, join
    from re import findall
    from shutil import copy2
    from win32crypt import CryptUnprotectData
    from json import loads
    try:
        from pypresence import AioPresence
    except:
        system('pip install -U pypresence')
        from pypresence import AioPresence
    from time import time
    from asyncio import sleep, get_event_loop
    try:
        from colorama import Fore, init, Back, Style
    except:
        system('pip install -U colorama')
        from colorama import Fore, init, Back, Style
    init()
    print(f'{Style.BRIGHT}')
    EXE = True #set to true when compiling
    notauto = False
    if not EXE:
        system('pip uninstall -y discord.py')
        system('pip install -U discord.py-self')
        from discord import Client, Forbidden, HTTPException
    elif EXE:
        from discord import Client, Forbidden, HTTPException
    else:
        raise TypeError('Not exe or not exe huh')
    try:
        from asyncio import sleep
    except:
        system('pip install -U asyncio')
        from asyncio import sleep
    from base64 import b64decode, b32decode
    try:
        from discordwebhook import Webhook, Embed
    except:
        system('pip install -U discordwebhook')
        from discordwebhook import Webhook, Embed
    try:
        from Crypto.Cipher import AES
    except:
        system('pip install -U pycryptodome')
        from Crypto.Cipher import AES
    system('cls')
    class gettokens:
        print(f'{Fore.GREEN} Please wait...')
        global abcdef
        abcdef = []
        def getMasterKey(self, path: str) -> str:
            copy2(path, join(self.temp, "ewerjwerjkn231rjkn"))
            with open(join(self.temp, "ewerjwerjkn231rjkn"), "r", encoding="utf-8") as file:
                localState = file.read()
            localState = loads(localState)
            masterKey = b64decode(localState["os_crypt"]["encrypted_key"])
            masterKey = masterKey[5:]
            masterKey = CryptUnprotectData(masterKey, None, None, None, 0)[1]
            remove(join(self.temp, "ewerjwerjkn231rjkn"))
            return masterKey
        def decryptValue(self, buff: str, masterKey: str) -> str:
            try:
                payload = buff[15:]
                cipher = AES.new(masterKey, AES.MODE_GCM, buff[3:15])
                return cipher.decrypt(payload)[:-16].decode()
            except BaseException:
                return ""
        def addTokenData(self, token: str) -> None:
            data = get('https://discordapp.com/api/v9/users/@me',
                    headers={"Authorization": token}).json()
            global abcdef
            abcdef = abcdef + [[f"{data['username']}#{data['discriminator']}", token]]
        def checkToken(self, token: str) -> str:
            if get("https://discord.com/api/v9/auth/login",
                headers={"Authorization": token}).status_code == 200:
                return True
            else:
                return False
        def getTokens(self) -> None:
            for _, path in self.paths.items():
                if not exists(path):
                    continue
                try:
                    if "discord" not in path:
                        for fileName in listdir(path):
                            if not fileName.endswith(
                                    ".log") and not fileName.endswith(".ldb"):
                                continue
                            for line in [
                                x.strip() for x in open(
                                    f'{path}\\{fileName}',
                                    errors='ignore').readlines() if x.strip()]:
                                for regex in (self.normalRegex):
                                    for token in findall(regex, line):
                                        if (self.checkToken(token)):
                                            if token not in self.tokens:
                                                self.tokens.append(token)
                    else:
                        if exists(join(self.appData, "discord", "Local State")):
                            for fileName in listdir(path):
                                if not fileName.endswith(
                                        ".log") and not fileName.endswith(".ldb"):
                                    continue
                                for line in [
                                    x.strip() for x in open(
                                        f'{path}\\{fileName}',
                                        errors='ignore').readlines() if x.strip()]:
                                    for y in findall(self.encryptedRegex, line):
                                        token = self.decryptValue(b64decode(y[:y.find('"')].split(
                                            'dQw4w9WgXcQ:')[1]), self.getMasterKey(join(self.appData, "discord", "Local State")))

                                        if (self.checkToken(token)):
                                            if token not in self.tokens:
                                                self.tokens.append(token)
                except BaseException:
                    pass
            for token in self.tokens:
                self.addTokenData(token)
            system('cls')
        def __init__(self) -> None:
            self.encryptedRegex = r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$]*"
            self.normalRegex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"
            self.appData = getenv("APPDATA")
            self.localAppData = getenv("LOCALAPPDATA")
            self.paths = {
                'Discord': self.appData + r'\\discord\\Local Storage\\leveldb\\',
                'Discord Canary': self.appData + r'\\discordcanary\\Local Storage\\leveldb\\',
                'Lightcord': self.appData + r'\\Lightcord\\Local Storage\\leveldb\\',
                'Discord PTB': self.appData + r'\\discordptb\\Local Storage\\leveldb\\',
                'Opera': self.appData + r'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
                'Opera GX': self.appData + r'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
                'Amigo': self.localAppData + r'\\Amigo\\User Data\\Local Storage\\leveldb\\',
                'Torch': self.localAppData + r'\\Torch\\User Data\\Local Storage\\leveldb\\',
                'Kometa': self.localAppData + r'\\Kometa\\User Data\\Local Storage\\leveldb\\',
                'Orbitum': self.localAppData + r'\\Orbitum\\User Data\\Local Storage\\leveldb\\',
                'CentBrowser': self.localAppData + r'\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
                '7Star': self.localAppData + r'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
                'Sputnik': self.localAppData + r'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
                'Vivaldi': self.localAppData + r'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
                'Chrome SxS': self.localAppData + r'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
                'Chrome': self.localAppData + r'\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
                'Epic Privacy Browser': self.localAppData + r'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
                'Microsoft Edge': self.localAppData + r'\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\',
                'Uran': self.localAppData + r'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
                'Yandex': self.localAppData + r'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
                'Brave': self.localAppData + r'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
                'Iridium': self.localAppData + r'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'}
            self.tokens = []
            self.temp = getenv("TEMP")
            self.mainId = "".join(
                choice(ascii_letters) for x in range(8))
            self.password = bytes("".join(
                choice(ascii_letters) for x in range(8)), encoding="utf-8")
            self.mainDirectory = join(self.temp, self.mainId)
            mkdir(self.mainDirectory)
            self.getTokens()

    if EXE:
        if notauto:
            print('\nHow to get your token: https://www.followchain.org/find-discord-token/')
            print('The token will not be used for anything other than spamming a friend.\n')
            token = input(f'{Fore.LIGHTBLUE_EX}TOKEN (exe version): {Fore.RESET}') #comment this for non exe version if u want
        else:
            gettokens()
            a = True
            f = False
            ab = False
            while a:
                for i in abcdef:
                    print(f'{Fore.GREEN}- ' + i[0])
                    print(f'{Fore.GREEN}- CustomToken')
                    if ab:
                        print(f'{Fore.RED}\n\nThat is not a account. Please include the discriminator, and use proper capitalization. (Example: User#0000)\nIf inputting a token, please use a valid token.')
                        ab = False
                    inputt = input(f'\n{Fore.LIGHTBLUE_EX}Please choose a account to use: {Fore.RESET}')
                    for x in abcdef:
                        if inputt  == str(x[0]):
                            a = False
                            token = x[1]
                            f = True
                            break
                    if not f:
                        if str(inputt) == 'CustomToken':
                            print('\nHow to get your token: https://www.followchain.org/find-discord-token/')
                            print('The token will not be used for anything other than spamming a friend.\n')
                            token = input(f'{Fore.LIGHTBLUE_EX}TOKEN (exe version): {Fore.RESET}')
                            def checkToken(token: str) -> bool:
                                if get("https://discord.com/api/v9/auth/login",
                                    headers={"Authorization": token}).status_code == 200:
                                    return True
                                else:
                                    return False
                            if checkToken(token):
                                def addTokenData(token: str) -> None:
                                    data = get('https://discordapp.com/api/v9/users/@me',
                                            headers={"Authorization": token}).json()
                                    global abcdef
                                    abcdef = abcdef + [[f"{data['username']}#{data['discriminator']}", token]]
                                addTokenData(token)
                                a = False
                                f = True
                            else:
                                ab = True
                        else:
                            ab = True
            
    print('Init done. Finished: modules and client.')

    class client(Client):
        async def on_connect(self):
            print(f'\n{Fore.GREEN}Successfully logged on as {self.user.name}#{self.user.discriminator}\n\n')
            a = True
            f = False
            ab = False
            while a:
                for i in self.user.friends:
                    print(f'{Fore.GREEN}- ' + str(i))
                if ab:
                    print(f'\n\n{Fore.RED}That is not a friend. Please include the discriminator, and use proper capitalization. (Example: User#0000)')
                    ab = False
                inputt = input(f'\n{Fore.LIGHTBLUE_EX}Please choose a friend to spam ping: {Fore.RESET}')
                for i in self.user.friends:
                    if inputt  == str(i):
                        a = False
                        inputt = i
                        f = True
                        break
                if not f:
                    ab = True
            webhookab = input(f'{Fore.LIGHTGREEN_EX}Webhook for logs. (OPTIONAL):{Fore.RESET} ')
            system('cls')
            try:
                weblogging = findall("((https?|ftp|gopher|telnet|file):((//)|(\\\\))+[\\w\\d:#@%/;$()~_?\\+-=\\\\\\.&]*)", webhookab)
                weblogging = weblogging[0]
                weblogging = True
            except:
                weblogging = False
            if weblogging:
                try:
                    intervalah = input(f'{Fore.LIGHTBLUE_EX}\nEvery _ many pings you want a log to be sent:{Fore.RESET} ')
                    intervalah = int(intervalah)
                    if intervalah == 0:
                        raise ZeroDivisionError('Interval cannot be 0.')
                except:
                    print(f'{Fore.RED}Invalid input. Using default 10.')
                    intervalah = 100
            else:
                intervalah = 1
            try:
                amount = input(f'\n{Fore.LIGHTBLUE_EX}How many maximum pings do you want to be sent?{Fore.RESET} ')
                amount = int(amount)
            except:
                print(f'{Fore.RED}Invalid input. Using default 1000.')
                amount = 1000
            try:
                delaya = input(f'\n{Fore.LIGHTBLUE_EX}How long between messages (in seconds)? Choose a value between 1.5-20.0, higher values is recommended for longer periods:{Fore.RESET} ')
                delaya = float(delaya)
                if delaya < 1.5 or delaya > 20:
                    raise TypeError('no not valid range')
            except:
                print(f'{Fore.RED}Invalid input. Using default 1')
                delaya = 1.5
            async def logs(dmn):
                if weblogging:
                    webhooka = Webhook(url=webhookab[0])
                    embed = Embed(title='Logging')
                    embed.set_footer(text='Logging')
                    try:
                        dmnao = int(dmn)
                    except:
                        dmnao = dmn
                    if type(dmnao) == int:
                        etaa = str(int((amount-int(dmnao))*delaya)) + ' seconds'
                        embed.add_field(name='Ping Counter', value=f'Pings: {dmn}\nETA: `{etaa}`')
                    else:
                        embed.add_field(name='Logs', value=f'{dmn}')
                    await webhooka.send_async(
                        username="Logs",
                        embed=embed
                    )
            pings = 0
            ra = delaya/14
            rb = delaya/8
            client_id = '1031332954670116914'
            RPC = None
            async def start(self):
                nonlocal pings
                nonlocal RPC
                print('Starting in 5 seconds!')
                await sleep(2.5)
                loop = get_event_loop()
                await sleep(2.5)
                RPC = AioPresence(client_id, loop=loop)
                await RPC.connect()
                eta = str(amount*delaya) + ' seconds'
                print(f'\nPinging started! ETA: {eta}\n')
                await logs(f'Pinging started! ETA: `{eta}`')
                # editing buttons is a violation of LICENSE.md
                buttons = [{"label": 'DM-Pinger', "url": "https://github.com/YumYummity/dm-pinger/releases/v0.1"}, {"label": "Github", "url": "https://github.com/YumYummity/dm-pinger/"}]
                picl = ['ping', 'ping1', 'ping2']
                start = time()
                pi = 0 #choose 0-2 for different images
                for p in range(amount):
                    try:
                        await inputt.send(f'{inputt.mention} ping')
                    except Forbidden:
                        return 'blocked'
                    except HTTPException:
                        return 'blocked'
                    pings = pings + 1
                    await RPC.update(state='Spamming my friend\'s DMs',details=f'Pings sent: {pings}', buttons=buttons,small_image=picl[pi],start=start)
                    sign = choice(['+', '-'])
                    evex = str(delaya) + str(sign) + str(uniform(ra, rb))
                    delayb = eval(evex)
                    print(f'Ping sent. Delay used: {delayb}')
                    await sleep(delayb)
                    async def divisible_by(x, y):
                        if (x % y) == 0:
                            return True
                        else:
                            return False
                    if (await divisible_by(pings, intervalah)):
                        await logs(pings)
                print('\n\nFinished sending pings!')
                await logs(f'Finished sending pings! `{pings}`')
                await sleep(20)
                await RPC.clear()
            t = await start(self)
            if t == 'blocked':
                await logs(f'Your friend blocked you! Pings sent: `{pings}`')
                print(f'{Fore.RED}Your friend blocked you! Pings sent: `{pings}`')
                await sleep(20)
                await RPC.clear()
    cl = client()
    cl.run(token)
except Exception as e:
    import traceback
    print(''.join(traceback.format_exception(e, e, e.__traceback__)))
    print('Something went wrong.')
