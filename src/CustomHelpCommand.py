from discord.ext import commands
import discord

class CustomHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        embed = discord.Embed(
            title="Bot Commands",
            description="Aquí se muestran los comandos disponibles.",
            color=discord.Color.blue()
        )

        for cog, commands in mapping.items():
            command_list = []
            for command in commands:
                command_info = f"`!miau {command.name}` - {command.description}"
                command_list.append(command_info)
            if command_list:
                embed.add_field(name='Categorías', value="\n".join(command_list), inline=False)
        
        embed.add_field(name='¿Cómo usar?', value="Para aprender a usar cada comando puedes utilizar `!miau [comando] help`\nPor ejemplo `!miau cat help`", inline=False)

        await self.get_destination().send(embed=embed)