import discord, os
from discord.ext import commands

client = commands.Bot(command_prefix='!')
token = os.getenv('token')

@client.event
async def on_ready():
	print(f'{client.user} is online.')

@client.command()
async def gethelp(ctx):
	emb=discord.Embed(title="How to Get Help",description=f"Post your explicit question in the appropriate channel and ping the corresponding role. For example, a math question should be posted in <#837876492276727808> with a <@&835678925643579404> ping.  Do not use <#835564615491518472> or other channels for questions—your question may be overlooked or forever lost.",color=0x62dfee)
	await ctx.reply(embed=emb)


client.run(token)
