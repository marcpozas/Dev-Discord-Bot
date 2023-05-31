import random

class GeneralCommands:
    """
    A class that contains general commands for handling unknown commands with different response types.
    """

    @staticmethod
    async def unknown_command(ctx, response_type):
        """
        Handle unknown commands based on the response type.

        Parameters:
            ctx (Context): The context object representing the command invocation.
            response_type (str): The type of response to handle.

        Returns:
            None

        Raises:
            None
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
        Send a random rude response message.

        Parameters:
            ctx (Context): The context object representing the command invocation.

        Returns:
            None

        Raises:
            None
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
        Send a default response message.

        Parameters:
            ctx (Context): The context object representing the command invocation.

        Returns:
            None

        Raises:
            None
        """
        responses = [
            'Comando incorrecto miau.'
        ]
        await ctx.send(random.choice(responses))
