from discord.ext.commands import Cog, command, CheckFailure, is_owner, guild_only
from discord import Embed, Member
from datetime import datetime, timedelta
from typing import Optional
from random import choice
import logging


class dono(Cog):

    def __init__(self, client):
        self.client = client

    @guild_only()
    @is_owner()
    @command()
    async def addsono(self, ctx, target: Member, sono: int):

        if target is None: return

        if sono is None: return

        else:

            embed=Embed(title=f"{ctx.author.name} esta a adicionar `{sono}` sonos, ao {target.name}",
                        color=ctx.author.color)

            mag = await ctx.send(f"> {target.mention}", embed=embed)

            await mag.add_reaction('✅')

            def check(reaction, user):
                return user == ctx.message.author and str(reaction.emoji) in ['✅']

            reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=180.0)

            if (reaction.emoji == '✅') and (reaction.message.id == mag.id):

                await mag.delete()

                embed=Embed(title=f"sucesso na ao adicionar",
                        color=ctx.author.color)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

                self.client.db.userglobal.update_one({"user_id":target.id}, {"$inc":{"sonos": + sono}})

    @guild_only()
    @is_owner()
    @command()
    async def addponto(self, ctx, target: Member, pont: int):

        if target is None: return

        if pont is None: return

        else:

            embed=Embed(title=f"{ctx.author.name} esta a adicionar `{pont}` pontos, ao {target.name}",
                        color=ctx.author.color)

            mag = await ctx.send(f"> {target.mention}", embed=embed)

            await mag.add_reaction('✅')

            def check(reaction, user):
                return user == ctx.message.author and str(reaction.emoji) in ['✅']

            reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=180.0)

            if (reaction.emoji == '✅') and (reaction.message.id == mag.id):

                await mag.delete()

                embed=Embed(title=f"sucesso na ao adicionar",
                        color=ctx.author.color)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":target.id}, {"$inc":{"ponto": + pont}})

    @guild_only()
    @is_owner()
    @command()
    async def sequestrar(self, ctx):

        links = [
                "https://cdn.discordapp.com/attachments/753391453052338226/756627543108354068/anime-kiss-1.gif"
                ]
        
        beijo1 = choice(links)
        
        embed=Embed(title=f"Miss foi sequestrada com sucesso",
                    color=ctx.author.color,)

        embed.set_image(url=beijo1)
        
        await ctx.send("> <@>", embed=embed)

    @sequestrar.error
    async def sequestrar_error(self, ctx, error):

        if isinstance(error, CheckFailure):

            embed=Embed(title="Acho que esse comando não existe e.e",
                        color=ctx.author.color,
                        timestamp=datetime.utcnow())

            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

def setup(client):

    client.add_cog(dono(client))

    print("Comandos ADM carregado")
