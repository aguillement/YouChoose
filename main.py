from discord.ext import commands


import discord
import os
import random
import requests

bot = commands.Bot(command_prefix='!')

"""
Get Bot commands info.
"""
@bot.command()
async def info(ctx):
    await ctx.send("for choosing **game** : !game *game1, game2, game3*")
    await ctx.send("for choosing **another** : !choose *word1, word2, word3*")

"""
Choose a game.
"""
@bot.command()
async def game(ctx, *args):
    games = ' '.join(args).split(',')
    #await ctx.send("{} possibilités: {}".format(len(games), ', '.join(games)))
    #await ctx.send(random.choice(games))

    game = random.choice(games)
    # TODO CALL API LIKE : get_game_picture(game)


"""
Choose a random.
"""
@bot.command()
async def choose(ctx, *args):
    choice = ' '.join(args).split(',')
    await ctx.send(random.choice(choice))

bot.run(os.getenv("DISCORD_TOKEN"))