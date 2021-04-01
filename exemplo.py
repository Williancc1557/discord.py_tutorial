import discord

bot = discord.Bot(command_prefix='w!')



@bot.command()
async def teste(ctx):
    await ctx.send('olá mundo')



bot.run('token')