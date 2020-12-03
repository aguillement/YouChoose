from request import get_game_picture

from discord.ext import commands

import discord
import os
import random

from settings import DISCORD_TOKEN

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

curl 'https://api.igdb.com/v4/games' 
-d 'search "rocket league"; fields screenshots.*;' 
-H 'Client-ID: ftg6d5z0xjj1u2n3i9cdbr5g1tyapu' 
-H 'Authorization: Bearer hfuah3bcm88lxtzmkgwh0ksjxsm4f7' 
-H 'Accept: application/json'
"""
@bot.command()
async def game(ctx, *args):
    games = ' '.join(args).split(',')
    #await ctx.send("{} possibilités: {}".format(len(games), ', '.join(games)))
    game = random.choice(games)
    await ctx.send(game)

    game_picture_url = get_game_picture(game)
    await ctx.send(game_picture_url)


"""
Choose a random.
"""
@bot.command()
async def choose(ctx, *args):
    choice = ' '.join(args).split(',')
    await ctx.send(random.choice(choice))

bot.run(DISCORD_TOKEN)