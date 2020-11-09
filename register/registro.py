from firebase_admin import db
from discord.ext.commands import Cog
from asyncio import sleep
from json import dump, load


class reg(Cog):

    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_member_join(self, member):

        if member.bot: return

        servidor = self.client.db.userguild.find({"server_id": member.guild.id} and {"user_id": member.id})
        total = self.client.db.userglobal.find({"user_id": member.id})
        
        if servidor is None:

            self.client.db.userguild.insert({
                    "server_id": member.guild.id,
                    "user_id": member.id,
                    "ponto": 0,
                    "limite": 1000,
                    "level": 0,
                    "xp": 0,
                    "planeta": "terra",
                    "classe": "sem classe"
                    })

        if total is None:

            self.client.db.userglobal.insert({
                    "user_id": member.id,
                    "status": "solteiro",
                    "casal": "null",
                    "sonos": 0,
                    "baniu": 0
                    })

    @Cog.listener()
    async def on_message(self, ctx):

        if ctx.author.bot: return

        if not ctx.guild: return

        servidor = self.client.db.userguild.find({"server_id": ctx.guild.id} and {"user_id": ctx.author.id})
        total = self.client.db.userglobal.find({"user_id": ctx.author.id})
        
        if servidor is None:

            self.client.db.userguild.insert({
                    "server_id": ctx.guild.id,
                    "user_id": ctx.author.id,
                    "ponto": 0,
                    "limite": 1000,
                    "level": 0,
                    "xp": 0,
                    "planeta": "terra",
                    "classe": "sem classe"
                    })

        if total is None:

            self.client.db.userglobal.insert({
                    "user_id": ctx.author.id,
                    "status": "solteiro",
                    "casal": "null",
                    "sonos": 0,
                    "baniu": 0
                    })

def setup(client):

    client.add_cog(reg(client))

    print("Registro carregado")