# Day 36: Automate Stock Checker API, News, and Daily Reminder

## Goals
- Build an automated system to check stock prices using an API.
- Fetch related news articles for significant stock movements.
- Send a daily reminder with stock updates and news.

## Tasks

### 1. Stock Checker API
- Use an API (e.g., Alpha Vantage, Finnhub) to fetch daily stock prices.
- Monitor for significant price changes (e.g., >5%).

### 2. News Fetcher
- When a significant change is detected, fetch relevant news using a news API (e.g., NewsAPI).
- Summarize top 3 news articles.

### 3. Daily Reminder
- Compile stock data and news into a summary.
- Send the summary via email or messaging service (e.g., SMTP, Twilio).

## Example Workflow

1. **Fetch Stock Data**
    - Request latest stock prices.
    - Compare with previous close.

2. **Check for Significant Change**
    - If change > threshold, proceed to fetch news.

3. **Fetch News**
    - Query news API with stock/company name.
    - Extract headlines and links.

4. **Send Reminder**
    - Format summary.
    - Send via preferred channel.

## Resources

- [Alpha Vantage API](https://www.alphavantage.co/documentation/)
- [NewsAPI](https://newsapi.org/docs)
- [Python `smtplib` for Email](https://docs.python.org/3/library/smtplib.html)
- [Twilio SMS API](https://www.twilio.com/docs/sms/send-messages)

---

**Tip:** Use environment variables to store API keys securely.
