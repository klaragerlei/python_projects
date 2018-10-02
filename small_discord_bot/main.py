# import the discord.py module
import discord
from discord.ext import commands

# put in the token or prefix of your bot to make it work for you
# WARNING: put these in a credentials file on a real bot, never put them in plain text in your code like this
bot_token = "put your bot's token here"
bot_prefix = "put your bot's command prefix here"

# create the bot object
bot = commands.AutoShardedBot(
    command_prefix=bot_prefix, description="A simple discord bot!"
)

# this will only get called when this file gets called directly
if __name__ == '__main__':
    # lists the different extensions of the bot
    extensions = [
        "base_commands"
    ]

    # loads each extension and will catch it if an exception happens, printing that it failed
    for ext in extensions:
        try:
            bot.load_extension("plugins." + ext + ".py")
        except (ImportError, discord.ClientException):
            print(f'Failed to load extension {ext}.')


# making sure that the bot will never react to another bot that tries to command it
@bot.check
async def no_bots(ctx):
    return not ctx.author.bot


# creating an event that gets called when the bot is ready
# (is connected to the discord api and has populated its cache)
@bot.event
async def on_ready():
    print("Ready!")

# running the bot
bot.run(bot_token)
