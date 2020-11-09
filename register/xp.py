from firebase_admin import db
from discord.ext.commands import Cog


class xp(Cog):

    def __init__(self, client):
            self.client = client

    @Cog.listener()
    async def on_message(self, ctx):

        if ctx.author.bot: return

        if not ctx.guild: return

        #xp global e por guild aparti de msg

        ref = db.reference("bot-seven")
        canal = ref.child(f"config/{ctx.guild.id}/{ctx.channel.id}/xp")
        final = canal.get()

        if final == "ativar":
            self.client.db.userguild.update_one({"server_id":ctx.guild.id} and {"user_id":ctx.author.id}, {"$inc":{"xp": + 4}})

        else: return

def setup(client):

    client.add_cog(xp(client))

    print("Ganho de XP ativo")
