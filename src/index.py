import discord
from discord.ext import commands
import os
import re

from Commands.CinemaMaldaCommand import cinemamalda_info_with_images, cinemamalda_info_no_images, unknown_command, help_command
from Commands.InstagramCommand import stalk_instagram_profile, instagram_help_command
from Commands.NotifyCommand import notify_something
from Commands.catCommand import generate_cat

from Utils import Utils
from CustomHelpCommand import CustomHelpCommand

# We get the current script folder name
script_folder = os.path.split(os.path.abspath(__file__))[0]
folder_name = os.path.split(script_folder)[1]

intents = discord.Intents.default()
intents.message_content = True
MIAU_BOT = commands.Bot(command_prefix='!miau ', description='Testing BOT', intents=intents)

# Override the default help command with the custom help command
MIAU_BOT.help_command = CustomHelpCommand()

bot_activity='marcpozas.com'

# Commands
@MIAU_BOT.command(name='ping', description='Para checkear la latencia del BOT.')
async def ping(ctx):
    print('Ping command invoked')
    await ctx.send('pong')

@MIAU_BOT.command(name='horoscopo', description='Te da unas indicaciones astrológicas.')
async def horoscopo(ctx):
    await ctx.send('Espabila xd')

@MIAU_BOT.command(name='malda', description='API Cinema Malda.')
async def malda(ctx, argument=None, *args):
    if "fechas" in args:
        dates = True
    else:
        dates = False

    movie_limit = None
    for arg in args:
        match_num = re.search(r'\d+', arg)
        if match_num:
            movie_limit = int(match_num.group())
            break

    if argument == 'info':
        await cinemamalda_info_no_images(ctx=ctx, movie_limit=movie_limit if movie_limit else 100, dates=dates if dates else False)
    elif argument == 'cartel':
        await cinemamalda_info_with_images(ctx=ctx, movie_limit=movie_limit if movie_limit else 100, dates=dates if dates else False)
    elif argument == 'help':
        await help_command(ctx=ctx)
    else:
        await unknown_command(ctx=ctx)

@MIAU_BOT.command(name='stalk', description='Stalkeando por Instagram.')
async def stalk(ctx, username=None, max_posts=3):
    if username == 'help':
        await instagram_help_command(ctx=ctx)
    elif username != None:
        await stalk_instagram_profile(ctx=ctx, username=username, max_posts=max_posts)

@MIAU_BOT.command(name='cat', description='Retorna una foto o gif de gato.')
async def cat(ctx, *args):
    await generate_cat(ctx=ctx, args=args)

@MIAU_BOT.command(name='notify', description='El usuario envía una propuesta o bug.')
async def notify(ctx, *args):
    message = ' '.join(args) if args else ''
    await notify_something(ctx=ctx, message=message)

# Events
@MIAU_BOT.event
async def on_ready():
    await MIAU_BOT.change_presence(activity=discord.Game(name=bot_activity))
    print('MIAU_BOT is ready :3')

TOKEN = Utils.get_json(file=f'{folder_name}\\TOKEN.json')
MIAU_BOT.run(TOKEN['token'])