#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29907731"))
API_HASH = environ.get("API_HASH", "8f59d632cb374705cfdee46ac17cc3cd")
BOT_TOKEN = environ.get("BOT_TOKEN", "7059623465:AAGPgJeFZtlByqhorWmpoUSnrOS1VW1rJCQ")
OWNER = int(environ.get("OWNER", "6697397532"))
CREDIT = environ.get("CREDIT", "MJ TEAM❤️")
AUTH_USER = os.environ.get('AUTH_USERS', '6631452970').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
