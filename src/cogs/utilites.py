import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
def setup(bot):
    bot.add_cog(Utilities(bot))