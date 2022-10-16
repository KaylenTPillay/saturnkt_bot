from discord import Embed
from discord import Colour

class EventControllerMemberJoin:
    ''' This class controls the on_member_join event from discord '''

    def __init__(self, greeting_channel_name='general'):
        self.greeting_channel_name = greeting_channel_name

    async def handleEvent(self, member):
        channel_name = self.greeting_channel_name
        await self.__perform_greeting(channel_name, member)

    async def __perform_greeting(self, channel_name, member):
        channel = self.__get_greeting_guild_channel(channel_name, member)
        if (channel == None):
            return

        await channel.send(embed=self.__generate_welcome_embed_greeting(member.display_name))


    def __get_greeting_guild_channel(self, channel_name, member):
        guild_channels = member.guild.channels
        return next((channel for channel in guild_channels if channel.name == channel_name), None)

    def __generate_welcome_embed_greeting(slef, member_name):
        embed_colour = Colour.dark_purple()
        embed_title = 'Welcome to the Guild!'
        embed_description = f'Thanks for joining us {member_name}'

        embed_model = Embed(title=embed_title, description=embed_description, colour=embed_colour)
        return embed_model
