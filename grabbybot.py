import discord
import string
import logging
import asyncio

#Set logging
logging.basicConfig(level=logging.INFO)
#Establish client
client = discord.Client()
#Login
login = False
        
@client.event
async def on_ready():
    #Add Channel ID first
    channel = client.get_channel('channel ID')
    f = open('training.txt', 'a', encoding='utf-8')
    n = 0
    #set limit (limited to upper limit of int)
    async for l in client.logs_from(channel, limit=100, reverse=True):
        #This writes the author, then the message, adding a new line
        #Each time
        f.write(l.author.name + ':' + '\n' + l.content + '\n' + '' + '\n')
        n = n+1
        print('added['+ str(n) +']:' + l.author.name+ ' : ' + l.content)



while login == False:
    email = input('Enter your email: ')
    password = input('Enter your email: ')
    client.run(email,password) 
    if client.is_logged_in == True:
        login == True

