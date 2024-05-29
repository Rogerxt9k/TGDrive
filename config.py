from dotenv import load_dotenv
import os

# Load environment variables from the .env file, if present
load_dotenv()

# Telegram API credentials obtained from https://my.telegram.org/auth
API_ID = int(os.getenv("API_ID", "20227614"))  # Your Telegram API ID
API_HASH = os.getenv("API_HASH", "b9268f7d01884a3d740ba17d0ad8754b")  # Your Telegram API Hash

# List of Telegram bot tokens used for file upload/download operations
BOT_TOKENS = os.getenv("BOT_TOKENS", "6997462172:AAGlI6eYJafPWUl-EzWR6q7ESPU4cCT7jYA").strip(", ").split(",")
BOT_TOKENS = [token.strip() for token in BOT_TOKENS if token.strip() != ""]  # Clean up any extra spaces

# List of Premium Telegram Account Pyrogram String Sessions used for file upload/download operations
STRING_SESSIONS = os.getenv("STRING_SESSIONS", "BQGPobEAASFDI0sRCdcT0GU20q6SWoJ_kO3yiGuxbW0WKO55LJh7-rSIG1SOC_zeFZOgfHK2oBCapV7SohwTBx5-mXs91T3jvXBVbAoeHyp0mYUFY7wMG_veRxOJHMBpYF3plO01lfzoFXiVQzyG7v19ed2IN939K8vl0WP1Y0VveHEmw2md-lIFJ7bwnyNYQD97HZJvoS7BJIQ-3YruXekmx1O1v6wGUGphK6E0DQN83VVbGuovt8gMj1OPdVnP6GOB3WpdEuWWY9YMpi11W6qnb-FFeTApi7auEAb5viA-NaKl1jdh7bkFr0WczvtEW4lgXVD_G1uglio7EnG2WEC5VK1d_gAAAAF_kG9IAA").strip(", ").split(",")
STRING_SESSIONS = [
    session.strip() for session in STRING_SESSIONS if session.strip() != ""
]  # Clean up any extra spaces

# Chat ID of the Telegram storage channel where files will be stored
STORAGE_CHANNEL = int(os.getenv("STORAGE_CHANNEL" , "-1002042477431"))  # Your storage channel's chat ID

# Message ID of a file in the storage channel used for storing database backups
DATABASE_BACKUP_MSG_ID = int(
    os.getenv("DATABASE_BACKUP_MSG_ID" , "11359")
)  # Message ID for database backup

# Password used to access the website's admin panel
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "razerx")  # Default to "admin" if not set

# Determine the maximum file size (in bytes) allowed for uploading to Telegram
# 1.98 GB if no premium sessions are provided, otherwise 3.98 GB
if len(STRING_SESSIONS) == 0:
    MAX_FILE_SIZE = 1.98 * 1024 * 1024 * 1024  # 2 GB in bytes
else:
    MAX_FILE_SIZE = 3.98 * 1024 * 1024 * 1024  # 4 GB in bytes

# Database backup interval in seconds. Backups will be sent to the storage channel at this interval
DATABASE_BACKUP_TIME = int(
    os.getenv("DATABASE_BACKUP_TIME", 60)
)  # Default to 60 seconds

# Time delay in seconds before retrying after a Telegram API floodwait error
SLEEP_THRESHOLD = int(os.getenv("SLEEP_THRESHOLD", 60))  # Default to 60 seconds

# Choose whether to use .session files for session persistence or in-memory sessions
# Set to False to use in-memory sessions instead of .session files
USE_SESSION_FILE = bool(
    os.getenv("USE_SESSION_FILE", True)
)  # Default to True (use .session files)
