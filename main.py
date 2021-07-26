import discord
import os
import requests

client = discord.Client(activity=discord.Game(name='Fetch'))
ClientToken = os.environ['Token']


async def SendCat(message):
 try:
  if message.content.lower().startswith("/cat"):
   r = requests.get("https://api.thecatapi.com/v1/images/search").json()
   await message.reply(r[0]["url"],mention_author=False)
 except:
  await message.reply("Could not get a picture of cute animal sorry",mention_author=False)


async def SendDog(message):
 try:
  if message.content.lower().startswith("/dog"):
   r = requests.get("https://random.dog/woof.json?ref=apilist.fun").json()
   await message.reply(r["url"],mention_author=False)
 except:
  await message.reply("Could not get a picture of a very cute animal sorry",mention_author=False)


async def Donation(message):
 embed=discord.Embed(title="Animal Welfare Insitute", url="https://awionline.org/", description="Since 1951, the Animal Welfare Institute has been dedicated to reducing animal suffering caused by people.", color=0x109319)
 embed.set_thumbnail(url="https://awionline.org/sites/default/files/uploads/images/18-AWI-Logo-Hexagons-Green-Border_300x300.png")
 await message.reply(embed=embed,mention_author=False)
 



@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))
  

@client.event
async def on_message(message):
 if message.author == client.user:
   return

 Commands = {
 "/cat":SendCat,
 "/dog":SendDog,
 "/donate":Donation
 }

 mess = message.content.lower()
 if mess in Commands.keys():
  await Commands[message.content.lower()](message)



client.run(ClientToken)