import requests
import smtplib
import datetime 
import os
from dotenv import load_dotenv


load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
API_KEY=os.getenv("STOCK_API_KEY")


NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY_NEWS=os.getenv("NEWS_API_KEY")


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price


parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "datatype":"json",
    "apikey":API_KEY
}


response=requests.get(STOCK_ENDPOINT,params=parameters)
data=response.json()
# print(data)

yesterday_stock_close=float(data["Time Series (Daily)"][list(data["Time Series (Daily)"])[0]]["4. close"])
daybeforeyesterday_stock_close=float(data["Time Series (Daily)"][list(data["Time Series (Daily)"])[1]]["4. close"])


# print(yesterday_stock_close)
# print(daybeforeyesterday_stock_close)


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp


diff_original=yesterday_stock_close-daybeforeyesterday_stock_close
diff=abs(diff_original)


#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.


percentage=(diff/daybeforeyesterday_stock_close)*100


#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.


time_now=datetime.datetime.now()
formatted_time_today=datetime.date.fromordinal(datetime.date.today().toordinal()).strftime("%F")
formatted_time_yesterday=datetime.date.fromordinal(datetime.date.today().toordinal()-1).strftime("%F")
# print(formatted_time_today)
# print(formatted_time_yesterday)


parameters_news={
    "q":COMPANY_NAME,
    "from":formatted_time_yesterday,
    "to":formatted_time_today,
    "sortBy":"publishedAt",
    "apikey":API_KEY_NEWS
}
dict={}

if percentage>=0.00:
    response=requests.get(url=NEWS_ENDPOINT,params=parameters_news)
    news_data=response.json()
    connection=smtplib.SMTP(os.getenv("PROVIDER"),port=587)
    connection.starttls()
    # for i in range(0,1):
        # print(news_data["articles"][i]["title"])
        # print(news_data["articles"][i]["description"])
        # print("\n")
        # dict[news_data["articles"][i]["title"].encode('ascii', 'ignore').decode('ascii')]=news_data["articles"][i]["description"].encode('ascii', 'ignore').decode('ascii')
        #print(dict)
    title1=news_data["articles"][0]["title"].encode('ascii', 'ignore').decode('ascii')
    des1=news_data["articles"][0]["description"].encode('ascii', 'ignore').decode('ascii')


    title2=news_data["articles"][1]["title"].encode('ascii', 'ignore').decode('ascii')
    des2=news_data["articles"][1]["description"].encode('ascii', 'ignore').decode('ascii')


    title3=news_data["articles"][2]["title"].encode('ascii', 'ignore').decode('ascii')
    des3=news_data["articles"][2]["description"].encode('ascii', 'ignore').decode('ascii')
    # print(dict.keys())
    if diff_original>0:
        connection.login(user=os.getenv("FROM"),password=os.getenv("PASSWORD"))
        connection.sendmail(from_addr=os.getenv("FROM"),
                            to_addrs=os.getenv("TO"),
                            msg=f"Subject:Tesla Stocks Update!\n\n TSLA: ^{float(percentage)}%\n\n\t\tTop Headlines of Today\n\nHeadline:{title1}\nBrief:{des1}\n\nHeadline:{title2}\nBrief:{des2}\n\nHeadline:{title3}\nBrief:{des3}\n\n~Shared by Soumyadeep Dey:)"
                            )
        connection.close()
    else:
        connection.login(user=os.getenv("FROM"),password=os.getenv("PASSWORD"))
        connection.sendmail(from_addr=os.getenv("FROM"),
                            to_addrs=os.getenv("TO"),
                            msg=f"Subject:Tesla Stocks Update!\n\n TSLA: {float(percentage)}%\n\n\t\tTop Headlines of Today\n\nHeadline:{title1}\nBrief:{des1}\n\nHeadline:{title2}\nBrief:{des2}\n\nHeadline:{title3}\nBrief:{des3}\n\n~Shared by Soumyadeep Dey:)"
                            )
        connection.close()
    


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""