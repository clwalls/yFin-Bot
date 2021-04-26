import discord
import os
from userInputs import parseUserInput

client = discord.Client()
@client.event
async def on_ready():
  ## startup bot
  print('We have logged in as {0.user}'.format(client))

@client.event
## triggers each time user types
async def on_message(message):
  ouput = ''
  # not the bot msging itself
  if message.author == client.user:
    return
  
  if message.content.startswith('$init'):
    await message.channel.send('Hello, eTrade bot is online.')

  # userInputs  
  if message.content.startswith('$'):
    print('Received Message: ' + message.content)
    output = parseUserInput(message.content[1:len(message.content)])
    await message.channel.send(output)
client.run(os.getenv('TOKEN'))