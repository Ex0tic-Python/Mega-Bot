# Made for Python 3.10 (Match statements are cool)
# Library Imports
import discord as disc
from json import load
from dotenv import load_dotenv
from os import getenv

# File Imports
from helper_methods import prefix_loader


def bot_initiation():
    # Loads bot info and creates bot instance
    with open(r'Cogs_And_Other\Data_Files\bot_info.json', 'r') as json_file:
        json_data = load(json_file)
    
    json_intents_data = json_data['Intents']
    intents = disc.Intents(
        guilds = json_intents_data['guilds'],
        members = json_intents_data['members'],
        moderation = json_intents_data['moderation'],
        emojis_and_stickers = json_intents_data['emojis_and_stickers'],
        integrations = json_intents_data['integrations'],
        webhooks = json_intents_data['webhooks'],
        invites = json_intents_data['invites'],
        voice_states = json_intents_data['voice_states'],
        presences = json_intents_data['presences'],
        messages = json_intents_data['messages'],
        reactions = json_intents_data['reactions'],
        typing = json_intents_data['typing'],
        message_content = json_intents_data['message_content'],
        guild_scheduled_events = json_intents_data['guild_scheduled_events'],
        auto_moderation = json_intents_data['auto_moderation']
    )

    bot = disc.ext.commands.Bot(
        prefix = prefix_loader,
        case_insensitive
    )
    
    load_dotenv()
    bot_token = getenv('bot_token')
    bot.run(bot_token)



if __name__ == '__main__':
    bot_initiation()
    
    
    
    
# -------------------------------------------------------------------------------


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


bot.run('token')
