import discord
intents = discord.Intents.all()
client = discord.Client(intents=intents)
p = 0
Prefix = '!'


############################### help commands ########################################
page = 0
pages = [
    
            [Prefix +"ping" ,'infinite pings'],
            [Prefix +"drake", 'what is drake doing'],
            [Prefix +"poggers", 'poggers'],
            [Prefix +"haryanvi", 'haryanvi dads after 8 pm'],
            [Prefix +"andrewtate", 'tate saves the world'],
            [Prefix +"ratlore", 'rat lore'],
            [Prefix +"tomholland", 'cutie tom'],
            [Prefix +"mrbeast", 'mrbeast one piece'],
            [Prefix +"spiderman", 'spiderman in mall'],
            [Prefix +"allahu","allahu"],
            [Prefix + "monkeygrandad",'']
            
            
            
            ]
max_fields_per_page = 10
######################################################################################


@client.event
async def on_ready():
    global p
    global Prefix
    print("bot is ready")
    print("Prefix is",Prefix)

@client.event



async def on_message(message):
    global p
    global Prefix
    global page
    global pages 
    global max_fields_per_page

    if message.content.startswith(Prefix + "help"):
        
        embed = discord.Embed(title="Command List", description="some cute commands", color=0x000000)
        for i in range(page * max_fields_per_page, (page + 1) * max_fields_per_page):
            if i >= len(pages):
                break
            embed.add_field(name=pages[i][0], value=pages[i][1], inline = False)
        embed.set_footer(text=f"Page {page+1}/{len(pages)//max_fields_per_page + 1}")
        sent_message = await message.channel.send(embed=embed)
        await sent_message.add_reaction("⬅️")
        await sent_message.add_reaction("➡️")

    elif message.content.startswith(Prefix + "ping"):
        p = 0
        for user in message.mentions:
            while True:
                if p == 1:
                    break
                await message.channel.send(user.mention)
    elif message.content.startswith(Prefix + "pstop"):
        p = 1
        print("Stopped")
    
    elif message.content.startswith(Prefix +"pingev"):
        print("claled pinge")
        while True:
            await message.channel.send("@everyone")

    elif message.content.startswith(Prefix +"drake"):
        print("drake called")
        channel = message.channel
        embed = discord.Embed(title="drake?", description="", color=0x000000)
        embed.set_image(url='https://cdn.discordapp.com/attachments/850766412204605500/857499270302269450/image0_1.gif')
        await channel.send(embed=embed)
    
    elif message.content.startswith(Prefix + "ratlore"):
        print("ratlore called")
        channel = message.channel
        embed = discord.Embed(title="", description="", color=0x000000)
        embed.set_image(url='https://media.tenor.com/t4NkMssGmJAAAAAd/rat-lore-lore.gif')
        await channel.send(embed=embed)
    
    elif message.content.startswith(Prefix +"poggers"):
        print("poggers called")
        channel = message.channel
        await message.channel.send("https://cdn.discordapp.com/attachments/717382550233940059/781442681065701376/video0.mov")
    
    elif message.content.startswith(Prefix +"andrewtate"):
        print("tate called")
        channel = message.channel
        await message.channel.send("https://media.discordapp.net/attachments/725255664783589387/1007915222897537174/D2E1D6C7-66F6-42E0-8119-C03C4AC2EC1F.gif")

    elif message.content.startswith(Prefix +"haryanvi"):
        print("haryanvi called")
        channel = message.channel
        await message.channel.send("https://cdn.discordapp.com/attachments/714789621405450313/992500088779837510/sheikhyoboooty-20220630-0002.mp4")

    elif message.content.startswith(Prefix +"mrbeast"):
        print("mrbeast called")
        channel = message.channel
        await message.channel.send("https://cdn.discordapp.com/attachments/882353430193123350/1028882206921342996/evilosakerfan53-11082022-0001.mp4")
    
    elif message.content.startswith(Prefix +"spiderman"):
        print("spiderman called")
        channel = message.channel
        await message.channel.send("https://cdn.discordapp.com/attachments/752603729189929070/953318724469940324/spiderman_in_mall-1.mp4")
    
    elif message.content.startswith(Prefix +"tomholland"):
        print("tomholland called")
        channel = message.channel
        await message.channel.send("https://cdn.discordapp.com/attachments/837565719499636756/930986109448630342/Tom_Holland-1-1.mp4")
    
    elif message.content.startswith(Prefix +"allahu"):
        print("allahu called")
        channel = message.channel
        await message.channel.send("*auzubillah minash shaitan irajeem bismillah irrahman irrahim*")
    
    elif message.content.startswith(Prefix +"monkeygrandad"):
        print("allahu called")
        channel = message.channel
        await message.channel.send("https://cdn.discordapp.com/attachments/411350982807519233/490949855435554839/6abba58c-31bc-437b-bc70-de8cac1d9b44.mp4")

    elif message.content.startswith(Prefix +"prefix"):
        Message = message.content.split()
        Prefix = Message[1]
        print("new prefix is" + Message[1])
       


    
    

    

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    













async def on_reaction_add(reaction, user):
    global page
    message = reaction.message
    if message.author == client.user and user != client.user:
        if str(reaction.emoji) == "⬅️":
            if page > 0:
                page -= 1
        elif str(reaction.emoji) == "➡️":
            if page < len(pages)//max_fields_per_page:
                page += 1
        embed = discord.Embed(title="Command List", description="some cute commands", color=0x000000)
        for i in range(page * max_fields_per_page, (page + 1) * max_fields_per_page):
            if i >= len(pages):
                break
            embed.add_field(name=pages[i][0], value=pages[i][1], inline = False)
        embed.set_footer(text=f"Page {page+1}/{len(pages)//max_fields_per_page + 1}")
        await message.edit(embed=embed)
        await message.remove_reaction(reaction.emoji, user)

















    
    

    

    

    
client.event(on_reaction_add)
client.run("MTA2NTA2NzU3ODU1ODUxMzIyMg.GPcq2c.lsI7oTqUSramLPNkXqLj12_i9Ocyyy-XtrLM-E")