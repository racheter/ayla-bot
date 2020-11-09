from discord.ext.commands import Cog


class autorole(Cog):

    def __init__(self, client):
            self.client = client
    
    @Cog.listener()
    async def on_message(self, ctx):

        if ctx.author.bot: return
        if not ctx.guild: return
        if ctx.guild.id == 726608160437305376:

            role = utils.get(ctx.author.roles, id=719585182637883504)
            user = ctx.author

            if role is None:
                await user.add_roles(role)

    @Cog.listener()
    async def on_member_join(self, member):

        if member.guild.id == 726608160437305376:

            role = utils.get(member.guild.roles, id=719585182637883504)
            user = member.author

            await user.add_roles(role)

def setup(client):

    client.add_cog(autorole(client))

    print("AutoRole ativo")