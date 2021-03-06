# CONFIG
# ---------
token = "NTcyMTIzNTU2NzI1NTIyNDcz.XN8zjA.LEyio-Nc4XOaBAQFk_FQXNaDIsU" # This is what the bot uses to log into Discord.
prefix = "emb/" # This will be used at the start of commands.
embed_role = "Embed Creator" # The role in your server used for embedding.
game = "with embeds!" # This will display as the game on Discord.
# ----------

from discord.ext import commands
from discord.ext.commands import Bot
import discord

bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Ready when you are. ;)") 
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    await bot.change_presence(activity=discord.Game(name=game))

@bot.command(pass_context=True)
async def help(ctx):
    channeldd = ctx.message.channel
    embed = discord.Embed(title="Help!", description="Basically, this is how I'm used.", color=0x00a0ea)
    embed.add_field(name="{}embed".format(prefix), value="Creates a quick embed with the users input after the command is called.")
    embed.add_field(name="{}rembed".format(prefix), value="Let's you embed with more user input. After entering your message the bot will ask questions about the color and thumbnail.")
    embed.set_footer(text="Embed Creator")
    await channeldd.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_role(embed_role)
async def rembed(ctx, *, a_sMessage):
    channeldd = ctx.message.channel
    color = None
    thumb = None
    embed_color = discord.Embed(title="🕑 Tick-Tock", description="Would you like to use a **custom color**? If **yes**, state it. If **no** simply say *no*.", color=0xffff00)
    embed_color.set_footer(text="Simply type a color name such as green in plaintext.")
    embed_thumb = discord.Embed(title="🕑 Tick-Tock", description="Would you like to use a **custom thumbnail**? If **yes**, state it. If **no** simply say *no*.", color=0xffff00)
    embed_thumb.set_footer(text="Simply type an image URL in plaintext.")
    await bot.delete_message(ctx.message)
    ques1 = await bot.send_message(ctx.message.channel, embed=embed_color)
    ques1
    msg = await bot.wait_for_message(author=ctx.message.author, timeout=60)
    if msg.content.lower() == "green":
        await bot.delete_message(ques1)
        await bot.delete_message(msg)
        color = 0x00ff00
        ques2 = await channeldd.send(embed=embed_thumb)
        ques2
    elif msg.content.lower() == "yellow":
        await bot.delete_message(ques1)
        await bot.delete_message(msg)
        color = 0xFFFF00
        ques2 = await channeldd.send(embed=embed_thumb)
        ques2
    elif msg.content.lower() == "blue":
        await bot.delete_message(ques1)
        await bot.delete_message(msg)
        color = 0x0000ff
        ques2 = await channeldd.send(embed=embed_thumb)
        ques2
    elif msg.content.lower() == "red":
        await bot.delete_message(ques1)
        await bot.delete_message(msg)
        color = 0xff0000
        ques2 = await channeldd.send(embed=embed_thumb)
        ques2
    else:
        await bot.delete_message(ques1)
        await bot.delete_message(msg)
        color = 0x00a0ea
        ques2 = await channeldd.send(embed=embed_thumb)
        ques2
    msg = await bot.wait_for_message(author=ctx.message.author, timeout=60)
    if msg.content.lower() == "no":
        await bot.delete_message(ques2)
        await bot.delete_message(msg)
        thumb = ctx.message.author.avatar_url
    else:
        await bot.delete_message(ques2)
        await bot.delete_message(msg)
        thumb = msg.content
    embed = discord.Embed(description=a_sMessage, color=color)
    embed.set_thumbnail(url=thumb)
    embed.set_author(name=ctx.message.author.name + " says..")
    embed.set_footer(text="Embed-This!")
    await channeldd.send(embed=embed)
    print(ctx.message.author.name + " has embedded a message in " + ctx.message.server.name)

@bot.command(pass_context=True)
@commands.has_role(embed_role)
async def embed(ctx, *, a_sMessage):
    channeldd = ctx.message.channel
    embed = discord.Embed(description=a_sMessage, color=0x00a0ea)
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    embed.set_author(name=ctx.message.author.name + " says..")
    embed.set_footer(text="Embed Creator")
    await bot.delete_message(ctx.message)
    await channeldd.send(embed=embed)
    print(ctx.message.author.name + " has embedded a message in " + ctx.message.server.name)

bot.run(token)
