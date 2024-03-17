STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_KEY = "EWUPU4W69UXX39SR"
NEWS_KEY = "8c270cd58a2f46d188f201e5bf2b0bdb"
import requests
from twilio.rest import Client
from datetime import date,timedelta
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
par = {
"function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "outputsize":"compact",
    "apikey":"EWUPU4W69UXX39SR"
}
par2 = {
    "q":COMPANY_NAME,
    "apikey":NEWS_KEY
}

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
resp = requests.get(url=STOCK_ENDPOINT,params=par)
data = resp.json()
today = float(data['Time Series (Daily)'][f'{date.today()- timedelta(days = 1)}']['4. close'])
yesterday = float(data['Time Series (Daily)'][f'{date.today()- timedelta(days = 2)}']['4. close'])
if today>yesterday:
    img = "🔺"
else:
    img = "🔻"
diff = abs(today-yesterday)
diff_per =diff/yesterday*100
news = False
resp2 = requests.get(url=NEWS_ENDPOINT,params=par2)
data2 = resp2.json()
if diff_per>10:
    news=True
news_data = (data2['articles'])
msg = \
f"""{STOCK}{img}{diff_per}
Headline 1:{news_data[0]['title']}
Brief:{news_data[0]['description']}
Headline 2:{news_data[1]['title']}
Brief:{news_data[1]['description']}
Headline 2:{news_data[2]['title']}
Brief:{news_data[2]['description']}

"""
print(msg)


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.
account_sid = "AC0b6f60e8f363062c0d04474b15415c1c"
auth_token =  "3ecd0da03c8b22eee1e668104b52655c"
cli = Client(account_sid,auth_token)
message = cli.messages.create(
    from_="+15052735708",
    body=msg,
    to="+918143119859"
)
print(message.status)



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

