import numpy as np
import pandas as pd

# colname: Year, Month, Day
def digame_index(df, year, month, day):
    result = df[(df.Year == year)&(df.Month == month)&(df.Day == day)].head(1)
    tail = df[(df.Year == year)&(df.Month == month)&(df.Day == day)].tail(1)
    print("from %s to %s" %(int(result.index.values),int(tail.index.values)))
    return result, tail
