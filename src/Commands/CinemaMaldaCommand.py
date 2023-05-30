import discord
import time
import random

from APIs.CinemaMaldaAPI_v1_0.CinemaMaldaAPI import CinemaMaldaAPI

async def cinemamalda_info_with_images(ctx, dates:bool, movie_limit:int=3):
    """
    COMPLETE
    """
    # Use cinemaAPI module to fetch movie data
    api = CinemaMaldaAPI()
    movie_data = api.movie_data

    # Create the list of embeds
    embeds = []

    # Create each individual embed and add it to the list
    for movie in movie_data:
        if len(embeds) >= movie_limit:
            break

        if dates and movie['release_status'] in ['', 'Próximamente', 'Exclusivo para familias con bebés.']:
            continue

        embed = discord.Embed(title=movie['title'], description=f"Estado salida: {movie['release_status'] if movie['release_status'] != '' else '????'}", url=movie['href'])
        embed.set_image(url=movie['image_url'])
        embeds.append(embed)

    # Send each embed in a separate message
    for embed in embeds:
        time.sleep(0.3)
        await ctx.channel.send(embed=embed)

async def cinemamalda_info_no_images(ctx, dates:bool, movie_limit:int=3):
    """
    COMPLETE
    """
    # Use cinemaAPI module to fetch movie data
    api = CinemaMaldaAPI()
    movie_data = api.movie_data

    # Create the list of embeds
    embeds = []
    embed = discord.Embed(title='Cinema Malda Info Cartelera', description='Lista de películas', url='https://www.cinemamalda.com/')

    embed_size = 0

    # Create each individual embed and add it to the list
    for movie in movie_data:
        if embed_size >= movie_limit:
            break

        if embed_size % 5 == 0 and embed_size != 0:
            embed_size = 0
            embeds.append(embed)
            
            # Create an embed
            embed = discord.Embed(title='Cinema Malda Info Cartelera', description='Lista de películas', url='https://www.cinemamalda.com/')

        if dates and movie['release_status'] in ['', 'Próximamente', 'Exclusivo para familias con bebés.']:
            continue

        embed.add_field(name=movie['title'], value=f"Estado salida: {movie['release_status'] if movie['release_status'] != '' else '????'}\n{movie['href']}", inline=False)
        embed.add_field(name='\u2005', value='\u2005', inline=False)  # Add empty field for spacing

        embed_size += 1

    if len(embed) > 45:
        embeds.append(embed)

    # Send each embed in a separate message
    for embed in embeds:
        time.sleep(0.3)
        await ctx.channel.send(embed=embed)

# async def unknown_command(ctx):
#     """
#     COMPLETE
#     """
#     responses = [
#         '¿Qué? xd',
#         '¿Sabes escribir?',
#         '¿Sí o qué?',
#         '...',
#         'Casiii crack',
#         'Sisi lo que tú digas',
#         'Lo que tengo que aguantar...',
#         'Bro mira el mensaje antes de enviarlo',
#         'Ajá',
#         'Totalmente',
#         'Alt + F4 por favor :)'
#     ]
#     await ctx.send(random.choice(responses))

async def help_command(ctx):
    embed = discord.Embed(title="!miau malda info")
    embed.add_field(name="Usage:", value="""
    `!miau malda [info / cartel / help] [options]`

    **Arguments:**
    `!miau malda info`: Retorna la información de la cartelera sin imágenes.
    `!miau malda cartel`: Retorna la información de la cartelera con imágenes.
    `!miau malda help`: Información sobre el comando.

    **Options:**
    `!miau malda [info/cartel] fechas`: Retorna solo las películas con fecha
    `!miau malda [info/cartel] 10`: Retorna solo 10 películas

    **Usage examples:**
    `!miau malda cartel`
    `!miau malda cartel fechas`
    `!miau malda cartel fechas 20`
    """, inline=False)

    await ctx.send(embed=embed)
