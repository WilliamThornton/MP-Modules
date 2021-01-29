import re
import discord
from discord import member
from discord.ext import commands
import Phoinex








#Enter prefix That Will Be The Start Of A Chat Command example-> command_prefix="!" How To Use Command In Chat-> !clear 2
client = commands.Bot(command_prefix="!")
































if client.command_prefix == "":
    print("Pleas Enter Command Prefix In Moddy!")
    input()
    quit()
def MModPackage():
    #kick
    @client.command()
    async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    #ban
    @client.command()
    async def ban(ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)

    #mute
    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                              read_messages=False)

        await member.add_roles(mutedRole, reason=reason)
        await ctx.send(f"Muted {member.mention} for reason {reason}")
        await member.send(f"You Are Muted In {guild.name} For {reason}")


    #unmute
    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        await ctx.send(f"Unmuted {member.mention}")
        await member.send(f"You Are Unmuted From {ctx.guild.name}")

#run
def MRun(Mtoken):
    client.run(Mtoken)

#Bot Ready
def MBotReady():
    @client.event
    async def on_ready():
        print(f"{client.user} Is Ready")



def DM():

    @client.command()
    async def dm(ctx, member: discord.Member, reason):
        guild = ctx.guild
        await member.send(reason)

def Clear():
    @client.command()
    async def clear(ctx, amount=2):
        await ctx.channel.purge(limit=amount)


def AutoMakeBot():
    # Bot Is Ready
    @client.event
    async def on_ready():
        await client.change_presence(status=discord.Status.online, activity=discord.Game("With A TBAR"))
        print(f"{client.user} Is Ready!")

    #mute
    @client.command()
    async def mute(ctx, member: discord.Member, reason=None):
            muted = discord.utils.get(ctx.guild.roles, name="Muted")
            await member.add_roles(muted)
            await ctx.send(f"{member} Has Been Muted!")
            print(f"{member} Got mute")
    #unmute
    @client.command()
    async def unmute(ctx, member: discord.Member, reason=None):
            muted = discord.utils.get(ctx.guild.roles, name="Muted")
            await member.remove_roles(muted)
            await ctx.send(f"{member} Has Been UnMuted!")
            print(f"{member} Got Unmute")


    #Bot dm
    @client.command()
    async def dm(ctx, member: discord.Member, reason):
        guild = ctx.guild
        await member.send(reason)
        print(f"{member} Got DM")

    # Clear Messages
    @client.command()
    async def clear(ctx, amount=2):
        await ctx.channel.purge(limit=amount)
        print("Clear Message")

    # kick
    @client.command()
    async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.channel.purge(limit=1)
        print(f"{member} Got Kick")

    # ban
    @client.command()
    async def ban(ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.channel.purge(limit=1)
        print(f"{member} Got Ban")

    # change bot status
    @client.command()
    async def status(ctx, statuss):
        await client.change_presence(status=discord.Status.online, activity=discord.Game(statuss))
        await ctx.channel.purge(limit=1)
        print("Changed Cstatus")
