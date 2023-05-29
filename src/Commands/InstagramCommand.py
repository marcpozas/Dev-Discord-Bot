import discord
import time

from APIs.InstagramAPI_v1_0.InstagramAPI import InstagramAPI

async def stalk_instagram_profile(ctx, username, max_posts:int=3):
    print(max_posts)
    # Use InstagramAPI module to fetch user data
    try:
        api = InstagramAPI(username=username)
    except:
        await ctx.channel.send('Instagram se ha rayado, dice que esperes unos minutos para intentarlo de nuevo.')
        return

    # Create the list of embeds
    embeds = []

    # Create an embed instance
    embed = discord.Embed(title=f'Instagram profile Info @{username}', description='Información del perfil', url=f'https://www.instagram.com/{username}/')

    # Add fields to the embed using the dictionary data
    embed.add_field(name="Biography", value=api.profile_data['biography'], inline=False)
    embed.add_field(name="Category Name", value=api.profile_data['category_name'], inline=False)
    embed.add_field(name="Followers", value=api.profile_data['followers'], inline=False)
    embed.add_field(name="Full Name", value=api.profile_data['full_name'], inline=False)
    embed.add_field(name="Has AR Effects", value=api.profile_data['has_ar_effects'], inline=False)
    embed.add_field(name="Has Channel", value=api.profile_data['has_channel'], inline=False)
    embed.add_field(name="Has Clips", value=api.profile_data['has_clips'], inline=False)
    embed.add_field(name="Has Guides", value=api.profile_data['has_guides'], inline=False)
    embed.add_field(name="Is Verified", value=api.profile_data['is_verified'], inline=False)
    embed.add_field(name="Posts count", value=api.profile_data['posts_count'], inline=False)
    embed.add_field(name="Seo categories", value=api.profile_data['seo_category_info'], inline=False)

    embeds.append(embed)

    for post_index in range(max_posts):

        skip_first, skip_second = True, True  # Flag variable to skip the first and second iteration

        caption = api.profile_data['posts'][post_index]['post_data']['caption']
        post_comments = api.profile_data['posts'][post_index]['post_data']['post_comments']
        post_likes = api.profile_data['posts'][post_index]['post_data']['post_likes']

        for post_data in api.profile_data['posts'][post_index]['post']:

            if skip_first and len(api.profile_data['posts'][post_index]['post']) > 1:
                skip_first = False
                continue  # Skip the first iteration

            # Create an embed instance
            embed = discord.Embed()

            if skip_second:
                skip_second = False
                # Add fields to the embed using the dictionary data
                embed.add_field(name="Caption: ", value=caption, inline=False)
                embed.add_field(name="Comments: ", value=post_comments, inline=False)
                embed.add_field(name="Likes: ", value=post_likes, inline=False)
                embed.title = f'Instagram Post {post_index+1} of @{username}'
                embed.url = f'https://www.instagram.com/p/{post_data["shortcode"]}/'

            if not post_data['is_video']:
                embed.set_image(url=post_data['display_url'])
            else:
                print(post_data['display_url'])
                embed.add_field(name="Video thumbnail: ", value=post_data['video_url'], inline=False)
                embed.set_image(url=post_data['display_url'])
                pass
        
            embeds.append(embed)

    # Send each embed in a separate message
    for embed in embeds:
        time.sleep(0.3)
        await ctx.channel.send(embed=embed)

async def instagram_help_command(ctx):
    embed = discord.Embed(title="!miau malda info")
    embed.add_field(name="Usage:", value="""
    `!miau malda {username} [max_posts]`

    **Arguments:**
    `!miau malda {username}`: Retorna la información del usuario y sus tres primeros posts.
    `!miau malda {username} 10`: Retorna la información del usuario y sus diez primeros posts.

    **Usage examples:**
    `!miau malda instagram`
    `!miau malda instagram 10`

    **Additional Info:**
    El valor default de posts es 3, y el máximo 12. Solo se permiten usuarios públicos.
    """, inline=False)

    await ctx.send(embed=embed)
