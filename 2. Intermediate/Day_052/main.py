from instagram import InstaFollower
from dotenv import load_dotenv
import os

load_dotenv("Intermediate/Day_052/.env")

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TARGET = os.getenv("TARGET")

bot = InstaFollower()

bot.login(username=USERNAME, password=PASSWORD)
bot.find_followers(target_user=TARGET)

bot.follow()

bot.quit()