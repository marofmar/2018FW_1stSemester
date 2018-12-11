def Chaikin(df):
    ad = (2 * df['close'] - df['high'] - df['low']) / (df['high'] - df['low']) * df['volume']
    Chaikin = pd.Series(pd.ewma(ad, span = 3, min_periods = 2) - pd.ewma(ad, span = 10, min_periods = 9), name = 'Chaikin')
    df = df.join(Chaikin) 
    plt.figure(figsize = (15,10))
    plt.plot(df['Chaikin'],'-m')
    plt.axhline(0, color='cyan')
    return df
    
def maOsc(df, n_short, n_long, fillna=False):
    emafast = ema(df.close, n_short, fillna)
    emaslow = ema(df.close, n_long, fillna)
    macd = emafast - emaslow
    if fillna:
        maOsc = macd.replace([np.inf, -np.inf], np.nan).fillna(0)
    result = pd.Series(macd, name='MA_Short%d_Long%d' % (n_short, n_long))
    df = df.join(result)
    plt.figure(figsize=(15,10))
    plt.plot(result,'-m')
    plt.axhline(0, color='cyan')
    return df
    
def dpo(df, n, fillna=False):
    """Detrended Price Oscillator (DPO)
    Is an indicator designed to remove trend from price and make it easier to
    identify cycles.
    http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:detrended_price_osci
    Args:
        close(pandas.Series): dataset 'Close' column.
        n(int): n period.
        fillna(bool): if True, fill nan values.
    Returns:
        pandas.Series: New feature generated.
    """
    dpo = df['close'].shift(int((0.5 * n) + 1)) - close.rolling(n).mean()
    if fillna:
        dpo = dpo.replace([np.inf, -np.inf], np.nan).fillna(0)
    result = pd.Series(dpo, name='dpo_'+str(n))
    df = df.join(result)
    #visualize
    plt.figure(figsize = (15,10))
    plt.plot(result,'-g')
    plt.axhline(0, color='cyan')
    return df
