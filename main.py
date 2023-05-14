# Made by DankoOfficial on Github
# Discord: $ky#4280
# Dont skid, I'll catch you I swear. Give credits
# vc = Valid Cookie
# vcr = Valid Cookie Robux
# vcf = Valid Cookie Full

import aiohttp
import discord
from discord.ext import commands

config = { 
    
    "token": "token",
    "prefix": ".",

}

bot = commands.Bot(
    command_prefix=config['prefix'],
    intents=discord.Intents.all(),
    help_command=None,
    activity=discord.Activity(type=discord.ActivityType.watching,name=f".help | Checking your Roblox Cookies")
    
)

@bot.event
async def on_ready():
    print(f"""Successfully Connected To [{bot.user}]\n\n[!] Logs will be sent here""")

@bot.command()
async def help(ctx):
    await ctx.reply(f'**{config["prefix"]}vc**: Checks if the cookie is vaild\n**{config["prefix"]}vcr**: Returns robux info about the cookie\n**{config["prefix"]}vcf**: Returns intensive info about the cookie.')

@bot.command()
async def vc(ctx, *, text):
    await ctx.message.delete()
    async with aiohttp.ClientSession(cookies={'.ROBLOSECURITY': text}) as session:
        try:
            async with session.get('https://www.roblox.com/mobileapi/userinfo') as response:
                embedVar = discord.Embed(title=":white_check_mark: Valid Cookie", description="", color=0x38d13b)
                embedVar1 = discord.Embed(title=":white_check_mark: Cookie", description='```'+text+'```', color=0x38d13b)
                embedVar.add_field(name="Passed Cookie: ", value='```                       Hidden                  ```', inline=False)
                dmch = await ctx.author.create_dm()
                await dmch.send(embed=embedVar1)
                await ctx.send(embed=embedVar)
        except:
            embedVar = discord.Embed(title=":x: Invalid Cookie", description="", color=0xFF0000)
            embedVar.add_field(name="Passed Cookie: ", value='```                       Hidden                  ```', inline=False)
            await ctx.send(embed=embedVar)
                
@bot.command()
async def vcr(ctx, *, text):
    await ctx.message.delete()
    async with aiohttp.ClientSession(cookies={'.ROBLOSECURITY': text}) as session:
        try:
            async with session.get('https://www.roblox.com/mobileapi/userinfo') as response:
                robux = (await response.json())['RobuxBalance']
                embedVar = discord.Embed(title=":white_check_mark: Valid Cookie", description="", color=0x38d13b)
                embedVar1 = discord.Embed(title=":white_check_mark: Cookie", description='```' + text + '```',color=0x38d13b)
                embedVar1.add_field(name="Robux", value='```' + str(robux) + '```', inline=False)
                embedVar.add_field(name="Passed Cookie: ", value='```                       Hidden                  ```', inline=False)
                embedVar.add_field(name="Robux", value='**' + str(robux) + '**', inline=False)
                dmch = await ctx.author.create_dm()
                await dmch.send(embed=embedVar1)
                await ctx.send(embed=embedVar)
        except:
            embedVar = discord.Embed(title=":x: Invalid Cookie", description="", color=0xFF0000)
            embedVar.add_field(name="Passed Cookie: ", value='```                       Hidden                  ```', inline=False)
            await ctx.send(embed=embedVar)

@bot.command()
async def vcf(ctx, *, text):
    await ctx.send('**Please wait we are fetching info...**')
    await ctx.message.delete()
    async with aiohttp.ClientSession(cookies={'.ROBLOSECURITY': text}) as session:
        try:
            async with session.get('https://www.roblox.com/mobileapi/userinfo') as resp:
                    robux = (await resp.json())['RobuxBalance']
                    thumbnail = (await resp.json())['ThumbnailUrl']
        except:
            return await ctx.send("Invalid .ROBLOSECURITY cookie.")
        async with session.get('https://billing.roblox.com/v1/credit') as resp:
            credit_robux = (await resp.json())['robuxAmount']
        async with session.get('https://www.roblox.com/my/settings/json') as resp:
            full_info = await resp.json()
            user_id = full_info['UserId']
            account_age = full_info['AccountAgeInDays']
            display_name = full_info['DisplayName']
            is_premium = full_info['IsPremium']
            is_admin = full_info['IsAdmin']
            is_birthdate_locked = full_info['IsBirthdateLocked']
            name = full_info['Name']
            requires_2fa_email = full_info['ChangeEmailRequiresTwoStepVerification']
            requires_2fa_password = full_info['ChangePasswordRequiresTwoStepVerification']
            user_above_13 = full_info['UserAbove13']
        try:
            async with session.get('https://accountsettings.roblox.com/v1/email') as resp:
                email_address = (await resp.json())['emailAddress']
                email_verified = (await resp.json())['verified']
                email = f"Email: {email_address} | is Email Verified: {email_verified}"
        except:
            email = "Email: No Email"
        async with session.get('https://friends.roblox.com/v1/my/friends/count') as resp:
            friends = (await resp.json())['count']
        async with session.get('https://friends.roblox.com/v1/user/friend-requests/count') as resp:
            friend_requests = (await resp.json())['count']
        async with session.get('https://voice.roblox.com/v1/settings') as resp:
            is_verified_voice = (await resp.json())['isVerifiedForVoice']
        async with session.get('https://accountinformation.roblox.com/v1/phone') as resp:
            try:
                phone_data = await resp.json()
                country_code = phone_data['countryCode']
                is_phone_verified = phone_data['isVerified']
                phone = phone_data['phone']
                phones = f'Phone Number: {phone} | is Phone Verified: {is_phone_verified} | Country: {country_code}'
            except:
                phones = 'Phone: None'
        async with session.get(f'https://groups.roblox.com/v2/users/{user_id}/groups/roles') as resp:
            try:
                groups_data = await resp.json()
                groups_roles = []
                for group in groups_data['data']:
                    group_id = group['group']['id']
                    group_name = group['group']['name']
                    role = group['role']['name']
                    groups_roles.append(f'**Name**: {group_name} | **Role**: {role}')
                groups = f"\n".join(groups_roles)
            except:
                groups = "No Groups"
        embed = discord.Embed(title=f"**{display_name} ({name})**", color=discord.Color.green())
        embed.set_thumbnail(url=f"{thumbnail}")
        embed.add_field(name="Robux Balance", value=f"{robux} R$", inline=True)
        embed.add_field(name="Credit Balance", value=f"{credit_robux} R$", inline=True)
        embed.add_field(name="Premium", value=is_premium, inline=True)
        embed.add_field(name="Admin", value=is_admin, inline=True)
        embed.add_field(name="Account Age", value=f"{account_age} Days", inline=True)
        embed.add_field(name="User Above 13", value=user_above_13, inline=True)
        embed.add_field(name="Voice Verification", value=is_verified_voice, inline=True)
        embed.add_field(name="Friends", value=friends, inline=True)
        embed.add_field(name="2FA Email Verification", value=requires_2fa_email, inline=True)
        embed.add_field(name="2FA Password Verification", value=requires_2fa_password, inline=True)
        embed.add_field(name="Birthdate Locked", value=is_birthdate_locked, inline=True)
        embed.add_field(name="Friend Requests", value=friend_requests, inline=True)
        embed.add_field(name="Email Verification", value=email, inline=False)
        embed.add_field(name="Phone Verification", value=phones, inline=False)
        embed.add_field(name="Groups", value=groups, inline=False)
        await ctx.send(embed=embed)

bot.run(config['token'])
