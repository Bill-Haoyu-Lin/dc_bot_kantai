
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
from random import seed
from random import randint

#load the .env file
load_dotenv()
#setting prefix for commands
client = commands.Bot(command_prefix = ".")
TOKEN = os.getenv('DISCORD_TOKEN')
TRIGGER_WORDS = {
    "Hibiki": ["That's me!", "( ͡° ͜ʖ ͡°)","DESU!","Ура!","	響だよ。その活躍ぶりから不死鳥の通り名もあるよ。\n我是响。由于活跃的战绩也被称作不死鸟哦。"],
    "who is ur owner": ["Biu SAMA"],
    "hi": ["hello",":smile:"],
    "8ball": ["It is certain :8ball:", "Definetly not :8ball:", "Definietly :8ball:" ],
    "来点色图": ["calling FBI........","FBI OPEN UP!"],
    "where is Bill": ["Writing his code, wait.....looks like it's not me!!!!!!:tired_face:"],
    "pog": ["Pog Champ!"],
    "hello": ["hello there!",":smile:"],
    "Good night": ["おやすみ\nnite nite:smile:","Oyasumi:smile:","司令官、今日も一日、お疲れ様。\n司令官，今天一天也辛苦您了"]
    }
#creating on ready command to let us know the bot is online
@client.event
async def on_ready():
    print("Hibiki is Online. ")


#reading messages sent in a discord and responds to specific phrases or words
@client.event
async def on_message(message):
    if (message.content.startswith("Hello")):
        await message.channel.send("hello, I am Hibiki")
        image = ["Верный.png"]
        await message.channel.send(file=discord.File(image[0]))
        #add reaction to message sent
        emoji  = '\N{THUMBS UP SIGN}'
        await message.add_reaction(emoji)

    if (message.content.startswith("D")):
        try:
            num_wrote = message.content;
            num_wrote=num_wrote.replace('D','')
            num = randint(1, int(num_wrote));
            await message.channel.send(num)
        except:
            await message.channel.send("PLEASE SEND SOMETHING GOOOOOOOD")

    if (message.content in TRIGGER_WORDS):
        await message.channel.send(random.choice(TRIGGER_WORDS[message.content]))
        emoji  = '\N{THUMBS UP SIGN}'
        await message.add_reaction(emoji)
    #processes all commands in messages so bot can read other commands afterwards
    await client.process_commands(message)

#command input your prefix then your command


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def joke(ctx):
    # opening jokes file and setting a list of each joke as an element to joke_list
    with open('Jokes.txt', 'r', encoding="utf8") as f:
        joke_list = f.readlines()
    msg = random.choice(joke_list)  # choosing random element from the list
    await ctx.send(msg)  # sending message

@client.command()
async def dice(ctx):
    # opening jokes file and setting a list of each joke as an element to joke_list
    num = randint(1, 100);
      # choosing random element from the list
    await ctx.send(num)

# knock knock joke command
@client.command()
async def knockjoke(ctx):
    await ctx.send("Knock Knock!")

    # waiting for the user to send the message "who's there?" it will timeout in 60 seconds
    def check(msg):
        return msg.content == "who's there?" and msg.channel == ctx.channel and msg.author == ctx.author

    await client.wait_for("message", check=check, timeout=60.0)

    # opening knockjokes file and setting a list of each joke to knock_joke_list
    with open("knockjokes.txt", "r", encoding="utf8") as f:
        knock_joke_list = f.readlines()
    joke = random.choice(knock_joke_list).split(
        "*")  # choosing a random joke from the list and splitting that list into two sublists
    who = joke[0]  # the who is the first element of the list
    await ctx.send(who)

    # waiting for user to send "{message that bot just sent} who?" it will timeout in 60 seconds
    message = f"{who} who?"

    def check1(msg):
        return msg.content == message and msg.channel == ctx.channel and msg.author == ctx.author

    await client.wait_for("message", check=check1, timeout=60.0)

    await ctx.send(joke[1])  # sending second element in joke sublist


client.run(TOKEN)
