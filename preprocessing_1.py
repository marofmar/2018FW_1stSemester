def preprocess_df(df):
    scaler = preprocessing.MinMaxScaler()
    df.dropna(inplace = True)
    df['future'] = scaler.fit_transform(np.array(df['future']).reshape(-1,1))
    for col in df.columns:
        if col != 'future':
            df.dropna(inplace = True)
            df[col] = scaler.fit_transform(np.array(df[col]).reshape(-1,1))
    df.dropna(inplace = True)

    sequential_data = []
    prev_hours = deque(maxlen = SEQ_LEN)

    for i in df.values:
        prev_hours.append([n for n in i[:-1]])
        if len(prev_hours) == SEQ_LEN:
            sequential_data.append([np.array(prev_hours), i[-1]])

    random.shuffle(sequential_data)

    X = []
    y = []

    for seq, target in sequential_data:
        X.append(seq)
        y.append(target)

    #print(X[0])

    return np.array(X), y
    
    
    
def test_preprocess_df(df):
    scaler = preprocessing.MinMaxScaler()
    df.dropna(inplace = True)
    df['future'] = scaler.fit_transform(np.array(df['future']).reshape(-1,1))
    for col in df.columns:
        if col != 'future':
            df.dropna(inplace = True)
            df[col] = scaler.fit_transform(np.array(df[col]).reshape(-1,1))
    df.dropna(inplace = True)

    sequential_data = []
    prev_hours = deque(maxlen = SEQ_LEN)

    for i in df.values:
        prev_hours.append([n for n in i[:-1]])
        if len(prev_hours) == SEQ_LEN:
            sequential_data.append([np.array(prev_hours), i[-1]])

    #random.shuffle(sequential_data)

    X = []
    y = []

    for seq, target in sequential_data:
        X.append(seq)
        y.append(target)

    #print(X[0])

    return np.array(X), y
