from discord.ext.commands import Cog, Greedy, command, guild_only, has_permissions, bot_has_permissions, CheckFailure
from discord import Embed, Member, PermissionOverwrite, utils
from datetime import datetime, timedelta
from json import dump, load
from asyncio import sleep
from firebase_admin import db
from typing import Optional


class admins(Cog):

    def __init__(self, client):
        self.client = client

    @guild_only()
    @command(aliases=['editprefixo'])
    @has_permissions(administrator=True)
    @bot_has_permissions(administrator=True)
    async def prefixo(self, ctx, prefix: str):

        contar = len(prefix)

        if contar <= 4:

            embed=Embed(
                title=f"Novo prefixo do servidor: `{prefix}`", color=ctx.author.color,timestamp=datetime.utcnow())
            await ctx.send(embed=embed)

            um = prefix.lower()
            dois = prefix.upper()

            with open(r"config/prefixo.json", 'r') as f:

                prefixos = load(f)

            prefixos[str(ctx.guild.id)] = [um, dois]

            with open(r"config/prefixo.json", 'w') as f:

                dump(prefixos, f, indent=4)

        elif contar >= 5:

            embed=Embed(title="Coloque apenas ate 4 caracteres", color=ctx.author.color, timestamp=datetime.utcnow())

            await ctx.send(embed=embed)

        else:

            embed=Embed(title="editprefixo [Prefixo desejado]", color=ctx.author.color, timestamp=datetime.utcnow())

            await ctx.send(embed=embed)

    @guild_only()
    @command(aliases=['aviso', 'adv', 'avisa', 'avisar'])
    @has_permissions(kick_members=True)
    @bot_has_permissions(kick_members=True)
    async def warn(self, ctx, target: Member = None, *, reason: Optional[str] = "Sem motivo definido"):

        if target == None:

            embed=Embed(title="aviso [pessoa] [motivo]", color=ctx.author.color)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(embed=embed)

        else:

            ref = db.reference("bot-seven")
            infoa = ref.child(f"avisos/{ctx.guild.id}/{target.id}/aviso")
            avisar = infoa.get()

            role1 = utils.get(ctx.guild.roles, name="1ª Aviso | Ayla")
            role2 = utils.get(ctx.guild.roles, name="2ª Aviso | Ayla")
            user = target

            if role1 is None:
                await ctx.guild.create_role(name="1ª Aviso | Ayla")
                pass

            if role2 is None:
                await ctx.guild.create_role(name="2ª Aviso | Ayla")
                pass


            if avisar == None:

                sera = ref.child("avisos")
                sera.update({f'{ctx.guild.id}/{target.id}': {"aviso": 0 }})

                await sleep(5)
                pass

            if avisar >= 0:

                embed=Embed(title=f"{ctx.author.name} esta prestes dar um aviso o(a) {target.name}",
                            description="tem certeza que deseja avisar ?\nReaja ao ✅ para avisar\nDuração de pergunta: `40s`",
                            color=ctx.author.color)

                embed.add_field(name="Motivo:", value= reason)

                mag = await ctx.send(embed=embed)
                await mag.add_reaction('✅')

                def check(reaction, user):
                    return user == ctx.message.author and str(reaction.emoji) in ['✅']

                reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=40.0)

                if (reaction.emoji == '✅') and (reaction.message.id == mag.id):

                    await mag.delete()

                    infoa2 = ref.child(f"avisos/{ctx.guild.id}/{target.id}")

                    num = avisar + 1
                    num2 = avisar - 2
                    user = target

                    if avisar == 0:

                        embed=Embed(title="Usuario recebeu o 1° aviso", color=0xDD2222, timestamp=datetime.utcnow())
                        embed.set_thumbnail(url=f"{target.avatar_url}")

                        embed.add_field(name= "user:",
                                        value= f"Nome: {target.name}\nApelido:{target.display_name}\nID:{target.id}",
                                        inline=False)

                        embed.add_field(name= "Motivo:", value= reason, inline=False)
                        embed.add_field(name= "Quem avisou:",
                                        value= f"Nome: {ctx.author.name}\nID: {ctx.author.id}", inline=False)

                        men = await ctx.send(embed=embed)

                        infoa2.update({"aviso": num })

                        role = utils.get(ctx.guild.roles, name="1ª Aviso | Ayla")

                        await sleep(1)
                        
                        await user.add_roles(role)

                        if ctx.guild.id == 719555624374894692:

                            canal1 = self.client.get_channel(id=719564144516268092)
                            await canal1.send(embed=embed)

                            await sleep(5)
                            await men.delete()

                    if avisar == 1:

                        embed=Embed(title="Usuario recebeu o 2° aviso", color=0xDD2222, timestamp=datetime.utcnow())
                        embed.set_thumbnail(url=f"{target.avatar_url}")

                        embed.add_field(name= "user:",
                                        value= f"Nome: {target.name}\nApelido:{target.display_name}\nID:{target.id}",
                                        inline=False)

                        embed.add_field(name= "Motivo:", value= reason, inline=False)
                        embed.add_field(name= "Quem avisou:",
                                        value= f"Nome: {ctx.author.name}\nID: {ctx.author.id}", inline=False)

                        men = await ctx.send(embed=embed)

                        infoa2.update({"aviso": num })

                        role = utils.get(ctx.guild.roles, name="2ª Aviso | Ayla")

                        await sleep(1)

                        await user.add_roles(role)

                        if ctx.guild.id == 719555624374894692:

                            canal1 = self.client.get_channel(id=719564144516268092)
                            await canal1.send(embed=embed)

                            await sleep(5)
                            await men.delete()

                    if avisar >= 2:

                        embed=Embed(title="Usuario recebeu o 3° aviso e foi banido", color=0xDD2222, timestamp=datetime.utcnow())
                        embed.set_thumbnail(url=f"{target.avatar_url}")

                        embed.add_field(name= "user:",
                                        value= f"Nome: {target.name}\nApelido:{target.display_name}\nID:{target.id}",
                                        inline=False)

                        embed.add_field(name= "Motivo:", value= reason, inline=False)
                        embed.add_field(name= "Quem avisou:",
                                        value= f"Nome: {ctx.author.name}\nID: {ctx.author.id}", inline=False)

                        men = await ctx.send(embed=embed)

                        infoa2.update({"aviso": num2 })

                        await target.ban(reason=reason)

                        if ctx.guild.id == 719555624374894692:

                            canal1 = self.client.get_channel(id=719564144516268092)
                            await canal1.send(embed=embed)

                            await sleep(5)
                            await men.delete()

    @guild_only()
    @command(aliases=['removeaviso', 'radv', 'desavisa', 'desavisar'])
    @has_permissions(kick_members=True)
    @bot_has_permissions(kick_members=True)
    async def unwarn(self, ctx, target: Member = None, *, reason: Optional[str] = "Sem motivo definido"):

        if target == None:

            embed=Embed(title="aviso [pessoa] [motivo]", color=ctx.author.color)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(embed=embed)

        else:

            ref = db.reference("bot-seven")
            infoa = ref.child(f"avisos/{ctx.guild.id}/{target.id}/aviso")
            avisar = infoa.get()

            role1 = utils.get(ctx.guild.roles, name="1ª Aviso | Ayla")
            role2 = utils.get(ctx.guild.roles, name="2ª Aviso | Ayla")
            user = target

            if role1 is None:
                await ctx.guild.create_role(name="1ª Aviso | Ayla")
                pass
            if role2 is None:
                await ctx.guild.create_role(name="2ª Aviso | Ayla")
                pass

            if avisar == None:

                sera = ref.child("avisos")

                sera.update({f'{ctx.guild.id}/{target.id}': {"aviso": 0 }})

                await sleep(5)
                pass

            if avisar == 0:

                embed=Embed(title="Usuario sem nem um aviso", color=0xDD2222, timestamp=datetime.utcnow())
                embed.set_thumbnail(url=f"{target.avatar_url}")

                await ctx.send(embed=embed)

            else:

                embed=Embed(title=f"{ctx.author.name} esta prestes a retirar um aviso do(a) {target.name}",
                            description="tem certeza que deseja retirar o aviso ?\nReaja ao ✅ para desavisar\nDuração de pergunta: `40s`",
                            color=ctx.author.color)

                embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                embed.add_field(name="Motivo da retirada:", value= reason)

                mag = await ctx.send(embed=embed)
                await mag.add_reaction('✅')

                def check(reaction, user):
                    return user == ctx.message.author and str(reaction.emoji) in ['✅']

                reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=40.0)

                if (reaction.emoji == '✅') and (reaction.message.id == mag.id):

                    await mag.delete()

                    infoa2 = ref.child(f"avisos/{ctx.guild.id}/{target.id}")

                    num2 = avisar - 1
                    user = target

                    if avisar == 1:

                        embed=Embed(title="Um aviso foi retirado", color=0xDD2222, timestamp=datetime.utcnow())
                        embed.set_thumbnail(url=f"{target.avatar_url}")

                        embed.add_field(name= "user:",
                                        value= f"Nome: {target.name}\nApelido:{target.display_name}\nID:{target.id}",
                                        inline=False)

                        embed.add_field(name= "Motivo:", value= reason, inline=False)
                        embed.add_field(name= "Quem retirou:",
                                        value= f"Nome: {ctx.author.name}\nID: {ctx.author.id}", inline=False)

                        men = await ctx.send(embed=embed)

                        infoa2.update({"aviso": num2 })

                        role = utils.get(ctx.guild.roles, name="1ª Aviso | Ayla")

                        await sleep(1)
                        
                        await user.remove_roles(role)

                        if ctx.guild.id == 719555624374894692:

                            canal1 = self.client.get_channel(id=719564144516268092)
                            await canal1.send(embed=embed)

                            await sleep(5)
                            await men.delete()

                    if avisar == 2:

                        embed=Embed(title="Um aviso foi retirado", color=0xDD2222, timestamp=datetime.utcnow())
                        embed.set_thumbnail(url=f"{target.avatar_url}")

                        embed.add_field(name= "user:",
                                        value= f"Nome: {target.name}\nApelido:{target.display_name}\nID:{target.id}",
                                        inline=False)

                        embed.add_field(name= "Motivo:", value= reason, inline=False)
                        embed.add_field(name= "Quem retirou:",
                                        value= f"Nome: {ctx.author.name}\nID: {ctx.author.id}", inline=False)

                        men = await ctx.send(embed=embed)

                        infoa2.update({"aviso": num2 })

                        role = utils.get(ctx.guild.roles, name="2ª Aviso | Ayla")

                        await sleep(1)

                        await user.remove_roles(role)

                        if ctx.guild.id == 719555624374894692:

                            canal1 = self.client.get_channel(id=719564144516268092)
                            await canal1.send(embed=embed)

                            await sleep(5)
                            await men.delete()


    @guild_only()
    @command(aliases=['purge', 'clear'])
    @has_permissions(manage_messages=True)
    @bot_has_permissions(manage_messages=True)
    async def apagar(self, ctx, targets: Greedy[Member], cmd: int):

        def _check(message):
            return not len(targets) or message.author in targets

        if cmd is None:

            embed=Embed(title="apagar [quantidade]", color=ctx.author.color)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(embed=embed)

        elif cmd >= 2 and cmd <= 1000:

            apagadas = await ctx.channel.purge(limit=cmd + 1,
                                                after=datetime.utcnow()-timedelta(days=14), 
                                                check=_check)

            embed=Embed(title=f"{len(apagadas) - 1} Mensagens foi apagada.", color=ctx.author.color)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            mag = await ctx.send(embed=embed)

            await sleep(5)

            await mag.delete()

        else:

            embed=Embed(title="Somente valores entre 2 a 1000 mensagens.", color=ctx.author.color)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(embed=embed)

    @guild_only()
    @command(aliases=['banir'])
    @bot_has_permissions(ban_members=True)
    @has_permissions(ban_members=True)
    async def ban(self, ctx, targets: Greedy[Member], *, reason: Optional[str] = "Sem motivo definido"):

        if not len(targets):
            embed=Embed(title=f"Sem nem um usuario mencionado.", color=ctx.author.color)
            await ctx.send(embed=embed)

        else:

            for target in targets:

                embed=Embed(title=f"{ctx.author.name} esta prestes a banir o {target.name}",
                            description="tem certeza que deseja banir ?\nReaja ao ✅ para banir\nDuração de pergunta: `40s`",
                            color=ctx.author.color)

                embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                embed.add_field(name="Motivo:", value= reason)

                mag = await ctx.send(embed=embed)
                await mag.add_reaction('✅')

                def check(reaction, user):
                    return user == ctx.message.author and str(reaction.emoji) in ['✅']

                reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=40.0)

                if (reaction.emoji == '✅') and (reaction.message.id == mag.id):

                    embed=Embed(title="Usuario banido", color=0xDD2222, timestamp=datetime.utcnow())
                    embed.set_thumbnail(url=f"{target.avatar_url}")

                    embed.add_field(name= "user:",
                                    value= f"Nome: {target.name}\nApelido:{target.display_name}\nID:{target.id}",
                                    inline=False)

                    embed.add_field(name= "Motivo:", value= reason, inline=False)
                    embed.add_field(name= "Quem baniu:",
                                    value= f"Nome: {ctx.author.name}\nID: {ctx.author.id}", inline=False)

                    men = await ctx.send(embed=embed)
                    await target.ban(reason=reason)

                    if ctx.guild.id == 719555624374894692:

                        canal1 = self.client.get_channel(id=719564144516268092)
                        await canal1.send(embed=embed)

                        await sleep(5)
                        await men.delete()

    @guild_only()
    @command(aliases=['expulsar', 'k'])
    @bot_has_permissions(kick_members=True)
    @has_permissions(kick_members=True)
    async def kick(self, ctx, targets: Greedy[Member], *, reason: Optional[str] = "Sem motivo definido"):

        if not len(targets):
            embed=Embed(title=f"Sem nem um usuario mencionado.", color=ctx.author.color)
            await ctx.send(embed=embed)

        else:
            
            for target in targets:

                embed=Embed(title=f"{ctx.author.name} esta prestes a expulsar o {target.name}",
                            description="tem certeza que deseja expulsar ?\nReaja ao ✅ para expulsar\nDuração de pergunta: `40s`",
                            color=ctx.author.color)

                embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

                embed.add_field(name="Motivo:", value= reason)

                mag = await ctx.send(f"> {ctx.author.mention}", embed=embed)
                await mag.add_reaction('✅')

                def check(reaction, user):
                    return user == ctx.message.author and str(reaction.emoji) in ['✅']

                reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=40.0)

                if (reaction.emoji == '✅') and (reaction.message.id == mag.id):

                    await mag.delete()

                    embed=Embed(title="Usuario Expulso", color=0xDD2222, timestamp=datetime.utcnow())
                    embed.set_thumbnail(url=f"{target.avatar_url}")

                    embed.add_field(name= "user:",
                                    value= f"Nome: {target.name}\nApelido:{target.display_name}\nID:{target.id}",
                                    inline=False)

                    embed.add_field(name= "Motivo:", value= reason, inline=False)

                    embed.add_field(name= "Quem expulsou:",
                                    value= f"Nome: {ctx.author.name}\nID: {ctx.author.id}", inline=False)

                    men = await ctx.send(embed=embed)
                    await target.kick(reason=reason)

                    if ctx.guild.id == 719555624374894692:

                        canal1 = self.client.get_channel(id=719564144516268092)
                        await canal1.send(embed=embed)

                        await sleep(5)
                        await men.delete()

    @guild_only()
    @command(aliases=['configurar'])
    @has_permissions(administrator=True)
    @bot_has_permissions(administrator=True)
    async def config(self, ctx, cmd: str, opc: str):

        ref = db.reference("bot-seven")
        cmd = cmd.lower()
        opc = opc.lower()
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/{cmd}")
        final = canal.get()

        if ((cmd == "xp") or (cmd == "rpg") or (cmd == "diversos") or (cmd == "jogos")) and (opc == "ativar"):

            if (final == "true"):

                embed=Embed(title=f"`{cmd}` ja esta ativo aqui",
                            color=ctx.author.color,
                            timestamp=datetime.utcnow())

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif (final == "false") or (final == None):

                ativar = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}")
                ativar.update({f"{cmd}": "true"})

                embed=Embed(title=f"`{cmd}` na sala foi ativo",
                            color=ctx.author.color,
                            timestamp=datetime.utcnow())

                await ctx.send(embed=embed)

        if ((cmd == "xp") or (cmd == "rpg") or (cmd == "diversos") or (cmd == "jogos")) and (opc == "desativar"):

            if (final == "false") or (final == None):

                embed=Embed(title=f"`{cmd}` ja esta desativado aqui",
                            color=ctx.author.color,
                            timestamp=datetime.utcnow())

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif (final == "true"):

                ativar = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}")
                ativar.update({f"{cmd}": "false"})

                embed=Embed(title=f"`{cmd}` na sala foi desativado",
                            color=ctx.author.color,
                            timestamp=datetime.utcnow())

                await ctx.send(embed=embed)

    @guild_only()
    @command(aliases=['falar'])
    @has_permissions(manage_messages=True)
    @bot_has_permissions(manage_messages=True)
    async def say(self, ctx, cmd: Optional[str] = "escreva: algo/embed/embedfrase.", *, reason: Optional[str] = "frase"):

        await ctx.message.delete()
        
        if cmd == "embed":

            if reason is None:

                embed=Embed(title="Favor escrever algo para mim falar",
                        color=ctx.author.color)
                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            else:

                separ = reason.split("|")

                embed=Embed(title=separ[0],
                        description=separ[1],
                        color=ctx.author.color,
                        timestamp=datetime.utcnow())
                await ctx.send(embed=embed)

        elif cmd == "embedfrase": 

            if reason is None:

                embed=Embed(title="Favor escrever algo para mim falar",
                        color=ctx.author.color)
                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            else:

                embed=Embed(title=reason,
                        color=ctx.author.color,
                        timestamp=datetime.utcnow())
                await ctx.send(embed=embed)

        elif (cmd != "embed") or (cmd != "embedfrase"):

            if reason == "frase":

                await ctx.send(f"{cmd}")

            else:

                await ctx.send(f"{cmd} {reason}")

    @say.error
    async def say_error(self, ctx, error):

        if isinstance(error, CheckFailure):

            embed=Embed(title="Vocẽ não tem permissão para usar minha voz.",
                        color=ctx.author.color,
                        timestamp=datetime.utcnow())

            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):

        if isinstance(error, CheckFailure):

            embed=Embed(title="Vocẽ não tem permissão para expulsar aqui.",
                        color=ctx.author.color,
                        timestamp=datetime.utcnow())

            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):

        if isinstance(error, CheckFailure):

            embed=Embed(title="Vocẽ não tem permissão para banir aqui.",
                        color=ctx.author.color,
                        timestamp=datetime.utcnow())

            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):

        if isinstance(error, CheckFailure):

            embed=Embed(title="Vocẽ não tem permissão para banir aqui.",
                        color=ctx.author.color,
                        timestamp=datetime.utcnow())

            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @apagar.error
    async def apagar_error(self, ctx, error):

        if isinstance(error, CheckFailure):

            embed=Embed(title="Vocẽ não tem permissão para apagar mensagens",
                        color=ctx.author.color,
                        timestamp=datetime.utcnow())

            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @prefixo.error
    async def prefixo_error(self, ctx, error):

        if isinstance(error, CheckFailure):

            embed=Embed(title="Vocẽ não tem permissão para mudar o prefixo",
                        color=ctx.author.color,
                        timestamp=datetime.utcnow())

            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @warn.error
    async def warn_error(self, ctx, error):

        if isinstance(error, CheckFailure):

            embed=Embed(title="Vocẽ não tem permissão para usar aviso",
                        color=ctx.author.color,
                        timestamp=datetime.utcnow())

            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @unwarn.error
    async def unwarn_error(self, ctx, error):

        if isinstance(error, CheckFailure):

            embed=Embed(title="Vocẽ não tem permissão para usar aviso",
                        color=ctx.author.color,
                        timestamp=datetime.utcnow())

            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

    @config.error
    async def warn_error(self, ctx, error):

        if isinstance(error, CheckFailure):

            embed=Embed(title="Vocẽ não tem permissão para confgurar os comandos e xp",
                        color=ctx.author.color,
                        timestamp=datetime.utcnow())

            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")

            await ctx.send(f"> {ctx.author.mention}", embed=embed)

def setup(client):

    client.add_cog(admins(client))

    print("Comandos ADM carregado")
