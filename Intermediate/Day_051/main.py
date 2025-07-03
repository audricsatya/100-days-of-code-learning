import os
import time
from  twitter_bot import InternetSpeed
from dotenv import load_dotenv

load_dotenv("Intermediate/Day_051/.env")

PROMISED_UPLOAD = 1000
PROMISED_DOWNLOAD = 1000
TWITTER_USERNAME = os.environ.get("USERNAME")
TWITTER_PASSWORD = os.environ.get("PASSWORD")

bot = InternetSpeed()
bot.get_internet_speed()
time.sleep(10)

if PROMISED_UPLOAD > bot.upload or PROMISED_DOWNLOAD > bot.download:
    message = f"Hey, why is my internet speed download {bot.download} Mbps and upload {bot.upload} Mbps when I pay for download {PROMISED_DOWNLOAD} Mbps and upload {PROMISED_UPLOAD} Mbps?"
    bot.tweet(password=TWITTER_PASSWORD, user=TWITTER_USERNAME, message=message)

bot.quit()