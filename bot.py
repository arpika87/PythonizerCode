import discord
from discord.ext import commands


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return


bot = commands.Bot(command_prefix='$')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

client.run('NTczNjkzMTk3NDk5MzY3NDM2.XMuo-Q.PmvhOq6nzSpXdT8KLI7897dQraU')
 