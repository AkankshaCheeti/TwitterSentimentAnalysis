from data_pre_processing import data_preprocessing
from twitter_tweet_Extraction import getTweets
from sentiment_analysis import sentiment_analysis
import pandas as pd
import yfinance as yf
import pandas as pd
from yahoo_fin import stock_info as si
def getSentiment(stock,company):
    #data = getTweets(stock,company)
    #data = pd.read_csv(r"./data/AMZN_randompeopledata/AMZN_random.csv", encoding = 'utf8')
    #data = pd.read_csv(r"./data/AMZN_successfulpeopledata/AMZN_successful.csv", encoding = 'utf8')
    data = pd.read_csv(r"./data/MSFT_randompeopledata/MSFT_random.csv", encoding = 'utf8')
    #data = pd.read_csv(r"./data/MSFT_successfulpeopledata/MSFT_successful.csv", encoding = 'utf8')
    cleaned_data = data_preprocessing(data, stock)
    cleaned_data['date'] = pd.to_datetime(cleaned_data['created_at']).dt.normalize()
    sentimented_data = sentiment_analysis(cleaned_data,stock)
    result_data = getrealstock(sentimented_data,stock)
    textblob_corr,vader_corr=calculate_correlation(result_data)
    return result_data,textblob_corr,vader_corr

def calculate_correlation(data):
    textblob_corr = data['text_blob'].corr(data['Adj Close'])
    vader_corr = data['vader_sentiment'].corr(data['Adj Close'])
    print(f"Correlation between TextBlob sentiment scores and stock prices: {textblob_corr}")
    print(f"Correlation between VADER sentiment scores and stock prices: {vader_corr}")
    return textblob_corr,vader_corr

def getrealstock(data,stock):
    start = min(data['date']).strftime('%Y-%m-%d')

    end = max(data['date']-  pd.to_timedelta(1, unit='d')).strftime('%Y-%m-%d')
    stock_data = yf.download(stock,start,end)
    stock_data.to_csv("./data/" + "realstockraw_" + stock + ".csv")
    stock_data['date'] = stock_data.index
    stock_data['date'] = pd.to_datetime(stock_data['date'],utc=True).dt.normalize()
    stock_data['Adj Close'] = stock_data['Adj Close'].astype(int)
    stock_data['Adj Close'] = stock_data['Adj Close'].apply(lambda x: (x - min(stock_data['Adj Close'])) / (max(stock_data['Adj Close']) - min(stock_data['Adj Close'])) * 0.5)
    result_data = pd.merge(data,stock_data,on='date')
    result_data = result_data[['date','text_blob','vader_sentiment','Adj Close']].copy()
    result_data.to_csv("./data/" + "randomrealstock_" + stock + ".csv")
    #result_data.to_csv("./data/" + "succesfulrealstock_" + stock + ".csv")
    return result_data