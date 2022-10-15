import discord
import discord.ext.commands as bot
import asyncio
from event.memberjoin.controlmemberjoin import EventControllerMemberJoin

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = bot.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_member_join(member):
    ''' Greets a new member when they join the channel. '''

    controller = EventControllerMemberJoin()
    await controller.handleEvent(member)



@bot.command(name="valorant_stats")
async def _valorant_stats(context, *args):
    ''' Gets the users valorant stats. This command requires the users valorant username. '''

    # We are joining the args with a space between each item.
    # This will be seen as a single username when searching for the users stats.
    username = "SaturnKT#skt" # TODO: We need to get the users username

    # Construct URL: https://tracker.gg/valorant/profile/riot/{username}/overview
    await context.send(f'https://tracker.gg/valorant/profile/riot/{username}/overview')

bot.run('ADD_BOT_TOKEN')
