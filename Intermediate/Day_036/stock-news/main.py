import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import smtplib

STOCK = "NVDA" # Stock symbol for NVIDIA
COMPANY_NAME = "NVIDIA" # Company name for news articles
API_KEY = "demo"  # Replace with your Alpha Vantage API key
NEWS_API_KEY = "demo"  # Replace with your NewsAPI key
TWILIO_ACCOUNT_SID = "demo"  # Replace with your
TWILIO_AUTH = "demo"  # Replace with your Twilio Auth Token
FROM_PHONE = "+1234567890"  # Replace with your Twilio phone number
TO_PHONE = "+0987654321"  # Replace with your phone number
FROM_EMAIL = "email@gmail.com"  # Replace with your email
PASSWORD = "your_password"  # Replace with your email password or app password
TO_EMAIL = "email@gmail.com"  # Replace with your email

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stock_data(stock_symbol):
    url = f"https://www.alphavantage.co/query"
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_symbol,
        "apikey": API_KEY
    }

    # Make a request to the Alpha Vantage API
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    
    if response.status_code != 200:
        raise Exception(f"Error fetching data from Alpha Vantage: {response.status_code}")

    data = response.json()

    # Get the last two days of stock data
    time_series = data["Time Series (Daily)"]
    dates = sorted(time_series.keys(), reverse=True)[:2]
    
    if len(dates) < 2:
        raise ValueError("Not enough data to compare two days.")
    
    yesterday_data = time_series[dates[0]]
    day_before_yesterday_data = time_series[dates[1]]
    
    yesterday_close = float(yesterday_data["4. close"])
    day_before_yesterday_close = float(day_before_yesterday_data["4. close"])
    
    percentage_change = ((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) * 100
    print(f"Yesterday's close: {yesterday_close}, Day before yesterday's close: {day_before_yesterday_close}")
    
    if abs(percentage_change) >= 5:
        print("Get News")
        return percentage_change
    else:
        print("No significant change in stock price.")
        return None

# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news(company_name):
    url = "https://newsapi.org/v2/everything"
    parameters = {
        "q": company_name,
        "from": (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d'),
        "sortBy": "relevancy",
        "pageSize": 3,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=parameters)
    response.raise_for_status()
    
    if response.status_code != 200:
        raise Exception(f"Error fetching news data: {response.status_code}")

    news_data = response.json()
    
    articles = []
    for article in news_data["articles"]:
        articles.append({
            "title": article["title"],
            "description": article["description"]
        })
    
    return articles

# Send an email with the percentage change and each article's title and description to your email address.
def send_email(percentage_change, articles, from_email, to_email, password):
    if not articles:
        print("No articles found to send.")
        return
    
    subject = f"{STOCK}: {'🔺' if percentage_change > 0 else '🔻'}{abs(percentage_change):.2f}%"
    body = "\n\n".join([f"Headline: {article['title']}\nBrief: {article['description']}" for article in articles])
    
    message = f"Subject: {subject}\n\n{body}"
    
    # Send the email using smtplib
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=from_email, password=password)  # Replace with your email password
            connection.sendmail(from_addr=from_email, to_addrs=to_email, msg=message)
            print(f"Sent Email: {subject}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_sms(percentage_change, articles, from_phone, to_phone):
    if not articles:
        print("No articles found to send.")
        return
    
    # Initialize Twilio client
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH)
    
    for article in articles:
        message = f"{STOCK}: {'🔺' if percentage_change > 0 else '🔻'}{abs(percentage_change):.2f}%\n" \
                  f"Headline: {article['title']}\n" \
                  f"Brief: {article['description']}"
        
        client.messages.create(
            body=message,
            from_=from_phone,  # Replace with your Twilio phone number
            to=to_phone  # Replace with your phone number
        )
        print(f"Sent SMS: {message}")

# Main function to execute the stock news retrieval and SMS sending
try:
    percentage_change = get_stock_data(STOCK)
    if percentage_change is not None:
        articles = get_news(COMPANY_NAME)
        send_email(percentage_change, articles, FROM_EMAIL, TO_EMAIL, PASSWORD)
        send_sms(percentage_change, articles, FROM_PHONE, TO_PHONE)
except Exception as e:
    print(f"An error occurred: {e}")

# This code is for educational purposes only. Use responsibly and ethically.
