from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Lasiya = InlineKeyboardMarkup([
        
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/Danuma_admin_bot")],
        [InlineKeyboardButton(
            "📣 Support channel 📣",url="https://t.me/danumabots")]
    ])
    thumbnail_url = "https://telegra.ph/file/0777bb5a6b5e947a1d9af.jpg"
    await message.reply_photo(thumbnail_url, caption=f"Hey<b>{message.from_user.first_name}.I'm UTUBE DOWNLODER BOT.</b>\n\n<b>Instructions for use..</b>\n• Type /help to get instructins.\n• Type /tute for make a bot like me.\n───── ❝ **E PUSTHAKALAYA BOTs™** ❞ ─────\n ", reply_markup=Lasiya)
    raise StopPropagation
