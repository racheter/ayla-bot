from discord import Embed, Member
from datetime import datetime
from typing import Optional
from random import randint, choice
from firebase_admin import db
from discord.ext.commands import Cog, command, guild_only, cooldown, BucketType


class jogos(Cog):

    def __init__(self, client):
        self.client = client

    @guild_only()
    @command()
    async def pay(self, ctx, target: Member = "null", sono: int = "null"):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/jogos")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config jogos ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            if (target == "null") or (sono == "null"):

                embed=Embed(title="Mencione e coloque o valor que deseja transferir",
                            color=ctx.author.color)

                await ctx.send(embed=embed)

            if sono <= 0:

                embed=Embed(title="Informe um valor superior a `0`",
                            color=ctx.author.color)

                await ctx.send(embed=embed)

            elif ctx.author.id == target.id:

                embed=Embed(title=f"Você não pode transferir para tu mesmo",
                            color=ctx.author.color)

                mag = await ctx.send(f"> {target.mention}", embed=embed)

            else:

                sonos = self.client.db.userglobal.find_one({"user_id": ctx.author.id})

                if (sonos["sonos"] - sono) < 1:

                    embed=Embed(title=f"Você não tem {sono} sonos, para transferir",
                                color=ctx.author.color)

                    await ctx.send(f"> {target.mention}", embed=embed)

                if (sonos["sonos"] - sono) >= 1:

                    embed=Embed(title=f"{ctx.author.name} esta transferir `{sono}` sonos, ao {target.name}",
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
                        self.client.db.userglobal.update_one({"user_id":ctx.author.id}, {"$inc":{"sonos": - sono}})

    @guild_only()
    @command()
    async def sono(self, ctx):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/jogos")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config jogos ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        else:

            embed=Embed(title="Sonooo",
                        color=ctx.author.color)

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @guild_only()
    @command()
    async def random(self, ctx, cmd: int = "null"):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/jogos")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config jogos ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            if cmd == "null":

                valor = randint(0, 100)

                embed=Embed(title="Randomizando um numero de `0` a `100`...",
                            color=ctx.author.color)

                embed.add_field(name=f"Numero da sorte ser `{valor}`",
                                value="Isso foi apenas um exemplo, coloque um valor\nExemplo: random `10`. saida imaginaria ser `6`",
                                inline=True)

                await ctx.send(embed=embed)

            else:

                valor = randint(0, cmd)

                embed=Embed(title=f"Numero da sorte ser `{valor}`",
                            color=ctx.author.color,)
                await ctx.send(embed=embed)

    @guild_only()
    @command()
    async def kiss(self, ctx, cmd: Optional[Member]):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/jogos")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config jogos ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            if cmd is None:

                embed=Embed(title="Mencione alguem para beijar e.e",
                        color=ctx.author.color)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            else:
                pessoa = cmd or ctx.author
                links = [
                        "https://cdn.discordapp.com/attachments/753391453052338226/756627543108354068/anime-kiss-1.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756627563828215848/anime-kiss-2.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756627609395265680/anime-kiss-4.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756627636389806201/anime-kiss-5.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756627660725157949/anime-kiss-6.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756627709148397597/anime-kiss-8.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756628452613816530/anime-kiss-34.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756628258447032430/anime-kiss-29.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756628132311859320/anime-kiss-25.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756628222409441453/anime-kiss-28.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756628028863414323/anime-kiss-23.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756628062799397054/anime-kiss-24.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756628290411954186/anime-kiss-30.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756628552291581962/anime-kiss-36.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756627935955517574/anime-kiss-16.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756627781332238488/anime-kiss-10.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756628838620069958/anime-kissin-3.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756629030559809556/anime-kissin-8.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756628807430963210/anime-kissin-2.gif",
                        "https://cdn.discordapp.com/attachments/753391453052338226/756628760484118528/anime-kissin-1.gif"
                        ]
                
                beijo1 = choice(links)
                
                embed=Embed(title=f"{ctx.author.name} beijou {pessoa.name}",
                            color=ctx.author.color,)

                embed.set_image(url=beijo1)
                
                mag = await ctx.send(f"{pessoa.mention}", embed=embed)

                await mag.add_reaction('🔃')

                def check(reaction, user):
                    return user == cmd and str(reaction.emoji) in ['🔃']

                reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=180.0)

                if reaction.emoji == '🔃':

                    beijo2 = choice(links)

                    embed=Embed(title=f"{pessoa.name} beijou {ctx.author.name}",
                            color=pessoa.color,)

                    embed.set_image(url=beijo2)

                    mag = await ctx.send(ctx.author.mention, embed=embed)

    @guild_only()
    @command()
    async def casar(self, ctx, target: Optional[Member]):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/jogos")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config jogos ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            user = self.client.db.userglobal.find_one({"user_id": ctx.author.id})

            if target is None:

                embed=Embed(title="Favor mencionar alguem para casar",
                            color=ctx.author.color,)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif target.id == ctx.author.id:

                embed=Embed(title="Você não pode, casar com você mesmo",
                            color=ctx.author.color,)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif target == self.client.user:

                embed=Embed(title="Ja estou em compromisso com meu serviço, sorry.",
                            color=ctx.author.color,)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif user["casal"] == target.id:

                embed=Embed(title="Os dois ja estão casados",
                        color=ctx.author.color,)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            else:

                if user["status"] == "solteiro":

                    embed=Embed(title=f"`{ctx.author.name}` esta pedindo a(o) `{target.name}` em casamento",
                                description="Para aceitar o casamento, reaja em ate `60s`",
                                color=ctx.author.color)

                    mag = await ctx.send(f"> {target.mention}", embed=embed)

                    await mag.add_reaction('✅')

                    def check(reaction, user):
                        return user == target and str(reaction.emoji) in ['✅']

                    reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=180.0)

                    if (reaction.emoji == '✅') and (reaction.message.id == mag.id):

                        await mag.delete()

                        embed=Embed(title=f"`{ctx.author.name}` e `{target.name}`, agora são casados",
                                description="Felicidades ao casal e tudo de bom.",
                                color=ctx.author.color)

                        await ctx.send(f"> {ctx.author.mention}", embed=embed)

                        self.client.db.userglobal.update_one({"user_id":ctx.author.id},
                                                            {"$set":{"status": target.name, "casal": target.id}})
                                                            
                        self.client.db.userglobal.update_one({"user_id":target.id},
                                                            {"$set":{"status": ctx.author.name, "casal": ctx.author.id}})

                else:

                    embed=Embed(title=f"`Ja esta casado(a)`{target.name}`",
                                color=ctx.author.color)
                    await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @guild_only()
    @command()
    async def divorciar(self, ctx, target: Optional[Member]):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/jogos")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config jogos ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            user = self.client.db.userglobal.find_one({"user_id": ctx.author.id})
            user2 = self.client.db.userglobal.find_one({"user_id": target.id})

            if target is None:

                embed=Embed(title="Favor mencionar ela ou ele para o divórcio",
                            color=ctx.author.color,)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            if target.id == ctx.author.id:

                embed=Embed(title="Você não casou com você mesmo",
                            color=ctx.author.color,)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            if user2["casal"] != ctx.author.id:

                embed=Embed(title=f"Você não esta casado com a(o) {target}",
                            color=ctx.author.color,)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            if target == self.client.user:

                embed=Embed(title="tu não casou comigo.",
                            color=ctx.author.color,)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            else:

                if user["status"] != "solteiro":

                    embed=Embed(title=f"{ctx.author.name} esta pedindo divócio a(o) {target.name}",
                                description="Para aceitar o divórcio, reaja em ate `60s`",
                                color=ctx.author.color)

                    mag = await ctx.send(f"> {target.mention}", embed=embed)

                    await mag.add_reaction('✅')

                    def check(reaction, user):
                        return user == target and str(reaction.emoji) in ['✅']

                    reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=180.0)

                    if (reaction.emoji == '✅') and (reaction.message.id == mag.id):

                        await mag.delete()

                        embed=Embed(title=f"{ctx.author.name} e {target.name}, se separaram",
                                description="Que triste que esse casal acabou.",
                                color=ctx.author.color)

                        await ctx.send(f"> {ctx.author.mention}", embed=embed)

                        self.client.db.userglobal.update_one({"user_id":ctx.author.id}, {"$set":{"status": "solteiro", "casal": "null"}})
                        self.client.db.userglobal.update_one({"user_id":target.id}, {"$set":{"status": "solteiro", "casal": "null"}})

def setup(client):

    client.add_cog(jogos(client))

    print("Jogos carregado")
