from discord import Embed
from datetime import datetime
from discord.ext.commands import Cog
from discord.ext.commands import CommandNotFound
from discord.ext.commands import CommandOnCooldown


class pre(Cog):

    def __init__(self, client):
            self.client = client
    
    @Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, CommandNotFound):

            embed=Embed(title="Comando nao encontrado. consulte o comando help",
                        color=ctx.author.color,
                        timestamp=datetime.utcnow())

            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(embed=embed)

def setup(client):

    client.add_cog(pre(client))

    print("Log_erro carregado")
