import discord

async def notify_something(ctx, message):
    with open(file='user_seggestions.txt', mode='a', encoding='UTF8') as f:
        f.write(message + '\n\n')

    await ctx.send('Notificación realizada!')

async def notify_help_command(ctx):
    embed = discord.Embed(title="!miau notify info")
    embed.add_field(name="", value="Este comando sirve para mandar un mensaje al developer.")
    embed.add_field(name="Usage:", value="""
    `!miau notify [message]`

    **Usage examples:**
    `!miau notify Sugiero implementar...`
    `!miau notify He encontrado un bug...`
    """, inline=False)

    await ctx.send(embed=embed)