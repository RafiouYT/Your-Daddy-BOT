import os
import discord
from discord.ext import commands
import google.generativeai as genai

# Secrets theke data neya
DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
GEMINI_API_KEY = os.environ['GEMINI_API_KEY']

# Gemini AI Setup
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", # Ebar flash try koro, library update hole eta kaj korbe
    system_instruction="You are a savage roasting bot named Your-Daddy. Speak in a mix of Banglish and Hindlish. Be very funny, sarcastic, and roast users who mention you."
)

# Discord Bot Setup
intents = discord.Intents.default()
intents.message_content = True 
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
        prompt = f"User said: {user_msg}. Roast them badly in Banglish-Hindlish style."
        
        try:
            response = model.generate_content(prompt)
            await message.reply(response.text)
        except Exception as e:
            print(f"Error: {e}")
            # Jodi Flash model ekhono kaj na kore, tobe ai error message-ta asbe
            await message.reply("Arey bhai, thora rukh! API error ho raha hai. (Model name issue)")

    await bot.process_commands(message)

bot.run(DISCORD_TOKEN)
