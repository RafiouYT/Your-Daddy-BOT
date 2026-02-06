import os
import discord
from discord.ext import commands
import google.generativeai as genai

# Secrets/Environment Variables theke data neya
DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
GEMINI_API_KEY = os.environ['GEMINI_API_KEY']

# Gemini AI Setup
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a savage roasting bot. Speak in a mix of Banglish and Hindlish. Be very funny, sarcastic, and roast users who mention you. Use words like 'Bhai', 'Aukaat', 'Abey', 'Gadhe', 'Chamcha'."
)

# Discord Bot Setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} ekhon online!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Bot-ke mention korle roast korbe
    if bot.user.mentioned_in(message):
        user_msg = message.content
        prompt = f"User said: {user_msg}. Roast them badly in Banglish-Hindlish mix style."
        
        response = model.generate_content(prompt)
        await message.reply(response.text)

    await bot.process_commands(message)

bot.run(DISCORD_TOKEN)
