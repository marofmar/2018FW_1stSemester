#Exponential Moving Average  
def EMA(df, n):  
    EMA = pd.Series(pd.ewma(df.close, span = n, min_periods = n - 1), name = 'EMA_' + str(n))  
    df = df.join(EMA)  
    return df
