import os

import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run("ODU4NjM0NTQwNDgyMDM1NzMy.YNg_uw.MA34XKbMV8FTyAKj9mJ03eZ1MxQ ")