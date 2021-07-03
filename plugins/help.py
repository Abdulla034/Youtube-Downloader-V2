from pyrogram import Client, Filters


@Client.on_message(Filters.command(["start"]))
async def start(client, message):
    helptxt = f"Hal-hazırda yalnız Youtube Single-i dəstəkləyir (Pleylist yoxdur) Sadəcə Youtubeden Linki Kopyalayib Buraya Yapışdırın"
    await message.reply_text(helptxt)
