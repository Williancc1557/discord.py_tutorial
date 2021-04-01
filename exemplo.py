import discord


#----------------- Prefixo -----------------------

bot = discord.Bot(command_prefix='w!')




# ----------------- Primeiro Comando -----------------------

@bot.command()
async def teste(ctx):
    await ctx.send('olá mundo')

    
    
    
# ----------------- Embed -----------------------
    
@bot.command()
async def embed(ctx):
    msg = discord.Embed(title='Olá mundo',
                        description=f'essa é a nossa descrição! executada pelo(a) {ctx.author}',
                        color=0x00FF00)
    await ctx.send(embed=msg)



bot.run('token')
