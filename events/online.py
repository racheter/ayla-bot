from discord.ext.commands import Cog
from discord.ext.tasks import loop
from discord import Game, Streaming
from asyncio import sleep
from itertools import cycle

status = cycle(['Olaaa, use help/ajuda.', 'prefixo padrão: -', 'V: 0.0.9.5'])

class ready(Cog):

    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):

        self.change_status.start()
        print(f"{self.client.user.name} Esta online")
        print("Versao alfa: 0.0.9.5")

    @loop(seconds=10)
    async def change_status(self):

        await self.client.change_presence(activity=Streaming(
                                        name=f"em {len(self.client.guilds)} servidores",
                                        url="https://www.twitch.tv/racheter"))
        await sleep(5)
        await self.client.change_presence(activity=Game(next(status)))

def setup(client):

    
    client.add_cog(ready(client))
