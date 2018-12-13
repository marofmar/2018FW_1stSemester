a = data.groupby('col_name')

def extract(groups, key):
    return groups.get_group((key))
    
for i in range(24): # data split by hour
    res = extract(a,i)
    res.to_csv(str(i) + '.csv')
