from email import message

import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!', help_command=None)
client = discord.Client()


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Trans guy shit'))


def randomly(pronouns1, pronouns2, name):
    random_sentences = [f"I just met a lovely person named {name}. {pronouns1} was really nice and would love to meet {pronouns2} again.",
                        f"Today I'm going to see someone named {name}. I'm really excited as I've heard that {pronouns1} is really nice.",
                        f"In class today, I met a new friend. {pronouns1} is called {name}. I'm so happy I met {pronouns2} as {pronouns1} is really smart and very nice as well. I can't wait till I meet {pronouns2} again"]

    n = random.randrange(0, len(random_sentences))
    return random_sentences[n]


@bot.command()
async def test(message, pronoun1, pronoun2, name):
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
                                   "1 Adj. : experiencing attraction solely (or primarily) to some members of the same gender.\n"
                                   "Can be used to refer to non-men who are attracted only to other non-men and non-women who are only attracted to non-women.\n\n"
                                   "2 Adj. : an umbrella term used to refer to the queer community as a whole, \n"
                                   "or as an individual identity label for anyone who is not straight")

    if "lesbian" in message.content.lower():
        await message.channel.send("Lesbian rights!!", tts=True)
        await message.channel.send("Lesbian\n"
                                   "used to refer to non-men who are attracted only to other non-men")

    if "bi" in message.content.lower():
        await message.channel.send("Bi rights!!", tts=True)
        await message.channel.send("Bisexual:\n"
                                   "1 noun & adj. : a person who experiences attraction to some men and women.\n\n"
                                   "2 adj. : a person who experiences attraction to some people of their gender and another gender.\n"
                                   "Bisexual attraction does not have to be equally split, \n"
                                   "or indicate a level of interest that is the same across the genders an individual may be attracted to. \n""")

    if "pan" in message.content.lower():
        await message.channel.send("Pan rights!!", tts=True)
        await message.channel.send("Pansexual: \n"
                                   "Adj. : a person who experiences sexual, romantic, physical, and/or spiritual attraction \n"
                                   "for members of all gender identities/expressions, usually with no preference of  gender")

    if "ace" in message.content.lower():
        await message.channel.send("Ace rights!!", tts=True)
        await message.channel.send("Asexual:\n"
                                   "Adj. : experiencing little or no sexual attraction to others and/or a lack of interest in sexual relationships/behavior.\n"
                                   "Asexuality exists on a continuum from people who experience no sexual attraction or have any desire for sex,\n"
                                   "to those who experience low levels, or sexual attraction only under specific conditions.\n"
                                   "Sometimes abbreviated to ace")

    if "aro" in message.content.lower():
        await message.channel.send("Aro rights!!", tts=True)
        await message.channel.send("Aromantic:"
                                   "Adj. : experiencing little or no romantic attraction to others and/or has a lack of interest in romantic relationships/behavior.\n"
                                   "Aromanticism exists on a continuum from people who experience no romantic attraction or have any desire for romantic activities,\n"
                                   "to those who experience low levels, or romantic attraction only under specific conditions.\n"
                                   "Many of these different places on the continuum have their own identity labels. \n"
                                   "Sometimes abbreviated to “aro” (pronounced like “arrow”).")




@bot.command()
async def help(message):
    await message.send("This bot is made so that you can try on new pronouns. \n"
                       "To do that write: !test [pronoun1] [pronoun2] [name]. \n"
                       "An example of how that could look like is: !test he them Alex")


bot.run("token")
