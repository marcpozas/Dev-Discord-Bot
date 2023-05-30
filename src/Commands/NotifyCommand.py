

async def notify_something(ctx, message):
    with open(file='user_seggestions.txt', mode='a', encoding='UTF8') as f:
        f.write(message + '\n\n')

    await ctx.send('Notificación realizada!')