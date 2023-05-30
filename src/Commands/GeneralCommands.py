import random

class GeneralCommands:
    """
    COMPLETE
    """

    @staticmethod
    async def unknown_command(ctx, response_type):
        """
        COMPLETE
        """
        if response_type == 'rude':
            await GeneralCommands.rude_response(ctx=ctx)
        elif response_type == 'default':
            await GeneralCommands.default_response(ctx=ctx)
        else:
            pass

    @staticmethod
    async def rude_response(ctx):
        """
        COMPLETE
        """
        responses = [
            '¿Qué? xd',
            '¿Sabes escribir?',
            '¿Sí o qué?',
            '...',
            'Casiii crack',
            'Sisi lo que tú digas',
            'Lo que tengo que aguantar...',
            'Bro mira el mensaje antes de enviarlo',
            'Ajá',
            'Totalmente',
            'Alt + F4 por favor :)'
        ]
        await ctx.send(random.choice(responses))

    @staticmethod
    async def default_response(ctx):
        """
        COMPLETE
        """
        responses = [
            'Comando incorrecto miau.'
        ]
        await ctx.send(random.choice(responses))
