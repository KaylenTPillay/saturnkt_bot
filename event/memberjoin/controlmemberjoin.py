
class EventControllerMemberJoin:
    ''' This class controls the on_member_join event from discord '''

    def __init__(self, greeting_channel_name='general'):
        self.greeting_channel_name = greeting_channel_name

    async def handleEvent(self, member):
        await self.__perform_greeting(self.greeting_channel_name, member)
        # TODO: Ensure the member has the correct role.
        # TODO: Send the member a private message informing them of this bots commands

    async def __perform_greeting(self, channel_name, member):
        channel = self.__get_greeting_guild_channel(channel_name, member)
        if (channel == None):
            return

        await channel.send(f'Hello {member.display_name}!')

    def __get_greeting_guild_channel(self, channel_name, member):
        guild_channels = member.guild.channels
        return next((channel for channel in guild_channels if channel.name == channel_name), None)
