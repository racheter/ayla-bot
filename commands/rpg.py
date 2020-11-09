from discord.ext.commands import Cog, command, guild_only, cooldown, BucketType, CommandOnCooldown
from discord import Embed, Member
from lib.viajar import viajante
from asyncio import sleep
from firebase_admin import db
from datetime import datetime, timedelta
from typing import Optional
from random import randint, choice


class rpg(Cog):

    def __init__(self, client):
        self.client = client

    @guild_only()
    @command()
    async def classe(self, ctx):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            qual = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": ctx.author.id})

            if qual["classe"] == "sem classe":

                embed=Embed(title=f"{ctx.author.name}, esta sem classe. Use `classes` para ver os valores e vantagens",
                            color=ctx.author.color
                            )
                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            else:

                embed=Embed(title=f"{ctx.author.name}, sua classe ser `{qual['classe']}`,",
                            color=ctx.author.color)
                await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @guild_only()
    @command()
    async def classes(self, ctx):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            embed=Embed(title="Classes espacial:",
                        color=ctx.author.color,
                        )

            fields=[("1️⃣ `Viajante` Valor: 100 sonos", "Viaje 2 vez de acordo com sua sorte\nComando liberado: `viajarextra`", False),
                    ("2️⃣ `Explorador` Valor: 125 sonos", "Ganhe pontos extra ao `explorar` ou `observar`", False),
                    ("3️⃣ `FBI espacial` Valor: 150 sonos", "Imune a roubos e pune quem tenta o roubar\nComando liberado: `punir [pirata]`", False),
                    ("4️⃣ `Pirata espacial` Valor: 200 sonos", "Rouba até 100 pontos de outros jogadores no mesmo planeta que você\nComando liberado: `roubar [vitima]` ", False),
                    ]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            mag = await ctx.send(f"> {ctx.author.mention}", embed=embed)

            await mag.add_reaction('1️⃣')
            await mag.add_reaction('2️⃣')
            await mag.add_reaction('3️⃣')
            await mag.add_reaction('4️⃣')

            def check(reaction, user):
                return user == ctx.message.author and str(reaction.emoji) in ['1️⃣', '2️⃣', '3️⃣', '4️⃣']

            reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=120.0)
            qual = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": ctx.author.id})
            sonos = self.client.db.userglobal.find_one({"user_id": ctx.author.id})

            if (reaction.emoji == '1️⃣') and (reaction.message.id == mag.id):

                await mag.delete()

                if qual["classe"] == "Viajante":

                    embed=Embed(title=f"{ctx.author.name} já é classe `viajante`, não precisa comprar novamente",
                                color=ctx.author.color
                                )

                    await ctx.send(f"> {ctx.author.mention}", embed=embed)

                else:

                    menos = 100

                    if sonos["sonos"] < menos:

                        embed=Embed(title=f"{ctx.author.name} não tem sonos o suficiente para a compra da classe",
                                    color=ctx.author.color
                                    )

                        await ctx.send(f"> {ctx.author.mention}", embed=embed)

                    if sonos["sonos"] >= menos:

                        embed=Embed(title=f"{ctx.author.name} tem certeza que irá comprar a classe por `100` sonos ?",
                                    color=ctx.author.color,
                                    description="Tem de espera da resposta `30` segundos"
                                    )

                        mag = await ctx.send(f"> {ctx.author.mention}", embed=embed)

                        await mag.add_reaction('✅')

                        def check(reaction, user):
                            return user == ctx.message.author and str(reaction.emoji) in ['✅']

                        reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=30.0)

                        if (reaction.emoji == '✅') and (reaction.message.id == mag.id):

                            embed=Embed(title=f"{ctx.author.name} compra da classe com sucesso",
                                    color=ctx.author.color,
                                    )

                            await mag.edit(embed=embed)

                            self.client.db.userglobal.update_one({"user_id":ctx.author.id}, {"$inc":{"sonos": - 100}})
                            self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$set":{"classe": "Viajante"}})

            if (reaction.emoji == '2️⃣') and (reaction.message.id == mag.id):

                await mag.delete()
                menos = 125

                if qual["classe"] == "Explorador":

                    embed=Embed(title=f"{ctx.author.name} já é classe `Explorador`, não precisa comprar novamente",
                                color=ctx.author.color
                                )

                    await ctx.send(f"> {ctx.author.mention}", embed=embed)

                else:

                    if sonos["sonos"] < menos:

                        embed=Embed(title=f"{ctx.author.name} não tem sonos o suficiente para a compra da classe",
                                    color=ctx.author.color
                                    )

                        await ctx.send(f"> {ctx.author.mention}", embed=embed)

                    if sonos["sonos"] >= menos:

                        embed=Embed(title=f"{ctx.author.name} tem certeza que irá comprar a classe por `125` sonos ?",
                                    color=ctx.author.color,
                                    description="Tempo de espera da resposta `30` segundos"
                                    )

                        mag = await ctx.send(f"> {ctx.author.mention}", embed=embed)

                        await mag.add_reaction('✅')

                        def check(reaction, user):
                            return user == ctx.message.author and str(reaction.emoji) in ['✅']

                        reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=30.0)

                        if (reaction.emoji == '✅') and (reaction.message.id == mag.id):

                            embed=Embed(title=f"{ctx.author.name} compra da classe com sucesso",
                                    color=ctx.author.color,
                                    )

                            await mag.edit(embed=embed)

                            self.client.db.userglobal.update_one({"user_id":ctx.author.id}, {"$inc":{"sonos": - 125}})
                            self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$set":{"classe": "Explorador"}})
            
            if (reaction.emoji == '3️⃣') and (reaction.message.id == mag.id):

                await mag.delete()

                menos = 150

                if qual["classe"] == "FBI espacial":

                    embed=Embed(title=f"{ctx.author.name} já é classe `FBI espacial`, não precisa comprar novamente",
                                color=ctx.author.color
                                )

                    await ctx.send(f"> {ctx.author.mention}", embed=embed)

                else:

                    if sonos["sonos"] < menos:

                        embed=Embed(title=f"{ctx.author.name} não tem sonos o suficiente para a compra da classe",
                                    color=ctx.author.color
                                    )

                        await ctx.send(f"> {ctx.author.mention}", embed=embed)

                    if sonos["sonos"] >= menos:

                        embed=Embed(title=f"{ctx.author.name} tem certeza que irá comprar a classe por `150` sonos ?",
                                    color=ctx.author.color,
                                    description="Tempo de espera da resposta `30` segundos"
                                    )

                        mag = await ctx.send(f"> {ctx.author.mention}", embed=embed)

                        await mag.add_reaction('✅')

                        def check(reaction, user):
                            return user == ctx.message.author and str(reaction.emoji) in ['✅']

                        reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=30.0)

                        if (reaction.emoji == '✅') and (reaction.message.id == mag.id):

                            embed=Embed(title=f"{ctx.author.name} compra da classe com sucesso",
                                    color=ctx.author.color,
                                    )

                            await mag.edit(embed=embed)

                            self.client.db.userglobal.update_one({"user_id":ctx.author.id}, {"$inc":{"sonos": - 150}})
                            self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$set":{"classe": "FBI espacial"}})

            if (reaction.emoji == '4️⃣') and (reaction.message.id == mag.id):

                await mag.delete()
                menos = 200

                if qual["classe"] == "Pirata espacial":

                    embed=Embed(title=f"{ctx.author.name} já é classe `Pirata espacial`, não precisa comprar novamente",
                                color=ctx.author.color
                                )

                    await ctx.send(f"> {ctx.author.mention}", embed=embed)

                else:

                    if sonos["sonos"] < menos:

                        embed=Embed(title=f"{ctx.author.name} não tem sonos o suficiente para a compra da classe",
                                    color=ctx.author.color
                                    )

                        await ctx.send(f"> {ctx.author.mention}", embed=embed)

                    if sonos["sonos"] >= menos:

                        embed=Embed(title=f"{ctx.author.name} tem certeza que irá comprar a classe por `200` sonos ?",
                                    color=ctx.author.color,
                                    description="Tempo de espera da resposta `30` segundos"
                                    )

                        mag = await ctx.send(f"> {ctx.author.mention}", embed=embed)

                        await mag.add_reaction('✅')

                        def check(reaction, user):
                            return user == ctx.message.author and str(reaction.emoji) in ['✅']

                        reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=30.0)

                        if (reaction.emoji == '✅') and (reaction.message.id == mag.id):

                            embed=Embed(title=f"{ctx.author.name} compra da classe com sucesso",
                                    color=ctx.author.color,
                                    )

                            await mag.edit(embed=embed)

                            resultado = sonos - 200

                            self.client.db.userglobal.update_one({"user_id":ctx.author.id}, {"$inc":{"sonos": - 200}})
                            self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$set":{"classe": "Pirata espacial"}})

    @guild_only()
    @command()
    async def rank(self, ctx):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            embed=Embed(title="em breve...",
                        color=ctx.author.color,
                        )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @guild_only()
    @cooldown(1, 60*10, BucketType.member)
    @command()
    async def punir(self, ctx, cmd: Member):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            info = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": ctx.author.id})
            info2 = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": cmd.author.id})

            if info["classe"] == "FBI espacial":

                if cmd is None:

                    embed=Embed(title="Não tem como punir o além",
                                color=ctx.author.color,
                                )

                    await ctx.send(f"> {ctx.author.mention}", embed=embed)

                if cmd.id == ctx.author.id:

                    embed=Embed(title="Porque quer punir você mesmo ?.",
                                color=ctx.author.color,
                                )

                    await ctx.send(f"> {ctx.author.mention}", embed=embed)

                else:

                    if info["planeta"] == info2["planeta"]:

                        if info2["classe"] == "Pirata espacial":

                            if info2["planeta"] == "terra":

                                embed=Embed(title=f"{ctx.author.name} Jogou o(a) na lua {cmd.name} para refletir suas ações",
                                        color=ctx.author.color,
                                        )

                                await ctx.send(f"> {cmd.mention} punido(a)", embed=embed)

                                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":cmd.author.id}, {"$set":{"planeta": "Lua"}})

                            else:

                                embed=Embed(title=f"{ctx.author.name} Jogou o(a) na terra {cmd.name} para refletir suas ações",
                                        color=ctx.author.color,
                                        )

                                await ctx.send(f"> {cmd.mention} punido(a)", embed=embed)

                                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":cmd.author.id}, {"$set":{"planeta": "terra"}})

                        else:

                            embed=Embed(title=f"o {cmd.name}, não é um pirata espacial ou mafioso",
                                    color=ctx.author.color,
                                    )

                            await ctx.send(f"> {ctx.author.mention}", embed=embed)

                    else:

                        embed=Embed(title="È caçador ou caçadora de piratas ? viaje até chegar no planeta dele(a)",
                                color=ctx.author.color,)

                        await ctx.send(f"> {ctx.author.mention}", embed=embed)

            else:

                embed=Embed(title=f"{ctx.author.name} não ser FBI espacial para usar punir bandidos",
                            description="Veja as classes e seus valores com o comando `classes`",
                            color=ctx.author.color,)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @guild_only()
    @cooldown(1, 60*10, BucketType.member)
    @command()
    async def roubar(self, ctx, cmd: Member):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            info = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": ctx.author.id})
            info2 = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": cmd.author.id})

            if info["classe"] == "Pirata espacial":

                if cmd is None:

                    embed=Embed(title="Mencione a vitima da proxima vez",
                                color=ctx.author.color,
                                )

                    await ctx.send(f"> {ctx.author.mention}", embed=embed)

                if cmd.id == ctx.author.id:

                    embed=Embed(title="Se é meio doido tentando roubar você mesmo.",
                                color=ctx.author.color,
                                )

                    await ctx.send(f"> {ctx.author.mention}", embed=embed)

                else:

                    if info["planeta"] == info2["planeta"]:

                        if info2["classe"] == "FBI espacial":

                            embed=Embed(title="Você não pode roubar a lei e.e(usuario mencionado ser do FBI)",
                                color=ctx.author.color,
                                )

                            await ctx.send(f"> {ctx.author.mention}", embed=embed)

                        else:

                            gerado = randint(30, 100)
                            
                            if info2["ponto"] >= gerado:

                                embed=Embed(title=f"{ctx.author.name} roubou {gerado} pontos do {cmd.name}",
                                        color=ctx.author.color,
                                        )

                                await ctx.send(f"> {cmd.mention} roubado(a)", embed=embed)

                                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})
                                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":cmd.author.id}, {"$inc":{"ponto": - gerado}})

                            else:

                                embed=Embed(title="Falha no roubo, ou a pessoa nao tinha grana ou vc queria dms dela",
                                        color=ctx.author.color,
                                        )

                                await ctx.send(f"> {ctx.author.mention}", embed=embed)

                    else:

                        embed=Embed(title="Quer roubar alguem de outro planeta ? viaje até ele e.e",
                                color=ctx.author.color,
                                )

                        await ctx.send(f"> {ctx.author.mention}", embed=embed)

            else:

                embed=Embed(title=f"{ctx.author.name} não faz parte da clssse Pirata espacial para usar esse comando",
                            description="Veja as classes e seus valores com o comando `classes`",
                            color=ctx.author.color,
                            )

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @guild_only()
    @cooldown(1, 60*31, BucketType.member)
    @command()
    async def crime(self, ctx):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            gerado = randint(10, 99)
            sera = randint(0, 1000)
            frases = [
                "Invadiu o sistema da nasa e ganhou",
                "Vendeu uma bike roubada por",
                "Fez contagem de carta e ganhou",
                "Entrou nos esquema de piramete e faturou",
                "Invadiu uma casa e achou"
            ]
            frase = choice(frases)

            embed=Embed(title="Procurando algum crime..",
                            color=ctx.author.color,
                            )

            mag = await ctx.send(f"> {ctx.author.mention}", embed=embed)

            await sleep(2)

            if sera == 103:

                embede=Embed(title="Tentou roubar o racheter e perdeu tudo",
                            color=ctx.author.color,
                            )
                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$set":{"ponto": 0}})

            if sera == 200:

                embeda=Embed(title=f"Assaltou o sansek e ganhou um pão de queijo",
                            color=ctx.author.color,
                            )
                await mag.edit(embed=embeda)

            else:

                embeds=Embed(title=f"{frase} `{gerado}` pontos",
                            color=ctx.author.color,
                            )

                await mag.edit(embed=embeds)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

    @guild_only()
    @command()
    @cooldown(1, 60*5, BucketType.member)
    async def observar(self, ctx):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            qual = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": ctx.author.id})

            if qual["classe"] == "Explorador":

                gerado = randint(8, 15)

                embed=Embed(title=f"Observando o céu",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(f"> {ctx.author.mention}", embed=embed)

                embede=Embed(title=f"Observando o céu...",
                            color=ctx.author.color,
                            )

                await mag.edit(embed=embede)

                await sleep(2)

                embeda=Embed(title=f"Uauu olhou as estrelas e ganhou {gerado} pontos",
                            color=ctx.author.color,
                            )
                embed.set_footer(text="Por ser um explorador ganhou pontos a mais")

                await mag.edit(embed=embeda)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"pontos": + gerado}})

            else:

                gerado = randint(5, 10)

                embed=Embed(title=f"Observando o céu..",
                            color=ctx.author.color,
                            )
                mag = await ctx.send(f"> {ctx.author.mention}", embed=embed)

                await sleep(2)

                embeda=Embed(title=f"Uauu olhou as estrelas e ganhou {gerado} pontos",
                            color=ctx.author.color,
                            )
                await mag.edit(embed=embeda)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"pontos": + gerado}})

    @guild_only()
    @command()
    async def raridade(self, ctx):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            embed=Embed(title="Raridades:",
                        color=ctx.author.color,
                        )

            embed.set_footer(text="Falha ao viajar de probabilidade de 11.75%")

            fields=[("Saturno `#1`", "Viajar até `saturno` ser **lendario** com probabilidade de `0.25%`", False),
                    ("Júpiter `#2`", "Viajar até `Júpiter` ser **épico** com probabilidade de `0.50%`", False),
                    ("Netuno `#3`", "Viajar até `Netuno` ser **épico** com probabilidade de `0.75%`", False),
                    ("Tita `#4`", "Viajar até `Tita` ser **épico** com probabilidade de `1%`", False),
                    ("Vênus `#5`", "Viajar até `Vênus` ser **épico** com probabilidade de `1.25%`", False),
                    ("Éris `#6`", "Viajar ate `Éris` ser **épico** com probabilidade de `1.50%`", False),
                    ("Ceres `#7`", "Viajar até `Ceres` ser **raro** com probabilidade de `1.75%`", False),
                    ("Europa `#8`", "Viajar até `Europa` ser **raro** com probabilidade de `2%`", False),
                    ("Urano `#9`", "Viajar até `Urano` ser **raro** com probabilidade de `2.50%`", False),
                    ("Marte `#10`", "Viajar até `Marte` ser **raro** com probabilidade de `3.75%`", False),
                    ("Makemake `#11`", "Viajar ate `Makemake` ser **raro** com probabilidade de `5%`", False),
                    ("Calisto `#12`", "Viajar até `Calisto` ser **incomum** com probabilidade de `5.25%`", False),
                    ("Mercúrio `#13`", "Viajar até `Mercúrio` ser **incomum** com probabilidade de `5.50%`", False),
                    ("Encélado `#14`", "Viajar até `Encélado` ser **incomum** com probabilidade de `6%`", False),
                    ("Miranda `#15`", "Viajar até `Miranda` ser **incomum** com probabilidade de `6.25%`", False),
                    ("Fobos `#16`", "Viajar até `Fobos` ser **incomum** com probabilidade de `7%`", False),
                    ("Haumea `#17`", "Viajar até `Haumea` ser **comum** com probabilidade de `8%`", False),
                    ("Plutão `#18`", "Viajar até `Plutão` ser **comum** com probabilidade de `9%`", False),
                    ("Lua `#19`", "Viajar até `Lua` ser **comum** com probabilidade de `10%`", False),
                    ("terra `#20`", "Viajar até `terra` ser **comum** com probabilidade de `11%`", False),
                    ]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @guild_only()
    @command()
    async def tudo(self, ctx):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            pontosp1 = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": ctx.author.id})

            zero = 100

            if pontosp1["ponto"] < zero:

                embed=Embed(title=f"Você precisa de `100` pontos, pelo menos para jogar no tudo ou nada",
                    color=ctx.author.color,
                    )

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif pontosp1["ponto"] >= zero:

                embed=Embed(title=f"Você está prestes a apostar todos seus `{pontosp1['ponto']}` pontos.",
                        description="Ao ganhar fica com o dobro de pontos\nNão nos culpe se perder **tudo** por azar",
                        color=ctx.author.color)

                embed.add_field(name=f"Esperando resposta do(a) `{ctx.author.name}`", value="Reaja ao ✅ para aceitar")

                mag = await ctx.send(f"> {ctx.author.mention}", embed=embed)
                await mag.add_reaction('✅')

                def check(reaction, user):
                    return user == ctx.message.author and str(reaction.emoji) in ['✅']

                reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=40.0)

                if (reaction.emoji == '✅') and (reaction.message.id == mag.id):

                    await mag.delete()

                    random1 = randint(12, 13)

                    if random1 == 12:

                        embed=Embed(title=f"O {ctx.author.name} perdeu Tudo",
                                color=ctx.author.color,
                                )

                        await ctx.send(f"> {ctx.author.mention}", embed=embed)

                        self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": - pontosp1["ponto"]}})

                    if random1 == 13:

                        embed=Embed(title=f"O {ctx.author.name} ganhou Tudo",
                                color=ctx.author.color,
                                )

                        await ctx.send(f"> {ctx.author.mention}", embed=embed)

                        self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + pontosp1["ponto"]}})

    @guild_only()
    @command()
    async def apostar(self, ctx, cmd: Member = "null", pont: int = None):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            if cmd is "null":

                embed=Embed(title=f"Mencione alguém para apostar e escolha o valor\nExemplo: apostar racheter `10`",
                        color=ctx.author.color,
                        )

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif pont < 5 or pont == None:

                embed=Embed(title="Apostas minimas de `5` pontos",
                    color=ctx.author.color,
                    )

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif ctx.author.id == cmd.id:

                embed=Embed(title="você não pode apostar, com você mesmo.",
                    color=ctx.author.color,
                    )

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif ctx.author.id != cmd.id:

                menos1 = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": cmd.author.id})
                menos2 = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": ctx.author.id})
                zero = 5

                if menos1["ponto"] < zero:

                    embed=Embed(title=f"O usuario `{cmd.name}` não tem `{pont}` pontos, para apostar",
                        color=ctx.author.color,
                        )

                    await ctx.send(f"> {ctx.author.mention}", embed=embed)

                elif menos2["ponto"] < zero:

                    embed=Embed(title=f"Você não tem `{pont}` pontos, para apostar",
                        color=ctx.author.color,
                        )

                    await ctx.send(f"> {ctx.author.mention}", embed=embed)

                elif menos2 >= zero:

                    embed=Embed(title=f"{ctx.author.name} quer apostar com {cmd.name}",
                            description=f"Aposta esta valendo `{pont}` pontos",
                            color=ctx.author.color)

                    embed.add_field(name=f"Esperando resposta do {cmd.name}", value="Reaja ao ✅ para aceitar")

                    mag = await ctx.send(f"> {cmd.mention}", embed=embed)
                    await mag.add_reaction('✅')

                    def check(reaction, user):
                        return user == cmd and str(reaction.emoji) in ['✅']

                    reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=180.0)

                    if (reaction.emoji == '✅') and (reaction.message.id == mag.id):

                        await mag.delete()

                        gerado1 = [10, 11]
                        gerado2 = [12, 13]

                        random1 = randint(10, 13)

                        for i in range(len(gerado1)):

                            if random1 == gerado1[i]:

                                if menos1["ponto"] < zero:

                                    embed=Embed(title=f"O usuario `{cmd.name}` não tem `{pont}` pontos, para apostar",
                                        color=ctx.author.color,
                                        )

                                    await ctx.send(f"> {ctx.author.mention}", embed=embed)

                                elif menos2["ponto"] < zero:

                                    embed=Embed(title=f"Você não tem `{pont}` pontos, para apostar",
                                        color=ctx.author.color,
                                        )

                                    await ctx.send(f"> {ctx.author.mention}", embed=embed)

                                else:

                                    embed=Embed(title=f"O ganhador de `{pont}` pontos foi o {ctx.author.name}",
                                            color=cmd.color,
                                            )

                                    await ctx.send(f"> {ctx.author.mention}", embed=embed)

                                    self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + pont}})
                                    self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":cmd.author.id}, {"$inc":{"ponto": - pont}})

                                    break

                        for a in range(len(gerado2)):

                            if random1 == gerado2[a]:


                                if menos1["ponto"] < zero:

                                    embed=Embed(title=f"O usuario `{cmd.name}` não tem `{pont}` pontos, para apostar",
                                        color=ctx.author.color,
                                        )

                                    await ctx.send(f"> {ctx.author.mention}", embed=embed)

                                elif menos2["ponto"] < zero:

                                    embed=Embed(title=f"Você não tem `{pont}` pontos, para apostar",
                                        color=ctx.author.color,
                                        )

                                    await ctx.send(f"> {ctx.author.mention}", embed=embed)

                                else:

                                    embed=Embed(title=f"O {ctx.author.name} perdeu `{pont}`pontos, para o {cmd.name}",
                                            color=cmd.color,
                                            )

                                    await ctx.send(f"> {cmd.mention}", embed=embed)

                                    self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":cmd.author.id}, {"$inc":{"ponto": + pont}})
                                    self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": - pont}})

                                    break            

    @guild_only()
    @command(aliases=["pl", "perfil"])
    async def profile(self, ctx, targe: Optional[Member]):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            targe = targe or ctx.author
            user = self.client.db.userguild.find_one({"server_id": targe.guild.id} and {"user_id": targe.id})
            total = self.client.db.userglobal.find_one({"user_id": targe.id})

            embed=Embed(title=f"Perfil no {ctx.guild.name}:",
                        color=targe.color,
                        )
            embed.set_author(name=f"{targe}", icon_url=f"{targe.avatar_url}")

            embed.add_field(
                name="Planeta:",
                value=f"{user['planeta']}",
                inline=False
                )
            embed.add_field(
                name="Classe:",
                value=f"{user['classe']}",
                inline=False
                )
            embed.add_field(
                name="Pontos espacial:",
                value=f"   `{user['ponto']}`",
                inline=True
                )
            embed.add_field(
                name="Moedas global(sonos):",
                value=f"   `{total['sonos']}`",
                inline=True
                )
            embed.add_field(
                name=f"Level: `{user['level']}` | `55`",
                value=f"[`{user['xp']}` | `{user['limite']}`]",
                inline=False
                )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @guild_only()
    @command()
    @cooldown(1, 3, BucketType.member)
    async def pontos(self, ctx, targe: Optional[Member]):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            targe = targe or ctx.author
            pontos = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": targe.id})

            embed=Embed(title=f"{targe.name} tem `{pontos['ponto']}` pontos espacial",
                        color=targe.color,
                        )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @guild_only()
    @command()
    @cooldown(1, 3, BucketType.member)
    async def planeta(self, ctx, targe: Optional[Member]):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            targe = targe or ctx.author
            pontos = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": targe.id})

            embed=Embed(title=f"{targe.name} está no planeta `{pontos['planeta']}`",
                        color=targe.color,
                        )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @guild_only()
    @command()
    @cooldown(1, 3, BucketType.member)
    async def sonos(self, ctx, targe: Optional[Member]):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            targe = targe or ctx.author
            pontos = self.client.db.userglobal.find_one({"user_id": targe.id})

            embed=Embed(title=f"{targe.name} tem `{pontos['sonos']}` sonos",
                        color=ctx.author.color,
                        )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @guild_only()
    @command(aliases=['daily', 'diário'])
    @cooldown(1, 86400, BucketType.user)
    async def diario(self, ctx):
        
        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            planeta = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": ctx.author.id})

            if planeta["planeta"] == "Saturno":

                gerado = randint(100, 150)

                embed=Embed(title="Seu sonos diário:", description=f"{gerado}",
                            color=ctx.author.color,
                            )

                embed.add_field(name="Para ver seus sonos:", value="Use sonos/perfil", inline=True)
                embed.set_footer(text="Esse é o diario de um planeta lendario")

                await ctx.send(embed=embed)

                self.client.db.userglobal.update_one({"user_id":ctx.author.id}, {"$inc":{"sonos": + gerado}})

            elif(
                planeta["planeta"] == "Júpiter" or
                planeta["planeta"] == "Netuno" or
                planeta["planeta"] == "Tita" or
                planeta["planeta"] == "Vênus" or
                planeta["planeta"] == "Éris"
                ):
                
                gerado = randint(80, 130)
                
                embed=Embed(title="Seu sonos diario:", description=f"{gerado}",
                            color=ctx.author.color,
                            )

                embed.add_field(name="Para ver seus sonos:", value="Use sonos/perfil", inline=True)
                embed.set_footer(text="Esse é o diário de um planeta épico")

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

                self.client.db.userglobal.update_one({"user_id":ctx.author.id}, {"$inc":{"sonos": + gerado}})

            elif(
                planeta["planeta"] == "Ceres" or
                planeta["planeta"] == "Europa" or
                planeta["planeta"] == "Urano" or
                planeta["planeta"] == "Marte" or
                planeta["planeta"] == "Makemake"
                ):

                gerado = randint(70, 80)

                embed=Embed(title="Seu pontos sonos:", description=f"{gerado}",
                            color=ctx.author.color,
                            )

                embed.add_field(name="Para ver seus sonos:", value="Use sonos/perfil", inline=True)
                embed.set_footer(text="Esse é o diário de um planeta raro")

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

                self.client.db.userglobal.update_one({"user_id":ctx.author.id}, {"$inc":{"sonos": + gerado}})

            elif(
                planeta["planeta"] == "Calisto" or
                planeta["planeta"] == "Mercúrio" or
                planeta["planeta"] == "Encélado" or
                planeta["planeta"] == "Miranda" or
                planeta["planeta"] == "Fobos"
                ):

                gerado = randint(60, 70)

                embed=Embed(title="Seu sonos diario:", description=f"{gerado}",
                            color=ctx.author.color,
                            )

                embed.add_field(name="Para ver seus sonos:", value="Use sonos/perfil", inline=True)
                embed.set_footer(text="Esse é o diário de um planeta incomum")

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

                self.client.db.userglobal.update_one({"user_id":ctx.author.id}, {"$inc":{"sonos": + gerado}})


            elif(
                planeta["planeta"] == "Haumea" or
                planeta["planeta"] == "Plutão" or
                planeta["planeta"] == "Lua" or
                planeta["planeta"] == "terra"
                ):

                gerado = randint(45, 60)

                embed=Embed(title="Seu sonos diário:", description=f"{gerado}",
                            color=ctx.author.color,
                            )

                embed.add_field(name="Para ver seus sonos:", value="Use sonos/perfil", inline=True)
                embed.set_footer(text="Esse é o diário de um planeta comum")

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

                self.client.db.userglobal.update_one({"user_id":ctx.author.id}, {"$inc":{"sonos": + gerado}})

    @guild_only()
    @command()
    @cooldown(1, 3600, BucketType.member)
    async def explorar(self, ctx):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            planeta = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": ctx.author.id})

            if planeta["planeta"] == "Saturno":

                gerado = randint(125, 150)

                embed=Embed(title=f"Explorando Saturno...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )
                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                embede.set_footer(text="Muito boa exploração em Saturno")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Júpiter":

                gerado = randint(110, 130)

                embed=Embed(title=f"Explorando Júpiter...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                
                embede.set_footer(text="Muito boa exploração em Júpiter")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Netuno":

                gerado = randint(100, 130)

                embed=Embed(title=f"Explorando Netuno...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                
                embede.set_footer(text="Muito boa exploração em Netuno")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Tita":

                gerado = randint(100, 125)

                embed=Embed(title=f"Explorando Titã...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                
                embede.set_footer(text="Muito boa exploração em Titã")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Vênus":

                gerado = randint(100, 120)

                embed=Embed(title=f"Explorando Vênus...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                embede.set_footer(text="Muito boa exploração em Vênus")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Éris":

                gerado = randint(95, 115)

                embed=Embed(title=f"Explorando Éris...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                
                embede.set_footer(text="Muito boa exploração em Éris")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Ceres":

                gerado = randint(60, 100)

                embed=Embed(title=f"Explorando Ceres...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                
                embede.set_footer(text="Muito boa exploração em Ceres")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Europa":

                gerado = randint(60, 90)

                embed=Embed(title=f"Explorando Europa...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                
                embede.set_footer(text="Muito boa exploração em Europa")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Urano":

                gerado = randint(60, 85)

                embed=Embed(title="Explorando Urano...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                
                embede.set_footer(text="Muito boa exploração em Urano")

                await mag.edit(embed=embede)

                ponto = ref.child(f"users/local/{ctx.guild.id}/{ctx.author.id}/pontos")
                sonos = ref.child(f"users/global/{ctx.author.id}/sonos")

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Marte":

                gerado = randint(60, 80)

                embed=Embed(title="Explorando Marte...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                
                embede.set_footer(text="Muito boa exploração em Marte")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Makemake":

                gerado = randint(55, 75)

                embed=Embed(title="Explorando Makemake...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                embede.set_footer(text="Muito boa exploração em Makemake")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Calisto":

                gerado = randint(40, 60)

                embed=Embed(title="Explorando Calisto...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                
                embede.set_footer(text="Muito boa exploração em Calisto")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Mercúrio":

                gerado = randint(40, 55)

                embed=Embed(title="Explorando Mercúrio...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                
                embede.set_footer(text="Muito boa exploração em Mercúrio")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Encélado":

                gerado = randint(35, 50)

                embed=Embed(title="Explorando Encélado...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                
                embede.set_footer(text="Muito boa exploração em Encélado")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Miranda":

                gerado = randint(35, 45)

                embed=Embed(title="Explorando Miranda...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                
                embede.set_footer(text="Muito boa exploração em Miranda")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Fobos":

                gerado = randint(32, 41)

                embed=Embed(title="Explorando Fobos...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                
                embede.set_footer(text="Muito boa exploração em Fobos")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Haumea":

                gerado = randint(30, 40)

                embed=Embed(title="Explorando Haumea...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                
                embede.set_footer(text="Muito boa exploração em Haumea")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Plutão":

                gerado = randint(25, 35)

                embed=Embed(title="Explorando Plutão...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                
                embede.set_footer(text="Muito boa exploração em Plutão")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "Lua":

                gerado = randint(20, 30)

                embed=Embed(title="Explorando Lua...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                
                embede.set_footer(text="Muito boa exploração em Lua")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["planeta"] == "terra":

                gerado = randint(15, 25)

                embed=Embed(title="Explorando terra...",
                            color=ctx.author.color,
                            )

                mag = await ctx.send(embed=embed)

                await sleep(2)

                embede=Embed(title="Sucesso na exploração!!",
                            color=ctx.author.color,
                            )

                embede.add_field(name="Pontos encontrados:", value=f"`{gerado}`", inline=True)
                
                embede.set_footer(text="Muito boa exploração em terra")

                await mag.edit(embed=embede)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

            if planeta["classe"] == "Explorador":

                gerado = randint(40, 60)

                fim=Embed(title=f"Ganhou `{gerado}` pontos, por ser um explorador.",
                            color=ctx.author.color,
                            )

                await ctx.send(f"> {ctx.author.mention}", embed=fim)

                self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"ponto": + gerado}})

    @guild_only()
    @command()
    @cooldown(1, 60*15, BucketType.member)
    async def viajar(self, ctx):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            planeta = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": ctx.author.id})
            puxarplaneta = viajante()

            if (
                planeta["planeta"] == "Saturno" or
                planeta["planeta"] == "Júpiter" or
                planeta["planeta"] == "Netuno" or
                planeta["planeta"] == "Titã" or
                planeta["planeta"] == "Vênus" or
                planeta["planeta"] == "Éris"
                ):


                if planeta["planeta"] == "Saturno":

                    embed=Embed(title="Eita Você está em um planeta Lendario",
                                description="tem certeza que deseja viajar ?\nReaja ao ✅ para viajar\nDuração de pergunta: `60s`",
                                color=ctx.author.color)

                    embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                    mag = await ctx.send(embed=embed)
                    await mag.add_reaction('✅')

                    def check(reaction, user):
                        return user == ctx.message.author and str(reaction.emoji) in ['✅']

                    reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=60.0)

                if (
                    planeta["planeta"] == "Júpiter" or
                    planeta["planeta"] == "Netuno" or
                    planeta["planeta"] == "Titã" or
                    planeta["planeta"] == "Vênus" or
                    planeta["planeta"] == "Éris"
                    ):

                    embed=Embed(title="Vocẽ está em um planeta Épico",
                                description="tem certeza que deseja viajar ?\nReaja ao ✅ para viajar\nDuração de pergunta: `60s`",
                                color=ctx.author.color)

                    embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                    mag = await ctx.send(embed=embed)
                    await mag.add_reaction('✅')

                    def check(reaction, user):
                        return user == ctx.message.author and str(reaction.emoji) in ['✅']

                    reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=60.0)
                    
                if (reaction.emoji == '✅') and (reaction.message.id == mag.id):

                    embede=Embed(title="Iniciando viajem !!",
                        color=ctx.author.color,
                        )

                    mag = await ctx.send(f"> {ctx.author.mention}", embed=embede)

                    await sleep(2)

                    if planeta["planeta"] == puxarplaneta[0]:

                        embed=Embed(title="Falha critica, motor falhou.",
                                description=f"Não saiu de {puxarplaneta[0]}",
                                color=ctx.author.color,
                                )

                        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                        await mag.edit(embed=embed)

                    elif puxarplaneta[0] == "Falhou":

                        embed=Embed(title="Muitos erros na viaje",
                                description=f"retornou a terra",
                                color=ctx.author.color,
                                )

                        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                        await mag.edit(embed=embed)

                        self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$set":{"planeta": "terra"}})

                    else:

                        embed=Embed(title=f"Sucesso na sua viajem.",
                                description=f"Viajou ate `{puxarplaneta[0]}`",
                                color=ctx.author.color,
                                )

                        embed.set_image(url=f"{puxarplaneta[1]}")
                        embed.add_field(name=f"Viajem {puxarplaneta[3]}:", value=f"Rank de raridade `{puxarplaneta[2]}`")

                        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                        msg = await mag.edit(embed=embed)
            
                        self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$set":{"planeta": puxarplaneta[0]}})
                                
            else:

                embede=Embed(
                    title="Iniciando viajem !!",
                    color=ctx.author.color,
                    )

                mag = await ctx.send(f"> {ctx.author.mention}", embed=embede)

                await sleep(2)

                if planeta["planeta"] == puxarplaneta[0]:

                    embed=Embed(title="Falha critica, motor falhou.",
                            description=f"Não saiu de {puxarplaneta[0]}",
                            color=ctx.author.color,
                            )

                    embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                    await mag.edit(embed=embed)

                elif puxarplaneta[0] == "Falhou":

                    embed=Embed(title="Muitos erros na viaje",
                            description=f"retornou a terra",
                            color=ctx.author.color,
                            )

                    embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                    await mag.edit(embed=embed)

                    self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$set":{"planeta": "terra"}})

                else:

                    embed=Embed(title=f"Sucesso na sua viajem.",
                            description=f"Viajou até `{puxarplaneta[0]}`",
                            color=ctx.author.color,
                            )

                    embed.set_image(url=f"{puxarplaneta[1]}")
                    embed.add_field(name=f"Viajem {puxarplaneta[3]}:", value=f"Rank de raridade `{puxarplaneta[2]}`")

                    embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                    msg = await mag.edit(embed=embed)
        
                    self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$set":{"planeta": puxarplaneta[0]}})

    @guild_only()
    @command()
    @cooldown(1, 60*15, BucketType.member)
    async def viajarextra(self, ctx):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/rpg")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="comando desligado aqui, para ativar",
                        description="Use: `config rpg ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            ifo = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": ctx.author.id})

            if ifo["classe"] == "Viajante":

                planeta = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": ctx.author.id})
                puxarplaneta = viajante()

                if (
                    planeta["planeta"] == "Saturno" or
                    planeta["planeta"] == "Júpiter" or
                    planeta["planeta"] == "Netuno" or
                    planeta["planeta"] == "Titã" or
                    planeta["planeta"] == "Vênus" or
                    planeta["planeta"] == "Éris"
                    ):


                    if planeta["planeta"] == "Saturno":

                        embed=Embed(title="Eita Você está em um planeta Lendario",
                                    description="tem certeza que deseja viajar ?\nReaja ao ✅ para viajar\nDuração de pergunta: `60s`",
                                    color=ctx.author.color)

                        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                        mag = await ctx.send(embed=embed)
                        await mag.add_reaction('✅')

                        def check(reaction, user):
                            return user == ctx.message.author and str(reaction.emoji) in ['✅']

                        reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=60.0)

                    if (
                        planeta["planeta"] == "Júpiter" or
                        planeta["planeta"] == "Netuno" or
                        planeta["planeta"] == "Titã" or
                        planeta["planeta"] == "Vênus" or
                        planeta["planeta"] == "Éris"
                        ):

                        embed=Embed(title="Você está em um planeta Épico",
                                    description="tem certeza que deseja viajar ?\nReaja ao ✅ para viajar\nDuração de pergunta: `60s`",
                                    color=ctx.author.color)

                        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                        mag = await ctx.send(embed=embed)
                        await mag.add_reaction('✅')

                        def check(reaction, user):
                            return user == ctx.message.author and str(reaction.emoji) in ['✅']

                        reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=60.0)
                        
                    if (reaction.emoji == '✅') and (reaction.message.id == mag.id):

                        embede=Embed(title="Iniciando viajem !!",
                            color=ctx.author.color,
                            )

                        mag = await ctx.send(f"> {ctx.author.mention}", embed=embede)

                        await sleep(2)

                        if planeta["planeta"] == puxarplaneta[0]:

                            embed=Embed(title="Falha critica, motor falhou.",
                                    description=f"Não saiu de {puxarplaneta[0]}",
                                    color=ctx.author.color,
                                    )

                            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                            await mag.edit(embed=embed)

                        elif puxarplaneta[0] == "Falhou":

                            embed=Embed(title="Muitos erros na viaje",
                                    description=f"retornou a terra",
                                    color=ctx.author.color,
                                    )

                            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                            await mag.edit(embed=embed)

                            self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$set":{"planeta": "terra"}})

                        else:

                            embed=Embed(title=f"Sucesso na sua viajem.",
                                    description=f"Viajou até `{puxarplaneta[0]}`",
                                    color=ctx.author.color,
                                    )

                            embed.set_image(url=f"{puxarplaneta[1]}")
                            embed.add_field(name=f"Viajem {puxarplaneta[3]}:", value=f"Rank de raridade `{puxarplaneta[2]}`")

                            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                            msg = await mag.edit(embed=embed)
                
                            self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$set":{"planeta": puxarplaneta[0]}})
                                    
                else:

                    embede=Embed(
                        title="Iniciando viajem !!",
                        color=ctx.author.color,
                        )

                    mag = await ctx.send(f"> {ctx.author.mention}", embed=embede)

                    await sleep(2)

                    if planeta["planeta"] == puxarplaneta[0]:

                        embed=Embed(title="Falha critica, motor falhou.",
                                description=f"Não saiu de {puxarplaneta[0]}",
                                color=ctx.author.color,
                                )

                        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                        await mag.edit(embed=embed)

                    elif puxarplaneta[0] == "Falhou":

                        embed=Embed(title="Muitos erros na viaje",
                                description=f"retornou a terra",
                                color=ctx.author.color,
                                )

                        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                        await mag.edit(embed=embed)

                        self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$set":{"planeta": "terra"}})

                    else:

                        embed=Embed(title=f"Sucesso na sua viajem.",
                                description=f"Viajou ate `{puxarplaneta[0]}`",
                                color=ctx.author.color,
                                )

                        embed.set_image(url=f"{puxarplaneta[1]}")
                        embed.add_field(name=f"Viajem {puxarplaneta[3]}:", value=f"Rank de raridade `{puxarplaneta[2]}`")

                        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                        msg = await mag.edit(embed=embed)
            
                        self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$set":{"planeta": puxarplaneta[0]}})

            else: 

                embed=Embed(title=f"{ctx.author.name} não faz parte da classe viajante para usar esse comando",
                            description="Veja as classes e seus valores com o comando `classes`",
                            color=ctx.author.color,
                            )

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @diario.error
    async def diario_cooldown(self, ctx, error):

        if isinstance(error, CommandOnCooldown):

            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)
            d, h = divmod(h, 24)

            embed=Embed(title=f"Espere `{h: .0f}H{m: .0f}Min{s: .0f}seg` para os pontos diarios novamente",
                        color=ctx.author.color,
                        )

            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @viajar.error
    async def viajar_cooldown(self, ctx, error):

        if isinstance(error, CommandOnCooldown):

            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)

            embed=Embed(title=f"Espere `{m: .0f}Min{s: .0f}seg` para viajar novamente.",
                        description="Fazendo a manutenção da sua nave",
                        color=ctx.author.color,
                        )

            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @observar.error
    async def observar_cooldown(self, ctx, error):

        if isinstance(error, CommandOnCooldown):

            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)

            embed=Embed(title=f"Espere `{m: .0f}Min{s: .0f}seg` para que observar a todo momento ?.",
                        description="Descanse os olhos da beleza do universo",
                        color=ctx.author.color,
                        )

            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @crime.error
    async def crime_cooldown(self, ctx, error):

        if isinstance(error, CommandOnCooldown):

            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)

            embed=Embed(title=f"Espere `{m: .0f}Min{s: .0f}seg` para ir ao crime novamente.",
                        description="Fugindo dos guradas...",
                        color=ctx.author.color,
                        )

            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @viajarextra.error
    async def viajarextra_cooldown(self, ctx, error):

        if isinstance(error, CommandOnCooldown):

            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)

            ref = db.reference("bot-seven")

            info = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": ctx.author.id})

            if info["classe"] == "Viajante":

                embed=Embed(title=f"Espere `{m: .0f}Min{s: .0f}seg` para viajar novamente.",
                            description="Fazendo a manutenção da sua nave",
                            color=ctx.author.color,
                            )

                embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            else: 

                embed=Embed(title=f"{ctx.author.name} não faz parte da classe viajante para usar esse comando",
                            description="Veja as classes e seus valores com o comando `classes`",
                            color=ctx.author.color,
                            )

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @punir.error
    async def punir_cooldown(self, ctx, error):

        if isinstance(error, CommandOnCooldown):

            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)

            info = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": ctx.author.id})

            if info["classe"] == "FBI espacial":

                embed=Embed(title=f"Espere `{m: .0f}Min{s: .0f}seg` para punir novamente.",
                            description="Ser a lei cansa né ?",
                            color=ctx.author.color,
                            )

                embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            else: 

                embed=Embed(title=f"{ctx.author.name} não faz parte da classe FBI espacial para usar esse comando",
                            description="Veja as classes e seus valores com o comando `classes`",
                            color=ctx.author.color,
                            )

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @explorar.error
    async def explorar_cooldown(self, ctx, error):

        if isinstance(error, CommandOnCooldown):

            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)
            d, h = divmod(h, 24)

            embed=Embed(title=f"Espere `{m: .0f}Min{s: .0f}seg` para se aventurar no planeta.",
                        description="Hora do descanso, e manutenção de equipamentos",
                        color=ctx.author.color,
                        )

            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @roubar.error
    async def roubar_cooldown(self, ctx, error):

        if isinstance(error, CommandOnCooldown):

            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)
            d, h = divmod(h, 24)

            info = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": ctx.author.id})

            if info["classe"] == "Pirata espacial":

                embed=Embed(title=f"Espere `{m: .0f}Min{s: .0f}seg` para roubar.",
                            description="se esconda até a barra estar limpa",
                            color=ctx.author.color,
                            )

                embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            else: 

                embed=Embed(title=f"{ctx.author.name} não faz parte da classe pirata espacial para usar esse comando",
                            description="Veja as classes e seus valores com o comando `classes`",
                            color=ctx.author.color,
                            )

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

def setup(client):

    client.add_cog(rpg(client))
    print("RPG carregado")    
