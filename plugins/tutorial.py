from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(Filters.command(["tute"]))
async def start(client, message):
    await message.reply_text("To make a YouTube downloader press ⚜️ Go ⚜️ button to go youtube directly. 🥳",
                             reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("⚜️ Go ⚜️", url="https://youtu.be/l6rTppg3a1w")]
        ]))
    
