#Moving Average  
def MA(df, n):  
    MA = pd.Series(pd.rolling_mean(df.close, n), name = 'MA_' + str(n))  
    df = df.join(MA)  
    return df
