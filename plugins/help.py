from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	Lasiya2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("🤖 Bot List 🤖", url="https://t.me/epusthakalaya_bots/7")],
		 ])
	help_image = "https://telegra.ph/file/2a5b44ea2f0a4b0a03f41.jpg"
	await message.reply_photo(help_image,  caption="**♔ HELP MENU ♔**\n• Just Send your Youtube video url. \n• And I will give Method list to select your choice.\n\n**♔සිංහල උදව්**\n• කොපි කරගත් Youtube ලින්කුව එවන්න.\n• එවිට ලැබෙන ලැයිස්තුවෙන් අවශ්‍ය පමාණය හා මාදිලිය තෝරාදෙන්න.\n\n\n **• Powered By;**\n• @epusthakalaya_bots.",reply_markup=Lasiya2)
