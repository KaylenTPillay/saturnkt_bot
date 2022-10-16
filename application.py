import discord
import discord.ext.commands as bot
import asyncio
from event.memberjoin.controlmemberjoin import EventControllerMemberJoin
from event.valorantassistent.controlvalorantassistent import EventControllerValorantAssistent

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = bot.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_member_join(member):
    ''' Greets a new member when they join the channel. '''

    controller = EventControllerMemberJoin()
    await controller.handle_event(member)



@bot.command(name="HeyCypher")
async def _valorant_assistent(context, *args):
    ''' Handles valorant queries '''

    controller = EventControllerValorantAssistent()
    await controller.handle_event(context, args)

bot.run('Add Bot TOKEN here')
