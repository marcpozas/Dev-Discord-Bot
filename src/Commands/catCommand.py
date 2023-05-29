import discord

from APIs.CataasAPI_v1_0.CataasAPI import CataasAPI

async def generate_cat(ctx, args):
    argument = ' '.join(args) if args else ' '

    options = ["-tag", "-gif", "-text", "-type", "-filter", "-width", "-height"]

    final_options = {}

    # Split the string into arguments based on the options
    current_option = ''
    for word in argument.split():
        
        if word in options:
            current_option = word
            final_options[current_option] = ''
        else:
            if current_option:
                final_options[current_option] = f"{(final_options[current_option] + ' ' + word).strip()}"
            else:
                if 'help' in args:
                    await help_command(ctx=ctx)
                    return
                elif 'tags' in args:
                    await get_tags(ctx=ctx)
                    return
                elif 'filters' in args:
                    await get_filters(ctx=ctx)
                    return
                elif 'types' in args:
                    await get_types(ctx=ctx)
                    return
                else:
                    await ctx.send('Comando incorrecto miau.')
                    return
    
    print(final_options)
    print(final_options.keys())

    if '-tag' not in final_options.keys():
        final_options['-tag'] = None
    if '-gif' not in final_options.keys():
        final_options['-gif'] = None
    else:
        final_options['-gif'] = 'gif'
    if '-text' not in final_options.keys():
        final_options['-text'] = None
    else:
        final_options['-text'] = final_options['-text'].replace(' ', '%20')
    if '-type' not in final_options.keys():
        final_options['-type'] = None
    if '-filter' not in final_options.keys():
        final_options['-filter'] = None
    if '-width' not in final_options.keys():
        final_options['-width'] = None
    if '-height' not in final_options.keys():
        final_options['-height'] = None

    print(final_options)
    
    api = CataasAPI(tag=final_options['-tag'], gif=final_options['-gif'], text=final_options['-text'], type_cat=final_options['-type'], filter_cat=final_options['-filter'], width=final_options['-width'], height=final_options['-height'])

    embed = discord.Embed(title="Cat", description="Cat generated", url=api.generated_cat)
    embed.set_image(url=api.generated_cat)

    await ctx.channel.send(embed=embed)

async def help_command(ctx):
    embed = discord.Embed(title="!miau cat info")
    embed.add_field(name="Usage:", value="""
    `!miau cat [options]`

    **Options:**
    `-tag [tag]`: Especifica la categoría del gato.
    `-gif`: Para recibir gif.
    `-text [text]`: Añade texto a la imagen.
    `-type [type]`: Tamaño imagen.
    `-filter [filter]`: Filtro que quieras.
    `-width [width]`: Ancho imagen.
    `-height [height]`: Altura imagen.

    **Usage examples:**
    `!miau cat`
    `!miau cat -tag cute -text Miau y eso uwu`
    `!miau cat -gif -text UaUaUaUa`
    `!miau cat -tag cute -width 1080 -height 600`

    **Datos adicionales:**
    `!miau cat tags`: Te dice los tags que existen.
    `!miau cat filtros`: Te dice los filtros que existen.
    `!miau cat types`: Te dice los filtros que existen.
    *Es incompatible utilizar -tag y -gif en el mismo comando.*
    """, inline=False)

    await ctx.send(embed=embed)

async def get_tags(ctx):
    api = CataasAPI(tag=None, gif=None, text=None, type_cat=None, filter_cat=None, width=None, height=None)

    tags_list = api.get_tags()

    part1 = ", ".join(tags_list[:len(tags_list) // 4])
    part2 = ", ".join(tags_list[len(tags_list) // 4: len(tags_list) // 2])
    part3 = ", ".join(tags_list[len(tags_list) // 2: 3 * len(tags_list) // 4])
    part4 = ", ".join(tags_list[3 * len(tags_list) // 4:])

    tags_tuple = (part1, part2, part3, part4)

    for tags in tags_tuple:
        await ctx.send(tags)


async def get_filters(ctx):
    api = CataasAPI(tag=None, gif=None, text=None, type_cat=None, filter_cat=None, width=None, height=None)
    await ctx.send(", ".join(api.get_filters()))

async def get_types(ctx):
    api = CataasAPI(tag=None, gif=None, text=None, type_cat=None, filter_cat=None, width=None, height=None)
    await ctx.send(", ".join(api.get_types()))