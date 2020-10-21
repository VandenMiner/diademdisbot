



from discord.ext import commands
from discord.utils import get
import os
import discord
import asyncio



ds = commands.Bot(command_prefix='!')
@ds.event
async def on_ready():
    await ds.change_presence(status=discord.Status.online, activity=discord.Game("илюшка гей"))
    print("Запуск")
@ds.event
async def on_raw_reaction_add(reaction):
	channel = ds.get_channel(reaction.channel_id)
	user = reaction.member
	guild = ds.get_guild(701453861679792195)
	сhannel1 = ds.get_channel(768411788264865802)
	if channel == сhannel1:
		role = discord.utils.get(guild.roles, name="Игрок")
		role2 = discord.utils.get(guild.roles, name="Без роли")
		await user.add_roles(role)
		await user.remove_roles(role2)
@ds.event
async def on_raw_reaction_remove(reaction):
	channel = ds.get_channel(reaction.channel_id)
	guild = ds.get_guild(701453861679792195)
	user = guild.get_member(reaction.user_id)
	сhannel1 = ds.get_channel(768411788264865802)
	if channel == сhannel1:
		role = guild.get_role(713365777033592834)
		role2 = discord.utils.get(guild.roles, name="Без роли")
		await user.remove_roles(role)
		await user.add_roles(role2)
@ds.event
async def on_member_join(member):
    channel = ds.get_channel(713305916044214292)


    vk = get(ds.emojis, name='vk')
    twitch = get(ds.emojis, name='twitch')

    role = discord.utils.get(member.guild.roles, name="Без роли")
    await member.add_roles(role)


    await channel.send(f"Приветствую тебя, {member.mention} :wave:")
    emb = discord.Embed()
    emb.color = discord.Colour.gold()
    emb.add_field(name = "⁣⁣⁣ ", value = f"""**В первую очередь рекомендуем получить**
**роль для доступа ко всем каналам**
**:closed_lock_with_key:[Получить роль](https://discord.gg/Bv85HnT)**

**Для комфортного времяпрепровождения**
**рекомендуем озокомиться с**
**:clipboard:[Правилами Discord](https://discord.gg/YGXUGva)**

**Полезные ссылки:**
{vk}[Группа Вк](https://vk.com/diadem.mine)
{twitch}[Twitch](https://www.twitch.tv/d1adem_)""")
    emb.set_thumbnail(url = "https://images-ext-1.discordapp.net/external/1AXiajN3xjbjin6VR-J4QNOG4Gy4wPP-uabVCUGMAp0/https/media.discordapp.net/attachments/713367810985689110/714404218777239614/anim.gif")
    emb.set_author(name = """Добро пожаловать в  официальный Discord 
 канал проекта Diadem!""", icon_url=member.avatar_url)

    await channel.send(embed = emb)
@ds.event
async def on_voice_state_update(member,before,after):
    if after.channel.id == 718359790778318918:
        for guild in ds.guilds:
            if guild.id == 701453861679792195:
                mainCategory = discord.utils.get(guild.categories, id=718359671403970620)
                channel2 = await guild.create_voice_channel(name=f"{member.display_name}",category=mainCategory)
                await member.move_to(channel2)
                await channel2.set_permissions(member,manage_channels=True)
                def check(a,b,c):
                    return len(channel2.members) == 0
                await ds.wait_for('voice_state_update', check=check)
                await channel2.delete()




@ds.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def член(ctx, amount = 1000):
	await ctx.channel.send("ахаха дурак")


@ds.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def clear(ctx, amount = 1000):
	await ctx.channel.purge(limit = amount)

@ds.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def message(ctx, arg):
	if arg == "1":

		diadem = get(ds.emojis, name='Diadem')
		role = discord.utils.get(ctx.guild.roles, name="Игрок")

		emb = discord.Embed()
		emb.color = discord.Colour.gold()
		emb.add_field(name = " ‏", value=f"""**Вы можете самостоятельно добавить/убрать себе**
**нужную роль нажав на нужную эмоцию под данным**
**сообщением!**
		
{diadem} - {role.mention}
""")
		emb.set_footer(text = "Нажимая на данную эмоцию вы автоматически соглашаетесь со всеми правилами поведения на вашем дискорд сервере.")
		emb.set_author(name = "Роли дискорд-канала Diadem. ", icon_url="https://images-ext-1.discordapp.net/external/dMIAfxxizvGvN8yAjHE1rIEZlZo44PJEt2i2oneBoYM/https/images-ext-1.discordapp.net/external/8U-ni-iOMzcYx-9W3FV5BwlGTNikVeRxEH3E5hYnKzA/https/media.discordapp.net/attachments/713367810985689110/714478708747927592/unknown.png")
		emb.set_thumbnail(url = "https://images-ext-1.discordapp.net/external/1AXiajN3xjbjin6VR-J4QNOG4Gy4wPP-uabVCUGMAp0/https/media.discordapp.net/attachments/713367810985689110/714404218777239614/anim.gif")
		reactionm = await ctx.channel.send(embed = emb)
		await reactionm.add_reaction(diadem)

token = os.environ.get("BOT_TOKEN")

ds.run(token)
#@ds.event
#async def on_reaction_add(reaction, user)
#	if reaction.message ==
