# main.py - 全境封鎖2 Discord Bot
import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
from gear_data import (
    gear_info, 
    gear_recommendations, 
    weapon_types, 
    skills, 
    game_mechanics, 
    game_modes, 
    enemy_types,
    weapon_talents,
    equipment_mods,
    special_equipment,
    game_tips,
    improvised_gear,
    enemy_factions,
    game_story
)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# 設定正確的 Intents
intents = discord.Intents.default()
intents.message_content = True  # 啟用 Message Content Intent
intents.guilds = True
intents.guild_messages = True

# 移除前綴，專注於斜線指令
bot = commands.Bot(command_prefix=None, intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    print(f"已登入為 {bot.user}")
    print(f"Bot ID: {bot.user.id}")
    print(f"Bot 在 {len(bot.guilds)} 個伺服器中")
    
    try:
        # 強制同步所有指令
        print("正在同步指令...")
        synced = await tree.sync()
        print(f"已同步 {len(synced)} 個指令")
        
        # 列出所有已註冊的指令
        print("已註冊的指令：")
        for cmd in tree.get_commands():
            print(f"  - /{cmd.name}: {cmd.description}")
            
    except Exception as e:
        print(f"同步失敗: {e}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        # 忽略前綴指令錯誤
        return
    print(f"指令錯誤: {error}")

@tree.command(name="gear", description="查詢裝備效果（輸入完整名稱）")
@app_commands.describe(name="裝備名稱")
async def gear(interaction: discord.Interaction, name: str):
    print(f"收到 gear 指令: {name}")
    info = gear_info.get(name)
    if info:
        embed = discord.Embed(
            title=f"🔍 {name}",
            description=info,
            color=0x00ff00
        )
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(f"❌ 找不到裝備「{name}」，請確認名稱是否正確。")

@tree.command(name="improvised", description="查詢臨時裝備資訊")
@app_commands.describe(gear_type="臨時裝備類型")
async def improvised(interaction: discord.Interaction, gear_type: str):
    print(f"收到 improvised 指令: {gear_type}")
    info = improvised_gear.get(gear_type)
    if info:
        embed = discord.Embed(
            title=f"🔧 {gear_type}",
            description=info,
            color=0xffaa00
        )
        await interaction.response.send_message(embed=embed)
    else:
        available_gear = "、".join(improvised_gear.keys())
        await interaction.response.send_message(f"❌ 沒有找到「{gear_type}」的臨時裝備。\n可用的類型：{available_gear}")

@tree.command(name="build", description="查詢推薦套裝配法（例如：突擊、狙擊、坦克、技能、爆擊、獵人、臨時）")
@app_commands.describe(style="風格類型")
async def recommend(interaction: discord.Interaction, style: str):
    print(f"收到 build 指令: {style}")
    rec = gear_recommendations.get(style.lower())
    if rec:
        embed = discord.Embed(
            title=f"📦 {style} 推薦套裝",
            description=rec,
            color=0x0099ff
        )
        await interaction.response.send_message(embed=embed)
    else:
        available_styles = "、".join(gear_recommendations.keys())
        await interaction.response.send_message(f"❌ 沒有找到「{style}」的推薦套裝類型。\n可用的類型：{available_styles}")

@tree.command(name="weapon", description="查詢武器類型資訊")
@app_commands.describe(weapon_type="武器類型")
async def weapon(interaction: discord.Interaction, weapon_type: str):
    print(f"收到 weapon 指令: {weapon_type}")
    info = weapon_types.get(weapon_type)
    if info:
        embed = discord.Embed(
            title=f"🔫 {weapon_type}",
            description=info,
            color=0xff6600
        )
        await interaction.response.send_message(embed=embed)
    else:
        available_weapons = "、".join(weapon_types.keys())
        await interaction.response.send_message(f"❌ 沒有找到「{weapon_type}」的武器類型。\n可用的類型：{available_weapons}")

@tree.command(name="talent", description="查詢武器天賦資訊")
@app_commands.describe(talent_name="天賦名稱")
async def talent(interaction: discord.Interaction, talent_name: str):
    print(f"收到 talent 指令: {talent_name}")
    info = weapon_talents.get(talent_name)
    if info:
        embed = discord.Embed(
            title=f"⚔️ {talent_name}",
            description=info,
            color=0xff8800
        )
        await interaction.response.send_message(embed=embed)
    else:
        available_talents = "、".join(weapon_talents.keys())
        await interaction.response.send_message(f"❌ 沒有找到「{talent_name}」的武器天賦。\n可用的天賦：{available_talents}")

@tree.command(name="mod", description="查詢裝備模組資訊")
@app_commands.describe(mod_name="模組名稱")
async def mod(interaction: discord.Interaction, mod_name: str):
    print(f"收到 mod 指令: {mod_name}")
    info = equipment_mods.get(mod_name)
    if info:
        embed = discord.Embed(
            title=f"🔧 {mod_name}",
            description=info,
            color=0x8888ff
        )
        await interaction.response.send_message(embed=embed)
    else:
        available_mods = "、".join(equipment_mods.keys())
        await interaction.response.send_message(f"❌ 沒有找到「{mod_name}」的裝備模組。\n可用的模組：{available_mods}")

@tree.command(name="special", description="查詢特殊裝備資訊")
@app_commands.describe(equipment_name="特殊裝備名稱")
async def special(interaction: discord.Interaction, equipment_name: str):
    print(f"收到 special 指令: {equipment_name}")
    info = special_equipment.get(equipment_name)
    if info:
        embed = discord.Embed(
            title=f"🌟 {equipment_name}",
            description=info,
            color=0xff00ff
        )
        await interaction.response.send_message(embed=embed)
    else:
        available_equipment = "、".join(special_equipment.keys())
        await interaction.response.send_message(f"❌ 沒有找到「{equipment_name}」的特殊裝備。\n可用的特殊裝備：{available_equipment}")

@tree.command(name="skill", description="查詢技能資訊")
@app_commands.describe(skill_name="技能名稱")
async def skill(interaction: discord.Interaction, skill_name: str):
    print(f"收到 skill 指令: {skill_name}")
    info = skills.get(skill_name)
    if info:
        embed = discord.Embed(
            title=f"⚡ {skill_name}",
            description=info,
            color=0x9933ff
        )
        await interaction.response.send_message(embed=embed)
    else:
        available_skills = "、".join(skills.keys())
        await interaction.response.send_message(f"❌ 沒有找到「{skill_name}」的技能。\n可用的技能：{available_skills}")

@tree.command(name="mechanic", description="查詢遊戲機制說明")
@app_commands.describe(mechanic="機制名稱")
async def mechanic(interaction: discord.Interaction, mechanic: str):
    print(f"收到 mechanic 指令: {mechanic}")
    info = game_mechanics.get(mechanic)
    if info:
        embed = discord.Embed(
            title=f"⚙️ {mechanic}",
            description=info,
            color=0xffcc00
        )
        await interaction.response.send_message(embed=embed)
    else:
        available_mechanics = "、".join(game_mechanics.keys())
        await interaction.response.send_message(f"❌ 沒有找到「{mechanic}」的機制。\n可用的機制：{available_mechanics}")

@tree.command(name="gamemode", description="查詢遊戲模式資訊")
@app_commands.describe(mode="模式名稱")
async def game_mode(interaction: discord.Interaction, mode: str):
    print(f"收到 gamemode 指令: {mode}")
    info = game_modes.get(mode)
    if info:
        embed = discord.Embed(
            title=f"🎮 {mode}",
            description=info,
            color=0xff0066
        )
        await interaction.response.send_message(embed=embed)
    else:
        available_modes = "、".join(game_modes.keys())
        await interaction.response.send_message(f"❌ 沒有找到「{mode}」的遊戲模式。\n可用的模式：{available_modes}")

@tree.command(name="enemy", description="查詢敵人類型資訊")
@app_commands.describe(enemy="敵人名稱")
async def enemy(interaction: discord.Interaction, enemy: str):
    print(f"收到 enemy 指令: {enemy}")
    info = enemy_types.get(enemy)
    if info:
        embed = discord.Embed(
            title=f"👹 {enemy}",
            description=info,
            color=0xff0000
        )
        await interaction.response.send_message(embed=embed)
    else:
        available_enemies = "、".join(enemy_types.keys())
        await interaction.response.send_message(f"❌ 沒有找到「{enemy}」的敵人類型。\n可用的敵人：{available_enemies}")

@tree.command(name="faction", description="查詢敵方陣營背景故事")
@app_commands.describe(faction="陣營名稱")
async def faction(interaction: discord.Interaction, faction: str):
    print(f"收到 faction 指令: {faction}")
    info = enemy_factions.get(faction)
    if info:
        embed = discord.Embed(
            title=f"🏛️ {faction} 陣營",
            description=info,
            color=0x8b0000
        )
        embed.set_footer(text="使用 /enemy [敵人名稱] 查詢具體敵人資訊")
        await interaction.response.send_message(embed=embed)
    else:
        available_factions = "、".join(enemy_factions.keys())
        await interaction.response.send_message(f"❌ 沒有找到「{faction}」的陣營。\n可用的陣營：{available_factions}")

@tree.command(name="story", description="查詢遊戲劇情故事")
@app_commands.describe(story="故事主題")
async def story(interaction: discord.Interaction, story: str):
    print(f"收到 story 指令: {story}")
    info = game_story.get(story)
    if info:
        embed = discord.Embed(
            title=f"📖 {story}",
            description=info,
            color=0x9932cc
        )
        embed.set_footer(text="使用 /faction [陣營名稱] 查詢敵方陣營資訊")
        await interaction.response.send_message(embed=embed)
    else:
        available_stories = "、".join(game_story.keys())
        await interaction.response.send_message(f"❌ 沒有找到「{story}」的劇情故事。\n可用的故事：{available_stories}")

@tree.command(name="tip", description="查詢遊戲提示")
@app_commands.describe(tip_type="提示類型")
async def tip(interaction: discord.Interaction, tip_type: str):
    print(f"收到 tip 指令: {tip_type}")
    info = game_tips.get(tip_type)
    if info:
        embed = discord.Embed(
            title=f"💡 {tip_type} 提示",
            description=info,
            color=0x00ffff
        )
        await interaction.response.send_message(embed=embed)
    else:
        available_tips = "、".join(game_tips.keys())
        await interaction.response.send_message(f"❌ 沒有找到「{tip_type}」的遊戲提示。\n可用的提示類型：{available_tips}")

@tree.command(name="brands", description="顯示所有可用的品牌套裝")
async def brand_list(interaction: discord.Interaction):
    print("收到 brands 指令")
    brands = list(gear_info.keys())
    brands_text = "、".join(brands)
    embed = discord.Embed(
        title="🏷️ 品牌套裝列表",
        description=f"可用的品牌套裝：\n{brands_text}",
        color=0x00ccff
    )
    await interaction.response.send_message(embed=embed)

@tree.command(name="help", description="顯示所有可用指令")
async def help_command(interaction: discord.Interaction):
    print("收到 help 指令")
    embed = discord.Embed(
        title="🤖 全境封鎖2 Bot 幫助",
        description="以下是所有可用的指令：",
        color=0x00ff00
    )
    
    commands_info = [
        ("/gear [名稱]", "查詢特定裝備的詳細資訊"),
        ("/improvised [類型]", "查詢臨時裝備的詳細資訊"),
        ("/build [類型]", "查詢特定風格的推薦配裝"),
        ("/weapon [類型]", "查詢武器類型的特點和推薦"),
        ("/talent [名稱]", "查詢武器天賦的詳細資訊"),
        ("/mod [名稱]", "查詢裝備模組的詳細資訊"),
        ("/special [名稱]", "查詢特殊裝備的詳細資訊"),
        ("/skill [名稱]", "查詢技能的詳細資訊"),
        ("/mechanic [名稱]", "查詢遊戲機制的說明"),
        ("/gamemode [模式]", "查詢遊戲模式的資訊"),
        ("/enemy [名稱]", "查詢敵人類型的特點和弱點"),
        ("/faction [名稱]", "查詢敵方陣營的背景故事"),
        ("/story [主題]", "查詢遊戲劇情故事"),
        ("/tip [類型]", "查詢遊戲提示"),
        ("/brands", "顯示所有可用的品牌套裝"),
        ("/help", "顯示此幫助訊息")
    ]
    
    for cmd, desc in commands_info:
        embed.add_field(name=cmd, value=desc, inline=False)
    
    embed.set_footer(text="使用 /gear [品牌名稱] 來查詢詳細資訊")
    await interaction.response.send_message(embed=embed)

bot.run(TOKEN)
