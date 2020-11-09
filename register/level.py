from discord import Embed, utils
from asyncio import sleep
from discord.ext.commands import Cog


class level(Cog):

    def __init__(self, client):
            self.client = client

    @Cog.listener()
    async def on_message(self, ctx):

        if ctx.author.bot: return

        if not ctx.guild: return

        analise = self.client.db.userguild.find_one({"server_id": ctx.guild.id} and {"user_id": ctx.author.id})

        #leveis por guild:

        if analise is None: return

        if (analise['xp'] >= 1000 and analise['xp'] <= 2199) and (analise['level'] == 0):
            #level 1 local

            if ctx.guild.id == 773751985932992565:

                embed=Embed(title=f"Subiu para o level 1 em `{ctx.guild.name}`",
                        description="Ganhou `50` sonos`",color=ctx.author.color,)
                await ctx.author.send(embed=embed)

                self.client.db.userglobal.update_one({"user_id":ctx.audthor.id},{"$inc":{"sonos": + 50}})

                role = utils.get(ctx.guild.roles, id=775130034641305641)
                user = ctx.author
                await user.add_roles(role)

            self.client.db.userguild.update_one(
                {"server_id":ctx.guild.id} and {"user_id":ctx.author.id},
                {"$set":{"limite": 2200}, "$inc":{"level": + 1}})

        if (analise['xp'] >= 2200 and analise['xp'] <= 3299) and (analise['level'] == 1):
            #level 2 local

            self.client.db.userguild.update_one(
                {"server_id":ctx.guild.id} and {"user_id":ctx.author.id},
                {"$set":{"limite": 3300}, "$inc":{"level": + 1}})

        if ((analise['xp'] >= 3300) and (analise['xp'] <= 4599)) and (analise['level'] == 2):
            #level 3 local

            self.client.db.userguild.update_one(
                {"server_id":ctx.guild.id} and {"user_id":ctx.author.id},
                {"$set":{"limite": 4600}, "$inc":{"level": + 1}})

        if ((analise['xp'] >= 4600) and (analise['xp'] <= 5999)) and (analise['level'] == 3):
            #level 4 local

            self.client.db.userguild.update_one(
                {"server_id":ctx.guild.id} and {"user_id":ctx.author.id},
                {"$set":{"limite": 6000}, "$inc":{"level": + 1}})

        if ((analise['xp'] >= 6000) and (analise['xp'] <= 7499)) and (analise['level'] == 4):
            #level 5 local

            self.client.db.userguild.update_one(
                {"server_id":ctx.guild.id} and {"user_id":ctx.author.id},
                {"$set":{"limite": 7500}, "$inc":{"level": + 1}})

        if ((analise['xp'] >= 7500) and (analise['xp'] <= 9099)) and (analise['level'] == 5):
            #level 6 local

            self.client.db.userguild.update_one(
                {"server_id":ctx.guild.id} and {"user_id":ctx.author.id},
                {"$set":{"limite": 9100}, "$inc":{"level": + 1}})

        if ((analise['xp'] >= 9100) and (analise['xp'] <= 10799)) and (analise['level'] == 6):
            #level 7 local

            self.client.db.userguild.update_one(
                {"server_id":ctx.guild.id} and {"user_id":ctx.author.id},
                {"$set":{"limite": 10800}, "$inc":{"level": + 1}})

        if ((analise['xp'] >= 10800) and (analise['xp'] <= 12599)) and (analise['level'] == 7):
            #level 8 local

            self.client.db.userguild.update_one(
                {"server_id":ctx.guild.id} and {"user_id":ctx.author.id},
                {"$set":{"limite": 12600}, "$inc":{"level": + 1}})

        if ((analise['xp'] >= 12600) and (analise['xp'] <= 14499)) and (analise['level'] == 8):
            #level 9 local

            self.client.db.userguild.update_one(
                {"server_id":ctx.guild.id} and {"user_id":ctx.author.id},
                {"$set":{"limite": 14500}, "$inc":{"level": + 1}})

        if ((analise['xp'] >= 14500) and (analise['xp'] <= 16499)) and (analise['level'] == 9):
            #level 10 local

            self.client.db.userguild.update_one(
                {"server_id":ctx.guild.id} and {"user_id":ctx.author.id},
                {"$set":{"limite": 16500}, "$inc":{"level": + 1}})

        if ((analise['xp'] >= 16500) and (analise['xp'] <= 18599)) and (analise['level'] == 10):
            #level 11 local:

            self.client.db.userguild.update_one(
                {"server_id":ctx.guild.id} and {"user_id":ctx.author.id},
                {"$set":{"limite": 18600}, "$inc":{"level": + 1}})

        if ((analise['xp'] >= 18600) and (analise['xp'] <= 20799)) and (analise['level'] == 11):
            #level 12 local:

            self.client.db.userguild.update_one(
                {"server_id":ctx.guild.id} and {"user_id":ctx.author.id},
                {"$set":{"limite": 20800}, "$inc":{"level": + 1}})


        if ((analise['xp'] >= 20800) and (analise['xp'] <= 23099)) and (analise['level'] == 12):
            #level 13 local

            self.client.db.userguild.update_one(
                {"server_id":ctx.guild.id} and {"user_id":ctx.author.id},
                {"$set":{"limite": 23100}, "$inc":{"level": + 1}})

        if ((analise['xp'] >= 23100) and (analise['xp'] <= 25499)) and (analise['level'] == 13):
            #level 14 local

            self.client.db.userguild.update_one(
                {"server_id":ctx.guild.id} and {"user_id":ctx.author.id},
                {"$set":{"limite": 25500}, "$inc":{"level": + 1}})

        if ((analise['xp'] >= 25500) and (analise['xp'] <= 27999)) and (analise['level'] == 14):
            #level 15 local

            self.client.db.userguild.update_one(
                {"server_id":ctx.guild.id} and {"user_id":ctx.author.id},
                {"$set":{"limite": 28000}, "$inc":{"level": + 1}})

        if (analise['xp'] >= 28000 and analise['xp'] <= 30599) and (analise['level'] == 0):
            #level 16 local

            self.client.db.userguild.update_one(
                {"server_id":ctx.guild.id} and {"user_id":ctx.author.id},
                {"$set":{"limite": 30600}, "$inc":{"level": + 1}})

def setup(client):

    client.add_cog(level(client))

    print("Ganho de level ativo")
