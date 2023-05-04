from textblob_sentiment import textblob_senti
from vader_sentiment import vader_sentiment

def sentiment_analysis(dataframe,stock):
    df1 = textblob_senti(dataframe)
    df2 = vader_sentiment(dataframe)
    result_dataframe = df1
    result_dataframe['vader_sentiment'] = df2['vader_sentiment']
    result_dataframe.to_csv("./output/" + "sentiment_" + stock + ".csv")
    return result_dataframe
