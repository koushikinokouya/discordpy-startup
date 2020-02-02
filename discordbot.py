from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    if message.content.startswith('&instinct-team'):
        role = discord.utils.get(message.guild.roles, name='instinct-team')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 追加しました！'
        await message.channel.send(reply)
    if message.content.startswith('$instinct-team'):
        role = discord.utils.get(message.guild.roles, name='instinct-team')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention} 解除しました！'
        await message.channel.send(reply)
    if message.content.startswith('&valor-team'):
        role = discord.utils.get(message.guild.roles, name='valor-team')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 追加しました！'
        await message.channel.send(reply)
    if message.content.startswith('$valor-team'):
        role = discord.utils.get(message.guild.roles, name='valor-team')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention} 解除しました！'
        await message.channel.send(reply)
    if message.content.startswith('&mystic-team'):
        role = discord.utils.get(message.guild.roles, name='mystic-team')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 追加しました！'
        await message.channel.send(reply)
    if message.content.startswith('$mystic-team'):
        role = discord.utils.get(message.guild.roles, name='mystic-team')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention} 解除しました！'
        await message.channel.send(reply)
    if message.content.startswith('&hunt-100'):
        role = discord.utils.get(message.guild.roles, name='hunt-100')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 追加しました！'
        await message.channel.send(reply)
    if message.content.startswith('$hunt-100'):
        role = discord.utils.get(message.guild.roles, name='hunt-100')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention} 解除しました！'
        await message.channel.send(reply)
    if message.content.startswith('&hunt-candy'):
        role = discord.utils.get(message.guild.roles, name='hunt-candy')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 追加しました！'
        await message.channel.send(reply)
    if message.content.startswith('$hunt-candy'):
        role = discord.utils.get(message.guild.roles, name='hunt-candy')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention} 解除しました！'
        await message.channel.send(reply)
    if message.content.startswith('&reid-JP'):
        role = discord.utils.get(message.guild.roles, name='reid-JP')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 追加しました！'
        await message.channel.send(reply)
    if message.content.startswith('$reid-JP'):
        role = discord.utils.get(message.guild.roles, name='reid-JP')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention} 解除しました！'
        await message.channel.send(reply)
    if message.content.startswith('&support'):
        role = discord.utils.get(message.guild.roles, name='support')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 追加しました！'
        await message.channel.send(reply)
    if message.content.startswith('$support'):
        role = discord.utils.get(message.guild.roles, name='support')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention} 解除しました！'
        await message.channel.send(reply)
    if message.content.startswith('&research-nest'):
        role = discord.utils.get(message.guild.roles, name='research-nest')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 追加しました！'
        await message.channel.send(reply)
    if message.content.startswith('$research-nest'):
        role = discord.utils.get(message.guild.roles, name='research-nest')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention} 解除しました！'
        await message.channel.send(reply)
    if message.content.startswith('&pvp-friends'):
        role = discord.utils.get(message.guild.roles, name='pvp-friends')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 追加しました！'
        await message.channel.send(reply)
    if message.content.startswith('$pvp-friends'):
        role = discord.utils.get(message.guild.roles, name='pvp-friends')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention} 解除しました！'
        await message.channel.send(reply)
    if message.content.startswith('&friend-code'):
        role = discord.utils.get(message.guild.roles, name='friend-code')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 追加しました！'
        await message.channel.send(reply)
    if message.content.startswith('$friend-code'):
        role = discord.utils.get(message.guild.roles, name='friend-code')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention} 解除しました！'
        await message.channel.send(reply)
    if message.content.startswith('&hunt-quest'):
        role = discord.utils.get(message.guild.roles, name='hunt-quest')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 追加しました！'
        await message.channel.send(reply)
    if message.content.startswith('$hunt-quest'):
        role = discord.utils.get(message.guild.roles, name='hunt-quest')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention} 解除しました！'
        await message.channel.send(reply)
    if message.content.startswith('&ios-spc'):
        role = discord.utils.get(message.guild.roles, name='ios-spc')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 追加しました！'
        await message.channel.send(reply)
    if message.content.startswith('$ios-spc'):
        role = discord.utils.get(message.guild.roles, name='ios-spc')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention} 解除しました！'
        await message.channel.send(reply)
    if message.content.startswith('&android-spc'):
        role = discord.utils.get(message.guild.roles, name='android-spc')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 追加しました！'
        await message.channel.send(reply)
    if message.content.startswith('$android-spc'):
        role = discord.utils.get(message.guild.roles, name='android-spc')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention} 解除しました！'
        await message.channel.send(reply)
    if message.content.startswith('&Jail-spc'):
        role = discord.utils.get(message.guild.roles, name='Jail-spc')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 追加しました！'
        await message.channel.send(reply)
    if message.content.startswith('$candy-trip'):
        role = discord.utils.get(message.guild.roles, name='candy-trip')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention} 解除しました！'
        await message.channel.send(reply)
    if message.content.startswith('$candy-trip'):
        role = discord.utils.get(message.guild.roles, name='candy-trip')
        await message.author.remove_roles(role)
        reply = f'{message.author.mention} 解除しました！'
        await message.channel.send(reply)

bot.run(token)
