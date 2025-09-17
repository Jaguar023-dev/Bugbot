config = {
    "name": "VAMPIRE-RISE-MD",
    "description": "Best WhatsApp bot developed by Kenyan Jaguar",
    "keywords": ["bot", "node", "baileys", "whatsapp"],
    "logo": "https://files.catbox.moe/9lcczo.jpg",
    "repository": "https://github.com/Jaguar023-dev/Bugbot",
    "success_url": "/",
    "stack": "heroku-24",
    "env": {
        "PREFIX": {
            "description": "Choose your prefix for your bot",
            "value": ".",
            "required": True
        },
        "AUTO_REJECT_CALL": {
            "description": "Enter yes for your bot to auto reject calls",
            "value": "no",
            "required": False
        },
        "AUTO_BIO": {
            "description": "Enter yes for your bot to auto update bio",
            "value": "no",
            "required": False
        },
        "AUTO_REPLY_STATUS": {
            "description": "Enter yes for your bot to notify people that you have viewed there status",
            "value": "no",
            "required": False
        },
        "REPLY_STATUS_TEXT": {
            "description": "Enter here your message for your bot to notify people that you have viewed there status",
            "value": "ʏᴏᴜʀ sᴛᴀᴛᴜs ʜᴀᴠᴇ ʙᴇᴇɴ ᴠɪᴇᴡᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅",
            "required": False
        },
        "AUTO_READ_STATUS": {
            "description": "Your status will be read automatically (type yes to activate or no to deactivate)",
            "value": "yes",
            "required": False
        },
        "AUTO_DOWNLOAD_STATUS": {
            "description": "Status will be sent to your inbox automatically (type yes to activate or no to deactivate)",
            "value": "no",
            "required": False
        },
        "AUTO_READ": {
            "description": "Messages will be marked as read automatically (type yes to activate or no to deactivate)",
            "value": "no",
            "required": False
        },
        "BOT_NAME": {
            "description": "Name for your bot",
            "value": "BWM-XMD",
            "required": False
        },
        "BOT_URL": {
            "description": "Image or video url for your bot menu",
            "value": "https://files.catbox.moe/9lcczo.jpg",
            "required": False
        },
        "PUBLIC_MODE": {
            "description": "Type yes for public mode or no for private mode",
            "value": "yes",
            "required": False
        },
        "HEROKU_API_KEY": {
            "description": "Enter your Heroku API key to be able to control your vars",
            "value": "",
            "required": False
        },
        "HEROKU_APP_NAME": {
            "description": "Enter your Heroku app name to be able to control vars",
            "value": "",
            "required": False
        },
        "OWNER_NUMBER": {
            "description": "Enter your number eg, 2547xxxxxxx",
            "value": "",
            "required": False
        },
        "STATUS_REACT_EMOJIS": {
            "description": "Enter your auto like status emojis",
            "value": "💚,🚀,🌎,✅",
            "required": False
        },
        "AUTO_REACT": {
            "description": "Enter your auto react messages",
            "value": "no",
            "required": False
        },
        "AUTO_REACT_STATUS": {
            "description": "Enter yes for your bot to auto like status",
            "value": "yes",
            "required": False
        },
        "OWNER_NAME": {
            "description": "Owner name",
            "value": "Ibrahim Adams",
            "required": False
        },
        "SESSION_ID": {
            "description": "Your session ID",
            "value": "",
            "required": True
        },
        "STARTING_BOT_MESSAGE": {
            "description": "Enable starting message (yes/no)",
            "value": "yes",
            "required": True
        },
        "PRESENCE": {
            "description": "Presence mode: 1=online, 2=typing, 3=recording",
            "value": "",
            "required": False
        },
        "ANTIDELETE_SENT_INBOX": {
            "description": "Enable anti-delete to be sent inbox (yes/no)",
            "value": "yes",
            "required": False
        },
        "ANTIDELETE_RECOVER_CONVENTION": {
            "description": "Enable anti-delete deleted to recover in conversation (yes/no)",
            "value": "no",
            "required": False
        },
        "GROUPANTILINK": {
            "description": "Enable anti-link in groups (yes/no)",
            "value": "no",
            "required": False
        },
        "CHATBOT": {
            "description": "Enable text chatbot (yes/no)",
            "value": "no",
            "required": False
        },
        "WELCOME_MESSAGE": {
            "description": "Enable welcoming message in groups (yes/no)",
            "value": "no",
            "required": False
        },
        "GOODBYE_MESSAGE": {
            "description": "Enable  goodbye in groups (yes/no)",
            "value": "no",
            "required": False
        },
        "AUDIO_CHATBOT": {
            "description": "Enable audio chatbot (yes/no)",
            "value": "no",
            "required": False
        },
        "MENU_TOP_LEFT": {
            "description": "Menu top left design",
            "value": "┌─❖",
            "required": False
        },
        "MENU_BOT_NAME_LINE": {
            "description": "Bot name line",
            "value": "│ ",
            "required": False
        },
        "MENU_BOTTOM_LEFT": {
            "description": "Menu bottom left",
            "value": "└┬❖",
            "required": False
        },
        "MENU_GREETING_LINE": {
            "description": "Greeting line",
            "value": "┌┤ ",
            "required": False
        },
        "MENU_DIVIDER": {
            "description": "Menu divider",
            "value": "│└────────┈⳹",
            "required": False
        },
        "MENU_USER_LINE": {
            "description": "User line in menu",
            "value": "│🕵️ ",
            "required": False
        },
        "MENU_DATE_LINE": {
            "description": "Date line in menu",
            "value": "│📅 ",
            "required": False
        },
        "MENU_TIME_LINE": {
            "description": "Time line in menu",
            "value": "│⏰ ",
            "required": False
        },
        "MENU_STATS_LINE": {
            "description": "Stats line in menu",
            "value": "│⭐ ",
            "required": False
        },
        "MENU_BOTTOM_DIVIDER": {
            "description": "Bottom divider of menu",
            "value": "└─────────────┈⳹",
            "required": False
        }
    },
    "formation": {
        "web": {
            "quantity": 1,
            "size": "basic"
        }
    },
    "buildpacks": [
        {"url": "heroku/nodejs"}
    ]
}