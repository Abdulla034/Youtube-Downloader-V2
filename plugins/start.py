from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Sahib", url="https://t.me/ShirnovCefer")],
    ])
    welcomed = f"Salam <b>{message.from_user.first_name}</b>\nHal-hazırda yalnız Youtube Single-i dəstəkləyir (Pleylist yoxdur) Sadəcə Youtubeden Linki Kopyalayib Buraya Yapışdırın"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
