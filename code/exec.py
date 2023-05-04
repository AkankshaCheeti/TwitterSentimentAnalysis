from getSentiment import getSentiment
import matplotlib.pyplot as plt

def plotting(dataframe,analysis,stock):
    dataframe.plot(x='date', y=analysis, kind = 'line',title=stock).get_figure().savefig(stock)
    plt.grid(which="major",alpha=0.6)
    plt.grid(which="minor",alpha=0.3)
    plt.show()
def plotting3(dataframe,stock):
    analysis = ["text_blob", "vader_sentiment", "Real_time Stock"]
    dataframe.plot(x='date', y=analysis, kind = 'line',title=stock).get_figure().savefig(stock)
    plt.grid(which="major",alpha=0.6)
    plt.grid(which="minor",alpha=0.3)
    plt.show()
def plotting2(result_data):
    # sample data
    dates=result_data["date"]
    textblob_sentiment = result_data["text_blob"]
    vader_sentiment = result_data["vader_sentiment"]
    stock_prices =result_data["Real_time Stock"]
    # create scatter plot for TextBlob sentiment scores and stock prices
    plt.scatter(dates, textblob_sentiment, color='blue', marker='o', label='TextBlob')
    plt.scatter(dates, stock_prices, color='red', marker='^', label='Real Stock')
    plt.title('Sentiment Scores and Stock Prices')
    plt.xlabel('Date')
    plt.ylabel('Score/Price')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    print("Choose from the following sample list of stock tickers or enter your stock ticker\n Tickers for:\n")
    sample_stocks = ['Nvidia is NVDA', 'Microsoft is MSFT', 'Apple.Inc is AAPL', 'Roblox.Inc is RBLX']
    for i in range(len(sample_stocks)):
        print((i+1),".", sample_stocks[i])
    stock = input("Enter stock ticker: \n")
    company=input("Enter company name: \n")
    print(" stock selected is", stock)
    print(" company name is", company)
    result_data,textblob_corr,vader_corr = getSentiment(stock,company)
    result_data.rename(columns = {'Adj Close':'Real_time Stock'}, inplace = True)
    analysis1 = ["text_blob", "Real_time Stock"]
    analysis2=["vader_sentiment", "Real_time Stock"]
    #plotting(result_data,analysis1,stock)
    #plotting(result_data,analysis2,stock)
    plotting3(result_data,stock)
    #plotting2(result_data)
    # plotting(result_data,stock)
    print("Exited")
    

