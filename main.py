#!/usr/bin/env python3.8

import discord
import time
import asyncio
import logging as log
from sys import argv, exit
import getopt


try:
    optlist, args = getopt.getopt(argv[1:], "hst:", ["help", "discrete", "token"])
except getopt.GetoptError as e:
    log.error(e)
    exit(2)
for o, a in optlist:
    (supress := True) if o == "-s" else ()
    (usage()) if o in ("-h", "--help") else ()
    if o in ("-t", "--token"):
        token = a
    if o == "--discrete":
        discrete = True

try: bool(discrete)
except NameError: discrete = False

log.basicConfig(
    level=log.INFO,
    format="(%(levelname)s) %(asctime)s: %(message)s",
    datefmt="[%H:%M:%S]"
)

class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        discord.Client.__init__(self, **kwargs)
    
    async def on_ready(self):
        log.info("Succesfully logged in")
    
    async def mute_all(self):
        (exit(0)) if input("Proceed [Y/N]").capitalize() not in ("Y", "YES") else ()
        guilds = [i for i in client.fetch_guilds(limit=None)]
        print(guilds)
        
if __name__=="__main__":
    client = Client()
    loop = asyncio.get_event_loop()
    client_loop = loop.run_in_executor(None, client.start(token, bot=False))
    loop.run_until_complete(asyncio.ensure_future(client.mute_all(), loop=loop))
    time.sleep(1)
    asyncio.run(client.mute_all())
