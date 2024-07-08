
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from ANNIEMUSIC import app

#--------------------------

MUST_JOIN = "KGF_ROCY"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
    photo="https://telegra.ph/file/dfde87c32f8951c6b7628.jpg",
    caption=f"According to my database, you haven't joined Support yet. If you want to use me, please join Support and start interacting with me again!",
    reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Join", url=link)],
        ]
    )
)
