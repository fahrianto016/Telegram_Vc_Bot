from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME


@Client.on_message(filters.command(["start", "start@DARKXV2BOT"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**HALOO TELASOO👋🏻 {}!**\n\n *SAYA ARSUL BOT YG SUNGGUH AMAZING YG BISA MEMUTAR LAGU DI GC KALIAN[😉]!**\n\n**KLIK /cmdlist UNTUK BANTUAN PERINTAH❤**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("★тαмвαнкαη gυα кє g¢ ℓυ★", url="https://t.me/DARKXV2BOT?startgroup=true")
            ],[
            InlineKeyboardButton("★𝙶𝚁𝚄𝙿𝙺𝚄★", url="https://t.me/areasulawesi"),
            InlineKeyboardButton("★𝙲𝙷𝙰𝙽𝙽𝙴𝙻★", url="https://t.me/Rakyatsulawesi")
            ],[
            InlineKeyboardButton("★𝙾𝚆𝙽𝙴𝚁 𝙸𝙽𝙸 𝙱𝙾𝚃★", url="http://t.me/tummingrockers")
            ]]
        ),
        disable_web_page_preview=True
    )
        
@Client.on_message(filters.command(["start", "start@DARKXV2BOT"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**♥︎ᴄᴏʙʀᴀᴍᴜsɪᴄʙᴏᴛ ɪs ᴏɴʟɪɴᴇ♥︎**",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="♥︎sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ♥︎", url="https://t.me/areasulawesi")
            ]]
        )
    )


@Client.on_message(filters.command(["cmdlist", "start@DARKXV2BOT"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**𓆩ᴄᴏʙʀᴀᴍᴜsɪᴄʙᴏᴛ𓆪 :ʜᴇʟᴘ ᴍᴇɴᴜ**

__×𓆩ʀ𓆪 ♥︎Fɪʀsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ..
__×𓆩ʀ𓆪 ♥︎ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀS ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀʟʟ ᴘᴇʀᴍɪSSɪᴏɴ♥︎ ..__

**𓆩ʀ𓆪 ♥︎ᴄᴏᴍᴍᴏɴ ᴄᴏᴍᴍᴀɴᴅs♥︎.**

• `/ᴘʟᴀʏ` - Sᴏɴɢ ɴᴀᴍᴇ : __ᴘʟᴀʏ ᴠɪᴀ ʏᴏᴜᴛᴜʙᴇ__
• `/ᴅᴘʟᴀʏ` - Sσηg ɴᴀᴍᴇ : __ᴘʟᴀʏ ᴠɪᴀ ᴅᴇᴇᴢᴇʀ__
• `/Sᴘʟᴀʏ` - Sᴏɴɢ ɴᴀᴍᴇ : __ᴘʟᴀʏ ᴠɪᴀ ᴊɪᴏ sᴀᴀᴠɴ__
• `/ᴘʟᴀʏʟɪsᴛ` - __sʜᴏᴡ ɴᴏᴡ ᴘʟᴀʏʟɪsᴛ__
• `/ᴄᴜʀʀᴇɴᴛ` - __sʜᴏᴡ ɴᴏᴡ ᴘʟᴀʏɪɴɢ__

• `/sᴏɴɢ` - sᴏɴɢ ɴᴀᴍᴇ : __ɢᴇᴛ ᴛʜᴇ sᴏɴɢ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ__
• `/vid` - Video Name : __ɢᴇᴛ ᴛʜᴇ sᴏɴɢ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ__
• `/deezer` - song name : __ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢs ʏᴏᴜ ᴡᴀɴᴛs ғʀᴏᴍ ᴅᴇᴇᴢᴇʀ__
• `/saavn` - song name : __ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ ʏᴏᴜ ᴡᴀɴᴛ ғʀᴏᴍ sᴀᴀᴠɴ__
• `/search` - YouTube Title : __(ɢᴇᴛ ʏᴏᴜᴛᴜʙᴇ sᴇᴀʀᴄʜ ǫᴜᴇʀʏ)__

**𓆩ʀ𓆪 ♥︎ɢʀᴏᴜᴘ ᴀᴅᴍɪɴs ᴄᴏᴍᴍᴀɴᴅ♥︎.**

• `/Sᴋɪᴘ : Sᴋɪᴘs ᴍᴜsɪᴄ
• `/ᴘᴀᴜSᴇ : ᴘᴀᴜSᴇ ᴘʟᴀʏɪɴɢ ᴍᴜSɪᴄ
• `/ʀᴇSᴜᴍᴇ : ʀᴇSᴜᴍᴇ ᴘʟᴀʏɪɴɢ ᴍᴜSɪᴄ
• `/ᴇɴᴅ : SᴛᴏᴘS ᴘʟᴀʏɪɴɢ ᴍᴜSɪᴄ
• `/ʀᴇʟᴏᴀᴅ : ʀᴇʟᴏᴀᴅS ᴀᴅᴍɪɴs ʟɪsᴛS
• `/ᴜSᴇʀʙᴏᴛᴊᴏɪɴ : ᴀSSɪSᴛᴀɴᴛ ᴊᴏɪɴS ᴛʜᴇ ɢʀᴏᴜᴘ
• `/ᴜSᴇʀʙᴏᴛʟᴇᴀᴠᴇ : ᴀSSɪsᴛᴀɴᴛ ʟᴇᴀᴠᴇS ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ.__""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="𓆩∆I$H𓆪", url="https://t.me/aish_jaan_0")
              ]]
          )
      )
