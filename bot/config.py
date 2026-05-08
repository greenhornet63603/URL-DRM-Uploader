import os
from dotenv import load_dotenv

if os.path.exists("config.env"):
    load_dotenv("config.env")
else:
    load_dotenv()


def is_enabled(value, default):
    value = str(value).lower()

    if value in ["true", "yes", "1", "enable", "y"]:
        return True

    elif value in ["false", "no", "0", "disable", "n"]:
        return False

    return default


class Config(object):

    # Telegram API
    API_ID = int(os.environ.get("API_ID", "27400172"))

    API_HASH = os.environ.get(
        "API_HASH",
        "56d0a75c5f9a9de6beb5452aa63c2d36"
    )

    BOT_TOKEN = os.environ.get(
        "BOT_TOKEN",
        "8724093305:AAEQymahtqxrtWLk1gpHibRmU_1rdIrdkfo
    )

    # MongoDB Disabled
    DATABASE_NAME = ""

    DATABASE_URL = ""

    # Owner
    OWNER_ID = int(
        os.environ.get("OWNER_ID", "7540570087")
    )

    # Log Channel
    LOG_CHANNEL = int(
        os.environ.get("LOG_CHANNEL", "-1003910418287")
    )

    # Web Server
    WEB_SERVER = is_enabled(
        os.environ.get("WEB_SERVER", "False"),
        False
    )

    # Thumbnails
    THUMBNAILS = list(
        map(str, os.environ.get("THUMBNAILS", "").split())
    )

    # Runtime Data
    CANCEL_DATA = {}
    PROCESS_DATA = {}


class Script(object):

    START_MESSAGE = (
        "Hello {mention}\n\n"
        "Send any link or txt file to start downloading."
    )

    DEV_MESSAGE = """
👋 Hey there, I'm Caption Alex ❤️

I create Telegram bots and automation tools.
"""

    HELP_MESSAGE = os.environ.get(
        "HELP_MESSAGE",
        "Help message"
    )

    PROGRESS_MESSAGE = """
**╔════❰ Uploading ❱══❍
║╭━➣
║┣⪼ Progress :- {percentage}%
║┣⪼ {progress}
║┣⪼ {finished} of {total}
║┣⪼ Speed :- {speed}/s
║┣⪼ ETA :- {eta}
║╰━➣
╚════════════════❍**
"""

    NEW_USER_MESSAGE = """
#NewUser

🆔 User ID: `{user_id}`
👤 User: {mention}
"""

    DOWNLOADING = """
📥 DOWNLOADING :- {start_index}/{end_index}

📝 Name » {link_no}) » {name}

Original Index:
{orginal_start_index}/{orginal_end_index}
"""

    DEFAULT_CAPTION = """
[📁] File_ID : {file_index}

𖤓 Title : {file_name}

🗃 Size : {file_size}

📚 Batch : {batch_name}
"""

    CAPTION_CB = """
**Set Caption**

➢ Available Variables 👇

🎴 Name : `{file_name}`
🗃 Size : `{file_size}`
⚙️ Extension : `{file_extension}`
🧭 Duration : `{file_duration}`
🖇 Link : `{file_url}`
🔢 Index : `{file_index}`
🗳 Batch : `{batch_name}`

==============================

➢ Current:
`{current_caption}`

==============================

➢ Default:
`{default_caption}`

➢ Status: {status}
"""
