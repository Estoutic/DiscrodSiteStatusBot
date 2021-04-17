import aiohttp
import ctx as ctx

from bot.Commands.Command import Command
from discord import Message


class Check(Command):
    async def execute(self, msg: Message):

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

    def get_name(self):
        return 'check'
