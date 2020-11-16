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
    @command(aliases=["beijar"])
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
                        "https://cdn.discordapp.com/attachments/753391453052338226/756628760484118528/anime-kissin-1.gif",
                        "https://tenor.com/view/blow-kiss-cat-gif-7332151",
                        "https://tenor.com/view/besitos-cute-kiss-muah-love-gif-5615952",
                        "https://tenor.com/view/kiss-dating-love-relationship-couples-gif-14190535",
                        "https://tenor.com/view/love-you-lots-gif-13817272",
                        "https://tenor.com/view/milk-and-mocha-bear-couple-kisses-kiss-love-gif-12498627",
                        "https://tenor.com/view/rain-kiss-aria-montgomery-lucy-hale-kisses-gif-5614993",
                        "https://tenor.com/view/pretty-little-liars-pll-muah-kiss-love-gif-4469403",
                        "https://tenor.com/view/tangled-eugene-flynn-rider-rapunzel-kiss-gif-3701305",
                        "https://tenor.com/view/love-you-lots-kiss-peachcat-gif-13985240",
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

                    embed=Embed(title=f"{pessoa.name} beijou devolta o(a) {ctx.author.name}",
                            color=pessoa.color,)

                    embed.set_image(url=beijo2)

                    mag = await ctx.send(ctx.author.mention, embed=embed)

    @guild_only()
    @command(aliases=["abraçar", "hug"])
    async def abracar(self, ctx, cmd: Optional[Member]):

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

                embed=Embed(title="Mencione alguem para abraçar e.e",
                        color=ctx.author.color)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            else:
                pessoa = cmd or ctx.author
                links = [
                        "https://tenor.com/view/rapunzel-eugene-flynn-hug-tangled-gif-6213503",
                        "https://media.giphy.com/media/EvYHHSntaIl5m/giphy.gif",
                        "https://tenor.com/view/chaves-chiquinha-abraco-abracao-oi-gif-4508403",
                        "https://tenor.com/view/hug-love-hi-bye-cat-gif-15999080",
                        "https://tenor.com/view/dog-hug-bff-bestfriend-friend-gif-9512793",
                        "https://tenor.com/view/frozen-anna-elsa-hug-hugging-gif-4911454",
                        "https://tenor.com/view/running-hug-embrace-imiss-you-good-to-see-you-again-gif-15965620",
                        "https://media.giphy.com/media/f6y4qvdxwEDx6/giphy.gif",
                        "https://tenor.com/view/hugs-notmine-kpop-korea-gif-4593622",
                        "https://media.tenor.co/videos/a0bca07a85d9e4693683d0fe98f3f2b7/mp4",
                        "https://media.giphy.com/media/VGACXbkf0AeGs/giphy.gif",
                        "https://media.giphy.com/media/OiKAQbQEQItxK/giphy.gif",
                        "https://media.giphy.com/media/a5vmVcRPc63qU/giphy.gif",
                        "https://media.giphy.com/media/llmZp6fCVb4ju/giphy.gif",
                        "https://tenor.com/view/milk-and-mocha-hug-cute-kawaii-love-gif-12535134",
                        "https://media.giphy.com/media/Hp4lpOT1Ns60o/giphy.gif",
                        "https://tenor.com/view/otters-sea-hug-sweet-finding-dory-gif-13642193",
                        "https://media.giphy.com/media/VbawWIGNtKYwOFXF7U/giphy.gif",
                        "https://media.giphy.com/media/5pUE8Ep8ONvTUihSqz/giphy.gif",
                        "https://media.giphy.com/media/8KKRIP5ZHUo2k/giphy.gif",
                        "https://media.giphy.com/media/QbkL9WuorOlgI/giphy.gif",
                        "https://media.giphy.com/media/lXiRKBj0SAA0EWvbG/giphy.gif",
                        "https://media.giphy.com/media/Lb3vIJjaSIQWA/giphy.gif",
                        "https://media.giphy.com/media/3o6Zth3OnNv6qDGQ9y/giphy.gif",
                        "https://media.giphy.com/media/42YlR8u9gV5Cw/giphy.gif",
                        ]
                
                beijo1 = choice(links)
                
                embed=Embed(title=f"{ctx.author.name} abraçou {pessoa.name}",
                            color=ctx.author.color,)

                embed.set_image(url=beijo1)
                
                mag = await ctx.send(f"{pessoa.mention}", embed=embed)

                await mag.add_reaction('🔃')

                def check(reaction, user):
                    return user == cmd and str(reaction.emoji) in ['🔃']

                reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=180.0)

                if reaction.emoji == '🔃':

                    beijo2 = choice(links)

                    embed=Embed(title=f"{pessoa.name} abraçou de volta a(o) {ctx.author.name}",
                            color=pessoa.color,)

                    embed.set_image(url=beijo2)

                    mag = await ctx.send(ctx.author.mention, embed=embed)
    @guild_only()
    @command(aliases=["slap", "bater"])
    async def tapa(self, ctx, cmd: Optional[Member]):

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

                embed=Embed(title="Mencione alguem para da um tapa e.e",
                        color=ctx.author.color)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            else:
                pessoa = cmd or ctx.author
                links = [
                        "https://tenor.com/view/baka-slap-huh-angry-gif-15696850",
                        "https://tenor.com/view/kevin-hart-slap-face-your-gif-10570690",
                        "https://tenor.com/view/tom-and-jerry-slap-slapping-butt-slap-spanking-gif-4517373",
                        "https://tenor.com/view/face-punch-punch-minions-fine-happy-gif-4902917",
                        "https://tenor.com/view/slap-in-the-face-angry-gtfo-bitc-bitch-slap-gif-15667197",
                        "https://tenor.com/view/slap-face-gif-11457043",
                        "https://tenor.com/view/tapa-slap-tapa-na-cara-novela-en-nombre-del-amor-gif-18605469",
                        "https://tenor.com/view/no-slap-fight-snap-out-gif-9934434",
                        "https://tenor.com/view/tapa-anime-bosta-tapa-naruto-slap-sakura-gif-13876327",
                        "https://tenor.com/view/lulugifs-charlie-brown-lucy-peanuts-punch-gif-15768734",
                        "https://tenor.com/view/psych-james-roday-shawn-spencer-dule-hill-gus-gif-4653591",
                        "https://tenor.com/view/tapa-slap-anime-smile-girls-last-tour-gif-17223486",
                        "https://tenor.com/view/tapa-zabuza-zabuza-momochi-kakashi-naruto-gif-18152981",
                        "https://media.giphy.com/media/gSIz6gGLhguOY/giphy.gif",
                        "https://media.giphy.com/media/w5FSoU86sXRFm/giphy.gif",
                        "https://media.giphy.com/media/vxvNnIYFcYqEE/giphy.gif",
                        "https://media.giphy.com/media/Hj9ixvpSfqcQo/giphy.gif",
                        ]
                
                beijo1 = choice(links)
                
                embed=Embed(title=f"{ctx.author.name} deu um tapa em {pessoa.name}",
                            color=ctx.author.color,)

                embed.set_image(url=beijo1)
                
                mag = await ctx.send(f"{pessoa.mention}", embed=embed)

                await mag.add_reaction('🔃')

                def check(reaction, user):
                    return user == cmd and str(reaction.emoji) in ['🔃']

                reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=180.0)

                if reaction.emoji == '🔃':

                    beijo2 = choice(links)

                    embed=Embed(title=f"{pessoa.name} deu outro tapa em {ctx.author.name}",
                            color=pessoa.color,)

                    embed.set_image(url=beijo2)

                    mag = await ctx.send(ctx.author.mention, embed=embed)

    @guild_only()
    @command(aliases=["dançar", "dance"])
    async def dancar(self, ctx, cmd: Optional[Member]):

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

                embed=Embed(title="Mencione alguem para dançar e.e",
                        color=ctx.author.color)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            else:
                pessoa = cmd or ctx.author
                links = [
                        "https://tenor.com/view/the-simpsons-dance-family-gif-3628979",
                        "https://tenor.com/view/milk-and-mocha-dance-dancing-music-gif-12302383",
                        "https://tenor.com/view/dancasincronizada-dancinhasincronizada-triosincronizado-sincronia-dancing-gif-13642190",
                        "https://media.tenor.co/videos/88bbc40b612fca20da9e2fb80dd552e5/mp4",
                        "https://media.tenor.co/videos/8f19a9d13a5cb161c462239a584094d8/mp4",
                        "https://media.tenor.co/videos/20c31be6f2c4cafa2be558e44d04aa80/mp4",
                        "https://tenor.com/view/dance-gif-9962144",
                        "https://tenor.com/view/gorilla-dance-monkey-moves-gif-17513213",
                        "https://media.giphy.com/media/l0HUfRgRh7BI7HINq/giphy.gif",
                        "https://media.giphy.com/media/l0HUqsz2jdQYElRm0/giphy.gif",
                        "https://media.giphy.com/media/8zYunr3Hg8XPq/giphy.gif",
                        "https://media.giphy.com/media/8zYunr3Hg8XPq/giphy.gif",
                        "https://media.giphy.com/media/6fScAIQR0P0xW/giphy.gif",
                        "https://media.giphy.com/media/2C3hV2vrG901a/giphy.gif",
                        "https://media.giphy.com/media/a8AXSGtbEl1du/giphy.gif",
                        "https://media.giphy.com/media/pyJqbazBZwmgMFT1hU/giphy.gif",
                        "https://media.giphy.com/media/3o6gE8Hu24GQ0UfZgA/giphy.gif",
                        "https://media.giphy.com/media/3o6gE3VhZCgkWTd0hq/giphy.gif",
                        "https://media.giphy.com/media/VHZ3d4ONaojh1SXKB0/giphy.gif",
                        "https://media.giphy.com/media/3o6gEdF4U6g3t1VO3m/giphy.gif",
                        "https://media.giphy.com/media/l46CeO6ZgoEUkBuCY/giphy.gif",
                        "https://media.giphy.com/media/3oz8xPL6TlIjxN1t3G/giphy.gif",
                        "https://media.giphy.com/media/26gs6RKvzfgsWRg3e/giphy.gif",
                        "https://media.giphy.com/media/xT8qBeXXHhwRmpOmFW/giphy.gif",
                        "https://media.giphy.com/media/l0K4aTfuNhKNTmvN6/giphy.gif",
                        "https://media.giphy.com/media/Ve20ojrMWiTo4/giphy.gif",
                        "https://media.giphy.com/media/iFL8qJ5DVusJG/giphy.gif",
                        "https://media.giphy.com/media/3og0Izv3p7vMprq2Qw/giphy.gif",
                        "https://media.giphy.com/media/l0Exk8EUzSLsrErEQ/giphy.gif",
                        "https://media.giphy.com/media/FzRKfocZhf7J6/giphy.gif",
                        "https://media.giphy.com/media/bTzFnjHPuVvva/giphy.gif",
                        "https://media.giphy.com/media/102VfCWF40oAuI/giphy.gif",
                        "https://media.giphy.com/media/1TJB4TPjtaEJq/giphy.gif",
                        "https://media.giphy.com/media/3o7abldj0b3rxrZUxW/giphy.gif",
                        "https://media.giphy.com/media/HqJmOe2M1Af9C/giphy.gif",
                        "https://media.discordapp.net/attachments/753391453052338226/774678602225942528/tenor.gif",
                        ]
                
                beijo1 = choice(links)
                
                embed=Embed(title=f"{ctx.author.name} dançou com {pessoa.name}",
                            color=ctx.author.color,)

                embed.set_image(url=beijo1)
                
                mag = await ctx.send(f"{pessoa.mention}", embed=embed)

                await mag.add_reaction('🔃')

                def check(reaction, user):
                    return user == cmd and str(reaction.emoji) in ['🔃']

                reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=180.0)

                if reaction.emoji == '🔃':

                    beijo2 = choice(links)

                    embed=Embed(title=f"{pessoa.name} dançou tambem com {ctx.author.name}",
                            color=pessoa.color,)

                    embed.set_image(url=beijo2)

                    mag = await ctx.send(ctx.author.mention, embed=embed)

    @guild_only()
    @command()
    async def casar(self, ctx, target: Member = None):

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

            if target == None:

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

            elif ctx.author.id == user2["casal"]:

                embed=Embed(title="Os dois ja estão casados",
                        color=ctx.author.color,)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif (user2["status"] != "solteiro") and (user2["casal"] != "null"):

                embed=Embed(title=f"`{target.name}` ja esta comprometido(a)",
                        color=ctx.author.color,)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif (user["status"] == "solteiro") and (user["casal"] == "null"):

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

    @guild_only()
    @command()
    async def divorciar(self, ctx, target: Member = None):

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

            if target == None:

                embed=Embed(title="Favor mencionar ela ou ele para o divórcio",
                            color=ctx.author.color,)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif target.id == ctx.author.id:

                embed=Embed(title="Você não casou com você mesmo",
                            color=ctx.author.color,)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif user2["casal"] != ctx.author.id:

                embed=Embed(title=f"Você não esta casado com a(o) {target}",
                            color=ctx.author.color,)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif target == self.client.user:

                embed=Embed(title="tu não casou comigo.",
                            color=ctx.author.color,)

                await ctx.send(f"> {ctx.author.mention}", embed=embed)

            elif (user["status"] != "solteiro") and (user["casal"] == "null"):

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
