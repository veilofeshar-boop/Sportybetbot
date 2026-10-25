import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Optional for now

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# ========== COMMANDS ==========

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Hey! I'm your private Football & Basketball assistant.\n\n"
        "What I can do right now:\n"
        "• Analyze matches\n"
        "• Help with SportyBet tickets\n"
        "• Research form & H2H\n"
        "• Track your bets (coming next)\n\n"
        "Just talk to me normally or use:\n"
        "/analyze <team1 vs team2>\n"
        "/code <paste SportyBet code>\n"
        "/help"
    )

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "<b>Commands</b>\n"
        "/start - Welcome message\n"
        "/analyze Manchester United vs Liverpool\n"
        "/code PASTE_YOUR_SPORTYBET_CODE\n"
        "/note <your note> - Save personal note\n\n"
        "You can also just type normally, e.g.\n"
        "\"What do you think about Arsenal vs Chelsea today?\""
    )

@dp.message(Command("analyze"))
async def cmd_analyze(message: types.Message):
    query = message.text.replace("/analyze", "").strip()
    if not query:
        await message.answer("Please write the match.\nExample: /analyze Arsenal vs Chelsea")
        return

    await message.answer(f"Analyzing: <b>{query}</b>\n\n(This is the starter version. Full stats + AI analysis coming in next update.)")
    
    # Placeholder – we will upgrade this with real data + AI
    await message.answer(
        f"<b>Quick Take on {query}</b>\n"
        "• I need live data connection for deep analysis.\n"
        "• Next version will pull form, H2H, xG, injuries etc."
    )

@dp.message(Command("code"))
async def cmd_code(message: types.Message):
    code = message.text.replace("/code", "").strip()
    if not code:
        await message.answer("Paste your SportyBet code after the command.\nExample: /code ABC123XYZ")
        return

    await message.answer(
        f"<b>SportyBet Code Received</b>\n<code>{code}</code>\n\n"
        "I can help you:\n"
        "• Split this ticket\n"
        "• Remove weak games\n"
        "• Change markets\n"
        "• Give risk assessment\n\n"
        "Reply with what you want me to do with it."
    )

@dp.message(Command("note"))
async def cmd_note(message: types.Message):
    note = message.text.replace("/note", "").strip()
    if note:
        # Later we will save this properly
        await message.answer(f"Note saved:\n{note}")
    else:
        await message.answer("Write something after /note")

# Normal messages (natural language)
@dp.message()
async def handle sn_message(message: types.Message):
    text = message.text.lower()

    if any(word in text for word in ["hello", "hi", "hey"]):
        await message.answer("Yes boss, I'm here. What do you need?")
    elif "sporty" in text or "code" in text:
        await message.answer("Send the code with /code followed by the code, or just paste it and tell me what to do.")
    else:
        await message.answer(
            "I heard you.\n\n"
            "For now use:\n"
            "• /analyze Team A vs Team B\n"
            "• /code YOUR_SPORTYBET_CODE\n\n"
            "Full natural conversation + deep analysis is coming in the next upgrade."
        )

# ========== RUN ==========

async def main():
    print("Bot is starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
