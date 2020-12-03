import random

from discord.ext import commands

from request import get_game_picture

from settings import DISCORD_TOKEN

bot = commands.Bot(command_prefix='!')


@bot.command()
async def info(ctx):
    """Get Bot commands info."""

    await ctx.send("for choosing **game** : !game *game1, game2, game3*")
    await ctx.send("for choosing **another** : !choose *word1, word2, word3*")


@bot.command()
async def game(ctx, *args):
    """Choose a game."""

    games = ' '.join(args).split(',')
    # await ctx.send("{} possibilités: {}".format(len(games), ', '.join(games)))
    game = random.choice(games).capitalize()
    await ctx.send(game)

    try:
        game_picture_url = get_game_picture(game)
        await ctx.send(game_picture_url)
    except IndexError:
        await ctx.send("> Pas d'image trouvée")


@bot.command()
async def choose(ctx, *args):
    """Choose a random."""

    choice = ' '.join(args).split(',')
    await ctx.send(random.choice(choice))

bot.run(DISCORD_TOKEN)
