from firebase_admin import initialize_app
from firebase_admin import db
from firebase_admin.credentials import Certificate
from discord.ext.commands import Cog
import pymongo


class adm(Cog):

    def __init__(self, client):
        self.client = client

        cred = Certificate('config/fb.json')
        initialize_app(cred, {
            'databaseURL': 'https://bot-seven-racheter.firebaseio.com/',
            'databaseAuthVariableOverride': {
                'uid': 'acesso-total'
            }
        })

        client.db = pymongo.MongoClient("mongodb+srv://racheter:JOIgVNE1kW1A0B5H@bot.wob10.gcp.mongodb.net/bot?retryWrites=true&w=majority")['database']
        
def setup(client):
    client.add_cog(adm(client))
    
    print("Dadas bases carregadas")
