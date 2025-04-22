# bot.py

import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_ID, API_HASH, BOT_TOKEN
from utils.logger import setup_logger
from utils.theme import WELCOME_MESSAGES
from utils.format_text import generate_order_format
from utils.database import update_mapping

setup_logger()

app = Client(
    "blakeshley_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    chat_id = message.chat.id

    try:
        # Teks pertama
        first = await client.send_message(chat_id, WELCOME_MESSAGES[0])
        await asyncio.sleep(3)
        await first.delete()

        # Teks kedua
        second = await client.send_message(chat_id, WELCOME_MESSAGES[1])
        await asyncio.sleep(3)
        await second.delete()

        # Teks ketiga + menu
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("ᯓ ✎ format your wishes ✎", callback_data="format")]
        ])
        await client.send_message(
            chat_id,
            WELCOME_MESSAGES[2],
            reply_markup=keyboard
        )

    except Exception as e:
        app.logger.error(f"Terjadi kesalahan saat mengirim pesan start: {e}")

@app.on_callback_query(filters.regex("format"))
async def format_button(client, callback_query):
    try:
        await callback_query.answer()
        username = callback_query.from_user.username or "username"

        text = generate_order_format(username)

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("ᯓ ✎ Copy Here", switch_inline_query_current_chat=text)]
        ])

        # Kirim format
        formatted_text = f"*Copy and Paste This:*\n\n```{text}```"
        sent = await callback_query.message.reply_text(
            formatted_text,
            parse_mode="Markdown",
            reply_markup=keyboard
        )

        await asyncio.sleep(420)  # 7 menit
        await sent.delete()

        try:
            await callback_query.message.delete()
        except Exception as e:
            app.logger.warning(f"Gagal menghapus pesan tombol format: {e}")

        await client.send_message(
            callback_query.message.chat.id,
            "༄ the magic fades into the mist... ༄"
        )

    except Exception as e:
        app.logger.error(f"Terjadi kesalahan dalam alur tombol format: {e}")

if __name__ == "__main__":
    app.run()