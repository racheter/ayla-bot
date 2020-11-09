from discord import Embed, Member
from datetime import datetime
from typing import Optional
from firebase_admin import db
from time import monotonic
from random import randint
from discord.ext.commands import Cog, command, guild_only, cooldown, BucketType


class comando(Cog):

    def __init__(self, client):
        self.client = client

    @guild_only()
    @command(aliases=['bi'])
    async def botinfo(self, ctx):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/diversos")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="Comando desligado aqui, para ativar",
                        description="Use: `config diversos ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            ping = self.client.latency * 1000

            embed=Embed(title="Bot info:", color=self.client.user.color,)
            embed.set_thumbnail(url=self.client.user.avatar_url)

            embed.add_field(name="ID:", value=f"{self.client.user.id}", inline=False)
            embed.add_field(name="Nome:", value=f"{self.client.user.name}", inline=False)
            embed.add_field(name="Usuarios:", value=f"`{len(list(self.client.users))}`", inline=True)
            embed.add_field(name="Quantidade de servidores:", value=f"`{len(self.client.guilds)}`", inline=True)
            embed.add_field(name="Ping:", value=f"`{ping: .0f}`", inline=False)
            embed.add_field(name="Criador", value="Racheter(ID:663927891297304614)", inline=False)
            embed.set_footer(text="Versão: Alfa-0.0.9.5")

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @guild_only()
    @command(aliases=["ui"])
    async def userinfo(self, ctx, member: Optional[Member]):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/diversos")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="Comando desligado aqui, para ativar",
                        description="Use: `config diversos ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            member = member or ctx.author or member.id
            user = self.client.db.userglobal.find_one({"user_id": member.id})

            if member.bot:

                embed=Embed(title="Informações do Bot",
                            color=member.color,
                        )

                embed.set_thumbnail(url=f"{member.avatar_url}")

                fields=[("ID:", member.id, False),
                        ("Nome:", str(member.name), True),
                        ("Cargo mais alto:", member.top_role.mention, True),
                        ("Bot criado:", member.created_at.strftime('%d/%m/%Y as %H:%M:%S'), True),
                        ("Entrou em:", member.joined_at.strftime('%d/%m/%Y as %H:%M:%S'), True)]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

                await ctx.send(f"> {member.mention}", embed=embed)
            
            else:

                def boost():
                    if bool(member.premium_since) is True: return "Sim"
                    if bool(member.premium_since) is False: return "Não"

                def status():
                    if user["status"] == "solteiro": return "Solteiro"
                    else: return f"Casado(a) com {user['status']}"

                booster = boost()
                statusc = status()

                embed=Embed(title="Informações do Membro", color=member.color)

                embed.set_thumbnail(url=f"{member.avatar_url}")

                fields=[("ID:", member.id, False),
                        ("Nome:", str(member.name), False),
                        ("Status civil:", statusc, False),
                        ("Cargo mais alto:", member.top_role.mention, True),
                        ("Atividade:", str(member.status).title(), True),
                        ("Booster:", booster, True),
                        ("Conta criada:", member.created_at.strftime('%d/%m/%Y as %H:%M:%S'), True),
                        ("Entrou em:", member.joined_at.strftime('%d/%m/%Y as %H:%M:%S'), True)]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

                await ctx.send(f"> {member.mention}", embed=embed)

    @guild_only()
    @command(aliases=["foto"])
    async def avatar(self, ctx, cmd: Member = "null"):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/diversos")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="Comando desligado aqui, para ativar",
                        description="Use: `config diversos ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            if cmd == "null":

                embed=Embed(title=f"A sua foto {ctx.author.name}",
                        color=ctx.author.color,
                    )

                embed.set_image(url=f"{ctx.author.avatar_url}")

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            else:

                embed=Embed(title=f"A foto do(a) {cmd.name}",
                        color=cmd.color,
                    )

                embed.set_image(url=f"{cmd.avatar_url}")

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @guild_only()
    @command(aliases=["si"])
    async def serverinfo(self, ctx):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/diversos")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="Comando desligado aqui, para ativar",
                        description="Use: `config diversos ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            embed=Embed(title="Informações do Servidor",
                        color=ctx.guild.owner.color)

            embed.set_thumbnail(url=f"{ctx.guild.owner.avatar_url}")

            field=[("ID:", ctx.guild.id, True),
                    ("Dono(a):", ctx.guild.owner, False),
                    ("Região:", ctx.guild.region, True),
                    ("Humanos:", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
                    ("Robos:", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
                    ("Salas de texto:", len(ctx.guild.text_channels), True),
                    ("Salas de voz:", len(ctx.guild.voice_channels), True),
                    ("Cargos:", len(ctx.guild.roles), True),
                    ("Servidor criado:", ctx.guild.created_at.strftime('%d/%m/%Y as %H:%M:%S'), True)]

            for name, value, inline in field:
                embed.add_field(name=name, value=value, inline=inline)

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @guild_only()
    @command()
    async def ping(self, ctx):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/diversos")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="Comando desligado aqui, para ativar",
                        description="Use: `config diversos ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

                before = monotonic()
                pingb = ((monotonic() - before) * 100000000)
                ping = self.client.latency * 1000

                embed=Embed(title="Poong!!",
                            color=ctx.author.color,
                        )

                embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                embed.add_field(name= "Ping BOT",
                                value= f"`{ping: .0f}ms`",
                                inline=True)

                embed.add_field(name="Ping API",
                                value=f"`{pingb: .0f}ms`",
                                inline=True)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @guild_only()
    @command(aliases=["ajuda", "comandos"])
    async def help(self, ctx, cmd: Optional[str] = "none"):

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/diversos")
        final = canal.get()

        if final == None or final == "false":

            embed=Embed(title="Comando desligado aqui, para ativar",
                        description="Use: `config diversos ativar`",
                        color=ctx.author.color,
                    )

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

        if final == "true":

            if cmd == "none":

                embed=Embed(title="Lista de Ajuda aos comandos:",
                        color=ctx.author.color,
                    )

                fields=[("Informaçoes use:", "help `info`", False),
                        ("Diversos use:", "help `div`", False),
                        ("RPG use:", "help `rpg`", False),
                        ("Administração use:", "help `adm`", False),
                        ("Configuração use:", "help `config`", False),
                        ]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif cmd == "info":

                embed=Embed(title="Comandos informativos:",
                        color=ctx.author.color,
                    )

                fields=[("`userinfo` [none ou membro]", "Para ver informações do usuario", False),
                        ("`serverinfo` [sem parametro]", "Para ver informações do servidor", False),
                        ("`botinfo` [sem parametros]", "Mostra infos do the seven(eu)", False),
                        ("`avatar` [membro]", "Mostra a foto de perfil do usuario", False),
                        ("`ping` [sem parametros]", "mostra a latencia do bot", False),
                        ]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif cmd == "div":

                embed=Embed(title="Comandos diversos ou aleatorio:",
                        color=ctx.author.color,
                    )

                fields=[("`random` [valor]", "Randomiza um numero escolhido", False),
                        ("`casar` [pessoa]", "Para casar com alguem efetando o userinfo global", False),
                        ("`sono`", "Envia um um msg nada aver", False),
                        ("`sonos`", "Para ver suas moedas global", False),
                        ("`pay` [pessoa] e [valor]", "Para trasnferir seu sonos a alguem", False),
                        ]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif cmd == "rpg":

                embed=Embed(title="Comandos do RPG:",
                        color=ctx.author.color,
                    )

                fields=[("`perfil` [none ou membro]", "Para ver informações de jogador", False),
                        ("`pontos` [none ou membro]", "Para ver os pontos", False),
                        ("`planeta` [none ou membro]", "Mostra seu planeta", False),
                        ("`raridade` [sem parametros]", "informações de raridade dos planetas/satelites", False),
                        ("`apostar` [membro] e [valor]", "Para começar uma aposta por pontos", False),
                        ("`tudo` [sem parametros]", "dobre ou perde todos seus pontos", False),
                        ("`viajar` [sem parametros]", "Para ir para algum planeta ou satelite natural", False),
                        ("`observar` [sem parametros]", "Observe as estrelas do universo", False),
                        ("`crime` [sem parametros]", "Faça um leve crime mas com cuidado e.e", False),
                        ("`classes` [sem parametros]", "Escolha uma classe e veja suas vantagens", False),
                        ("`classe` [sem parametros]", "Veja sua classe atual", False),
                        ("`diario` [sem parametros]", "Para ganhar pontos diarios", False),
                        ("`explorar` [sem parametros]", "Para explorar o planeta que esta e ganhar pontos e sonos", False),
                        ]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif cmd == "adm":

                embed=Embed(title="Comandos do ADM:",
                        color=ctx.author.color,
                    )

                fields=[("`ban` [membro] e [motivo]", "Para banir um membro", False),
                        ("`kick` [membro] e [motivo]", "Para expulsar alguem", False),
                        ("`say` [embed ou embedfrase] ou/e [msg]", "Para usar a voz do bot", False),
                        ("`apagar` [membro] ou [valor]", "Apaga de 2 até 1000 msg da sala", False),
                        ]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif cmd == "config":

                embed=Embed(title="Comandos para configurar:",
                        color=ctx.author.color,
                    )

                fields=[("`ativar` [comando ou xp]", "ativa um comando na sala q o executar", False),
                        ("`desativar` [comando ou xp]", "desativa um comando na sala q o executar", False),
                        ("`prefixo` [prefixo]", "muda o prefixo do servidor", False),
                        ]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            else:

                embed=Embed(color=ctx.author.color,
                        )
                            
                embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                embed.add_field(
                    name="Modulo não encontrado ou nao disponivel",
                    value=
                        "```use apenas help ou help [Modulo]```"
                    ,inline=False)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

def setup(client):

    client.add_cog(comando(client))

    print("Comandos carregado")
