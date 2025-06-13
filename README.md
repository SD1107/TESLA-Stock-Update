# 📈 Tesla Stock News Alert with Email Notification

A Python automation script that monitors Tesla Inc. (TSLA) stock prices using the Alpha Vantage API. If the stock price changes more than a specified threshold (5% by default) compared to the previous day, the script fetches the latest news about Tesla from the NewsAPI and sends a summary of the top 3 headlines to a specified email address.

---

## 🔧 Features

- 📊 **Stock Data**: Real-time closing price analysis using Alpha Vantage API.
- 📰 **News Headlines**: Fetches top 3 Tesla-related news articles using NewsAPI.
- 📧 **Email Alerts**: Sends formatted news summaries via SMTP.
- 🧠 **Logic**: Only sends alerts if the price fluctuation is significant (greater than or equal to 5%).
- ✅ Fully environment-variable based for API keys and sensitive information.

---

## 🛠️ Technologies Used

- Python 3
- [Alpha Vantage API](https://www.alphavantage.co/documentation/)
- [NewsAPI](https://newsapi.org/docs)
- `requests`
- `smtplib`
- `dotenv`
- `os`
- `datetime`

---



