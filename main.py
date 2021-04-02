import aiohttp
import asyncio
import discord
import json
from discord.ext import commands

from config import settings

bot = discord.Client()
bot = commands.Bot(command_prefix=(settings['prefix']))


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command(name='check')
async def check(ctx: commands.Context):
    msg = ctx.message.content
    splitmessage = msg.split()
    url = splitmessage[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                guild = ctx.message.guild
                guild.id = 804421990508134430
                await guild.create_text_channel('ok')
            else:
                guild = ctx.message.guild
                guild.id = 804421990508134430
                await guild.create_text_channel('not ok')


@bot.command(name='start')
async def start(ctx):
    path = 'data.json'
    with open(path, 'r') as f:
        dat = json.loads(f.read())
        for i in dat['urls']['url']:
            neural = (i['first'])
    while True:
        async with aiohttp.ClientSession() as session:
            async with session.get(neural) as resp:
                if resp.status == 200:
                    print(1)
                else:
                    print(0)
        await asyncio.sleep(10)


@bot.command(name='add')
async def init(ctx: commands.Context):
    msg = ctx.message.content
    splits = msg.split()
    url = splits[1]
    file = 'data.json'
    with open(file, 'w') as f:
        json.dump(urls, f)
    # = json.loads(url)
    # with open('data.json') as data_file:


#     datan = json.loads(data_file)
#      datan['urls']['url'] = {'first': str(url)}
#   with open('data.json', 'w') as data_file:
#        json.dump(datan, indent=4)

# todos = json.loads(response.text)
@bot.command(name='gif')
async def createChannel(ctx, ):
    msg = ctx.message.content
    splits = msg.split()
    chnlname = splits[1]
    guild = ctx.message.guild
    guild.id = 804421990508134430
    await guild.create_text_channel(chnlname)


@bot.command(name='qwerty')
async def check(ctx: commands.Context):
    guild = bot.get_guild(804421990508134430)
    await guild.create_text_channel('ok')
    msg = ctx.message.content
    splitmessage = msg.split()
    url = splitmessage[1]
    category = 827507953912381440
    await guild.create_voice_channel('1', overwrites=None, category=category, reason=None)
    while True:

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    await discord.VoiceChannel.edit(guild, name="ok")

                else:
                    await discord.VoiceChannel.edit(guild, name="nope")
        await asyncio.sleep(10)


@bot.command(name='create')
async def setup_counter(ctx):
    try:
        guild = bot.get_guild(804421990508134430)
        await ctx.send("Setting up management!")
        category = await guild.create_category("Sites", overwrites=None, reason=None)
        await guild.create_voice_channel(f"Member Count: {guild.member_count}", overwrites=None, category=category,
                                         reason=None)
        await ctx.send("Setup finished!")
    except Exception as errors:
        print(f"Bot Error: {errors}")


@bot.command(name='kill')
async def killer(ctx):
    while True:
        await ctx.send("FUCK!!!!!!!!")


bot.run(settings['token'])
