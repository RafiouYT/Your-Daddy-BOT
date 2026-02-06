import os
import discord
from discord.ext import commands
import google.generativeai as genai

# Secrets theke data neya
DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
GEMINI_API_KEY = os.environ['GEMINI_API_KEY']

# Gemini AI Setup
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Discord Bot Setup
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} online hoyeche!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message):
        try:
            response = model.generate_content(f"Roast this person in Banglish: {message.content}")
            await message.reply(response.text)
        except Exception as e:
            print(f"Error: {e}")
            await message.reply(f"Abe error ho gaya: {e}")

    await bot.process_commands(message)

bot.run(DISCORD_TOKEN)
