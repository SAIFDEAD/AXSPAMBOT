from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("🌺 ᴄᴏᴍᴍᴀɴᴅs 🌺", data="help_back"),
        Button.url("💘 𝙾𝚆𝙽𝙴𝚁 💘", "https://t.me/Saif_Dictator")
    ],
    [
        Button.url("🌼 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 🌼", "https://t.me/Dead_SupportChat"),
        Button.url("🏵 𝚂𝚄𝙿𝙿𝙾𝚃 🏵 •", "https://t.me/SAIFHELPGC")
    ],
    [
        Button.url("🌿 𝚁𝙴𝙿𝙾 🌿", "https://graph.org/file/1cec00803e0497f6794f3.mp4"),
        Button.url("💘 𝙼𝚈 𝙿𝙰𝙿𝙰 💘", "https://t.me/Saif_Dictator")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [🇩𝜩Ⓐ︎🇩](https://t.me/Saif_Dictator)**\n\n"
        TEXT += f"» **ᴅᴇᴀᴅ ᴠᴇʀsɪᴏɴ :** `M3.3`\n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://graph.org/file/4d811a985dedfe0cb135c.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
)
