from discord.ext.commands import Bot
from discord import Client, Intents
from json import load
from lib.infobot import informar
import pymongo
import logging

client = Client()
info = informar()


def get_prefix(client, message):

    if not message.guild:
        return "-"

    with open("config/prefixo.json") as f:
        prefixos = load(f)

    if str(message.guild.id) not in prefixos:
        return "-"

    prefixe = prefixos[str(message.guild.id)]
    return prefixe

client = Bot(case_insensitive=True, command_prefix=get_prefix, intent=Intents.all())
client.remove_command("help")

modulos = [
    "commands.cmdadm",
    "commands.diversos",
    "commands.rpg",
    "commands.cdmdono",
    "commands.jogos",
    "register.adm",
    "register.xp",
    "register.level",
    "register.registro",
    "events.erros",
    "events.online"
    ]

logging.basicConfig(level=logging.ERROR)

if __name__ == "__main__":

    for modulo in modulos:
        client.load_extension(modulo)

    client.run(info)
