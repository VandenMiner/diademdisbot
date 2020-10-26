from discord.ext import commands
from discord.utils import get
import os
import discord
import asyncio


intents = discord.Intents.all()
ds = commands.Bot(command_prefix='!', intents = intents)
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
async def on_raw_reaction_add(reaction):
	channel = ds.get_channel(reaction.channel_id)
	user = reaction.member
	guild = ds.get_guild(701453861679792195)
	сhannel1 = ds.get_channel(768411788264865802)
	if channel == сhannel1:
		emb = discord.Embed()
		emb.add_field(name = ":white_check_mark: Вы установили себе роль Игрок :white_check_mark: ", value = """Теперь вам доступны большинство каналов
	дискорд-сервера **Diadem**. 
	Для того чтобы снять роль - просто уберите свою реакцию.""")
		emb.color = discord.Colour.green()
		emb.set_thumbnail(url = "https://images-ext-1.discordapp.net/external/1AXiajN3xjbjin6VR-J4QNOG4Gy4wPP-uabVCUGMAp0/https/media.discordapp.net/attachments/713367810985689110/714404218777239614/anim.gif")
		await user.send(embed = emb)
		role = discord.utils.get(guild.roles, name="Игрок")
		role2 = discord.utils.get(guild.roles, name="Без роли")
		await user.add_roles(role)
		await user.remove_roles(role2)
@ds.event
async def on_raw_reaction_remove(reaction):
	channel = ds.get_channel(reaction.channel_id)
	сhannel1 = ds.get_channel(768411788264865802)
	if channel == сhannel1:
		guild = ds.get_guild(reaction.guild_id)
		print(str(reaction.user_id))
		user = discord.utils.get(guild.members, id = reaction.user_id)
		emb = discord.Embed()
		emb.add_field(name = ":x: Вы сняли с себя роль Игрок :x: ", value = """Вы потеряли доступ к большинству каналов. 
	Для того чтобы вернуть роль - просто поставте реакцию""")
		emb.color = discord.Colour.red()
		emb.set_thumbnail(url = "https://images-ext-1.discordapp.net/external/1AXiajN3xjbjin6VR-J4QNOG4Gy4wPP-uabVCUGMAp0/https/media.discordapp.net/attachments/713367810985689110/714404218777239614/anim.gif")
		await user.send(embed = emb)
		role = guild.get_role(713365777033592834)
		role2 = discord.utils.get(guild.roles, name="Без роли")
		await user.remove_roles(role)
		await user.add_roles(role2)

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
@ds.event
async def on_ready():
    await ds.change_presence(status=discord.Status.online, activity=discord.Game("Minecraft"))
    print("Запуск")



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

#1

 @ds.command(
  name="mc",
  aliases=["майн", "мс", "minecraft", "mine"],
  brief="Информация о Minecraft сервере",
  usage="mc <ip> [port]",
  description="Информация о Minecraft сервере")
 async def _mc(self, ctx, ip, port=None):
  message = await ctx.send("Идёт сбор информации, пожалуйста подождите.")

  if port is None:
   server = MinecraftServer.lookup(f"{ip}:25565")
  else:
   try:
    server = MinecraftServer.lookup(f"{ip}:{port}")
   except ValueError:
    embed = discord.Embed(title="Ошибка Подключения", description="Порт вне допустимого диапазона **0-65535**.",
           color=0xb20000)
    await message.delete()
    return await ctx.send(embed=embed)

  try:
   server_ping = server.ping()
   server_status = server.status()

  except socket.timeout:
   players = "`❌ Не Доступно`"
   version = "`❌ Не Доступно`"
   description = "`❌ Не Доступно`" 
   ping = "`❌ Не Доступно`"
   status = "🔴 Отключен"

  except socket.gaierror:
   embed = discord.Embed(title="Ошибка Ввода", description="Вы ввели не действительный IP или Порт.", color=0xb20000)
   await message.delete()
   return await ctx.send(embed=embed)

  except IOError as error:
   embed = discord.Embed(title="Ошибка Подключение", description="Мне не удалось получить информацию с этого сервера.\n"
                    "Возможно у него стоит какая-та защита.\n\n"
                    f"`Ошибка: {error}`",
          color=0xb20000)
   await message.delete()
   return await ctx.send(embed=embed)

  else:
   players = f"{server_status.players.online}/{server_status.players.max}"
   version = server_status.version.name

   if 'extra' in server_status.description:
    description = f"\n- {server_status.description['extra'][0]['text']}\n" \
         f"- {server_status.description['extra'][1]['text']}\n" \
         f"- {server_status.description['extra'][2]['text']}"
   else:
    description = server_status.description['text']

   ping = server_ping
   status = "🟢 Включен"

  if status == "🟢 Включен":
   try:
    server_query = server.query()

   except socket.timeout:
    query = "Query отключен на сервере"

   else:
    query = f"**Хост:** {server_query.host}\n" \
      f"**Софт:** {server_query.software}\n" \
      f"**MOTD:** {server_query.motd}\n" \
      f"**Плагины:** {''.join(server_query.plugins)}\n" \
      f"**Игроки:** {', '.join(server_query.players.names)}"

  else:
   query = "`❌ Не Доступно`"

  embed = discord.Embed(
   title="Статус Travedit Сервер",
   description=f"**IP:** {ip}\n"
      f"**Описание:** {description}\n"
      f"**Версия:** {version}",
   color=0xFF7F3F)
  embed.add_field(name="Игроки", value=players, inline=False)
  embed.add_field(name="Статус", value=status, inline=False)
  embed.add_field(name="Пинг", value=ping, inline=False)
  embed.add_field(name="Данные через Query",
      value=query,
      inline=False)

  await message.edit(content=None, embed=embed)
token = os.environ.get("BOT_TOKEN")

ds.run(token)
