from datetime import datetime, timedelta
from dateutil import parser

from telethon import TelegramClient
from stepik_client import Stepik

import os

# Use your own values from my.telegram.org
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')
channel_id = os.getenv('CHANNEL_ID')

# Enter parameters below:
# 1. Get your keys at https://stepik.org/oauth2/applications/
# (client type = confidential, authorization grant type = client credentials)
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
COURSE_ID = os.getenv('COURSE_ID')
api_host = "https://stepik.org"

DAYS_IN_THE_PAST = 1

# We have to manually call "start" if we want an explicit bot token
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
stepik_client = Stepik(client_id=client_id, client_secret=client_secret)

# The first parameter is the .session file name (absolute paths allowed)
with bot:
    course_reviews_obj = stepik_client.fetch_object_with_params('course-review', f'course={COURSE_ID}')
    for review in course_reviews_obj:
        create_date = parser.parse(review['create_date'], ignoretz=True)
        review_age = datetime.now() - create_date
        if review_age < timedelta(days=DAYS_IN_THE_PAST, minutes=5):
            user = stepik_client.fetch_object('user', review['user'])
            user_fullname = user["full_name"]
            user_profile = f'{api_host}/users/{user["id"]}'

            text = review["text"]
            review_link = f"{api_host}/course/{COURSE_ID}/reviews/{review['id']}"
            score = f"Рейтинг: {int(review['score']) * '★'}"
            create_date = f"{review['create_date']}"

            result = f"""
{create_date}

{user_fullname} {user_profile}

{text}

{score}

{review_link}
"""
            bot.loop.run_until_complete(bot.send_message(int(channel_id), result))
