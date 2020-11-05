import discord
import random
from discord.ext import commands


class CommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', aliases=['latency'])
    @commands.guild_only()
    async def ping(self, ctx):
        """Command which pings the bot"""
        phrase=["I am alive...",
                "I was definitely not sleeping...",
                "I'm still here",
                "You are using a ping command? Why?",
                "You disturbed me. I was sleeping man....",
                "At your service.",
                "Yah the bot's online.",
                "Hiiiiiii",
                "boink",
                "beep boop, boop beep",
                "Why you playin' ping pong."]
        ph=random.choice(phrase)
        lsm = round((self.bot.latency) * 100)
        embed = discord.Embed(title='**pong...!**', description=f"_{ph}_ \n**~{lsm} ms taken**...", color=discord.Color.gold())

        await ctx.send(content=None, embed=embed)

    @commands.command(name='echo', aliases=['copy', 'mimic'])
    async def echo(self, ctx, *, our_input: str):
        """A simple command which repeats our input"""
        await ctx.send(our_input)

    @commands.command(name='embedexample', aliases=['embedexample'])
    async def embed(self, ctx):
        embed = discord.Embed(title='**EMBED EXAMPLE**',description="Here's some stuff...",color=discord.Color.green())

        embed.add_field(name='Field1', value='val1')
        embed.add_field(name='Field2', value='val2', inline=False)
        embed.add_field(name='Field3', value='val3', inline=False)
        embed.add_field(name='Field4', value='val4')
        embed.add_field(name='Field5', value='val5')
        embed.add_field(name='Field6', value='val6')
        embed.add_field(name='Field7', value='val7')
        embed.add_field(name='Field8', value='val8')
        embed.add_field(name='Field9', value='val9')
        embed.add_field(name='Field10', value='val10')
        embed.set_footer(text='<footer-text>')
        await ctx.send(embed=embed)

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case CommandsCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(CommandsCog(bot))
