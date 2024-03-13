import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    @nextcord.slash_command(description="Sends a list of bot commands")
    async def help(self, interaction: Interaction):
        await interaction.response.send_message("None... as of now ;)")
       
    @nextcord.slash_command(description="Sends bot latency")
    async def ping(self, interaction: Interaction):
        latency = int(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! My latency is {latency} ms!")
        
    @nextcord.slash_command(description="Sends info about the current server")
    async def serverinfo(self, interaction: Interaction):
        guild = interaction.guild
        name = guild.name
        await interaction.response.send_message(f"Name: {name}")
        
    @nextcord.slash_command(description="Sends info about the given user")
    async def userinfo(self, interaction: Interaction, member: Member = None):
        if member is None:
            member = interaction.user
        name = member.mention
        await interaction.response.send_message(name)

    @nextcord.slash_command(description="Sends the given users avatar")
    async def avatar(self, interaction: Interaction, member: Member = None):
        if member is None:
            member = interaction.user
        name = member.name
        avatar = member.avatar
        
        embed = nextcord.Embed(
            color=0x4584B6,
            title=f"{name}'s Avatar:"
        )
        embed.set_image(url=avatar)

        await interaction.response.send_message(embed=embed)
        
def setup(bot):
    bot.add_cog(Information(bot))
