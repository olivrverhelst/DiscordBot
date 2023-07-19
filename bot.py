from email import message

import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!', help_command=None)
client = discord.Client()


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Being gay and slaying'))


def randomly(pronouns1, pronouns2, name):
    random_sentences = [f"I just met a lovely person named {name}. {pronouns1} was really nice and would love to meet {pronouns2} again.",
                        f"Today I'm going to see someone named {name}. I'm really excited as I've heard that {pronouns1} is really nice.",
                        f"In class today, I met a new friend. {pronouns1} is called {name}. I'm so happy I met {pronouns2} as {pronouns1} is really smart and very nice as well. I can't wait till I meet {pronouns2} again"]

    n = random.randrange(0, len(random_sentences))
    return random_sentences[n]


@bot.command()
async def pronouns(message, pronoun1, pronoun2, name):
    await message.send('Hey {}, you want to try on {}/{} pronouns'.format(name, pronoun1, pronoun2))
    await message.channel.send(randomly(pronoun1, pronoun2, name))


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    if message.author == client.user:
        return

    if "trans" in message.content.lower():
        await message.channel.send("Trans rights!!", tts=True)
        await message.channel.send("Transgender:\n"
                                   "1 Adj. : a gender description for someone who has transitioned (or is transitioning) \n"
                                   "from living as one gender to another.\n\n"
                                   "2 Adj. : an umbrella term for anyone whose sex assigned at birth and gender identity do not correspond in the expected way\n"
                                   " (e.g., someone who was assigned male at birth, but does not identify as a man).")

    if "gay" in message.content.lower():
        await message.channel.send("Gay rights!!", tts=True)
        await message.channel.send("Gay:\n"
                                   "used in mainly two ways. \n"
                                   "The first is for individuals solely attracted to the same gender, often men who only likes men. \n"
                                   "The second use for the word is for any queer individual.")

    if "lesbian" in message.content.lower():
        await message.channel.send("Lesbian rights!!", tts=True)
        await message.channel.send("Lesbian\n"
                                   "used to refer to non-men who are attracted only to other non-men")

    if "bi" in message.content.lower():
        await message.channel.send("Bi rights!!", tts=True)
        await message.channel.send("Bisexual:\n"
                                   "Term used for individuals who are attracted to two or more genders, often with a preference")

    if "pan" in message.content.lower():
        await message.channel.send("Pan rights!!", tts=True)
        await message.channel.send("Pansexual: \n"
                                   "Term used for people who are attracted to all gender without a preference")

    if "ace" in message.content.lower():
        await message.channel.send("Ace rights!!", tts=True)
        await message.channel.send("Asexual:\n"
                                   "Used for people who experience little to no sexual attraction")

    if "aro" in message.content.lower():
        await message.channel.send("Aro rights!!", tts=True)
        await message.channel.send("Aromantic:"
                                   "Used for people who experience little to no romantic attraction")




@bot.command()
async def help(message):
    await message.send("This bot has two different commands you could use. \n"
                       "A pronouns command which allows you to try on new pronouns and a new name, this command is triggered by using '!pronouns [pronoun1] [pronoun2] [name]'\n"
                       "The other command/s makes the bot say [identity] rights! and its belonging definition. To trigger this one use the command '![trans/gay/bi/pan/ace/aro]")


bot.run("token")
