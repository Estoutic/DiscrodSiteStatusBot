from discord import Message
from discord.ext import commands


class Command:

    async def execute(self, msg: Message):
        ...

    def get_name(self):
        ...