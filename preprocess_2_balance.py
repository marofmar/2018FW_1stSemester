def preprocess_df(df):
    df = df.drop('future', 1)
    for col in df.columns:
        if col != 'target':
            df[col] = df[col].pct_change()
            df.dropna(inplace = True)
            df[col] = preprocessing.scale(df[col].values)
    df.dropna(inplace = True)

    sequential_data = []
    prev_hours = deque(maxlen = SEQ_LEN)

    for i in df.values:
        prev_hours.append([n for n in i[:-1]])
        if len(prev_hours) == SEQ_LEN:
            sequential_data.append([np.array(prev_hours), i[-1]])

    random.shuffle(sequential_data)
    #print(sequential_data[0])

    bigger = []
    smaller = []

    for seq, target in sequential_data:
        if target == 0:
            smaller.append([seq, target])
        else:
            bigger.append([seq, target])

    random.shuffle(bigger)
    random.shuffle(smaller)

    lower = min(len(bigger), len(smaller))
    #print(lower)
    bigger = bigger[:lower]
    smaller = smaller[:lower]

    sequential_data = bigger + smaller

    random.shuffle(sequential_data)

    X = []
    y = []

    for seq, target in sequential_data:
        X.append(seq)
        y.append(target)

    return np.array(X), y
