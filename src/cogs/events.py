import discord
from discord.ext import commands



class EventsCog(commands.Cog):
    """EventsCog"""

    """
    @commands.command(name='me')
    @commands.is_owner()
    async def only_me(self, ctx):
        '''Command which only responds to the owner of the bot.'''

        await ctx.send(f'Hello {ctx.author.mention}. This command can only be used by you!!')
    """

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        """Event Listener which is called when a user is banned from the guild
        For more info:
        http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_member_ban
        """
        print(f'{user} was banned from {guild.name}-{guild.id}')


    @commands.Cog.listener()
    async def on_member_join(self, guild, user):
        """Event listener which is called when a user joins the guild
        For more info:
        http://discord.py.readthedocs.io/en/rewrite/api.html#discord.on_member_join
        """
        print(f'{user} joined {guild.name}-{guild.id}')


    @commands.Cog.listener()
    async def on_member_remove(self, guild, user):
        """Event listener which is called when a user leaves the guild
        For more info:
        http://discord.py.readthedocs.io/en/rewrite/api.html#discord.on_member_remove
        """
        print(f'{user} has left {guild.name}-{guild.id}')

# The setup function below is neccesarry. Remember we give bot.add_cog() the name of the class in this case EventsCog.
def setup(bot):
    bot.add_cog(EventsCog(bot))
