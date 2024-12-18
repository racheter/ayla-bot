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

        servidor = self.client.db.userguild.find_one({"server_id": member.guild.id} and {"user_id": member.id})
        total = self.client.db.userglobal.find_one({"user_id": member.id})
        
        if servidor is None:

            self.client.db.userguild.insert_one({
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

            self.client.db.userglobal.insert_one({
                    "user_id": member.id,
                    "status": "solteiro",
                    "casal": "null",
                    "sonos": 0,
                    "baniu": 0
                    })

        ref = db.reference("bot-seven")
        avisos = ref.child(f"avisos/{member.guild.id}/{member.id}")
        ca_pre = avisos.get()

        if ca_pre is None:

            sera = ref.child("avisos")

            sera.update({f'{member.guild.id}/{member.id}': {"aviso": 0 }})

    @Cog.listener()
    async def on_message(self, message):

        if message.author.bot: return

        if not message.guild: return

        servidor = self.client.db.userguild.find_one({"server_id": message.guild.id} and {"user_id": message.author.id})
        total = self.client.db.userglobal.find_one({"user_id": message.author.id})
        
        if servidor is None:

            self.client.db.userguild.insert_one({
                    "server_id": message.guild.id,
                    "user_id": message.author.id,
                    "ponto": 0,
                    "limite": 1000,
                    "level": 0,
                    "xp": 0,
                    "planeta": "terra",
                    "classe": "sem classe"
                    })

        if total is None:

            self.client.db.userglobal.insert_one({
                    "user_id": message.author.id,
                    "status": "solteiro",
                    "casal": "null",
                    "sonos": 0,
                    "xp": 0,
                    "baniu": 0
                    })

        ref = db.reference("bot-seven")
        avisos = ref.child(f"avisos/{message.guild.id}/{message.author.id}")
        ca_pre = avisos.get()

        if ca_pre is None:

            sera = ref.child("avisos")

            sera.update({f'{message.guild.id}/{message.author.id}': {"aviso": 0 }})

def setup(client):

    client.add_cog(reg(client))

    print("Registro carregado")
