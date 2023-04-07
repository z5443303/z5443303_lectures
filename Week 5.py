import pandas as pd
import numpy as np

# Write this function
def mk_df(date_info, aud_usd_info, eur_aud_info):
    """ Combines the information from different sources to produce a dataframe
    with dates row labels. Row labels must be sorted

    Parameters
    ----------
    date_info : list
        date_info = [(row_id, date)]

    aud_usd_info : list
        aud_usd_info = [(row_id, aud/usd)]


    eur_aud_info : list
        eur_aud_info = [(row_id, eur/aud)]

    Returns
    -------
    df
    """
    index = [key for key, value in date_info]
    data = [value for key, value in date_info]
    date_series = pd.Series(data=data, index=index)

    index = [key for key, value in aud_usd_info]
    data = [value for key, value in aud_usd_info]
    aud_usd_series = pd.Series(data=data, index=index)

    index = [key for key, value in eur_aud_info]
    data = [value for key, value in eur_aud_info]
    eur_aud_series = pd.Series(data=data, index=index)

    df = pd.DataFrame({'Dates': date_series, 'AUD/USD': aud_usd_series, 'EUR/AUD': eur_aud_series})

    df.index = df['Dates']
    df = df[['AUD/USD','EUR/AUD']]
    df.sort_index(inplace=True)

    return df


# Sample data for you to develop your function
# date_info = [(row_id, date)]
date_info = [
    (11 , '2020-09-08'),
    (70 , '2020-09-09'),
    (99 , '2020-09-10'),
    (4  , '2020-09-11'),
    (7  , '2020-09-14'),
    (100, '2020-09-15'),
    ]

# aud_usd_info = [(row_id, aud/usd)]
aud_usd_info = [
    (70 ,  0.7209),
    (4  ,  0.7263),
    (11 ,  0.7280),
    (7  ,  0.7281),
    (100,  0.7285),
]


# eur_aud_info = [(row_id, eur/aud)]
eur_aud_info = [
    (70 ,  1.6321),
    (4  ,  1.6282),
    (99 ,  1.6221),
    (100,  1.6288),
    (11 ,  1.6232),
    ]

df = mk_df(date_info, aud_usd_info, eur_aud_info)
print(df)
import pandas as pd
import numpy as np
from unanswered import *

aud_usd_lst = [
    ('2020-09-08', 0.7280),
    ('2020-09-09', 0.7209),
    ('2020-09-11', 0.7263),
    ('2020-09-14', 0.7281),
    ('2020-09-15', 0.7285),
    ]

eur_aud_lst = [
    ('2020-09-08',  1.6232),
    ('2020-09-09',  1.6321),
    ('2020-09-10',  1.6221),
    ('2020-09-11',  1.6282),
    ('2020-09-15',  1.6288),
    ]

# Replace unanswered with your solution.
aud_usd_series = unanswered
eur_aud_series = unanswered
df = unanswered
index = [key for key, value in aud_usd_lst]
data = [value for key, value in aud_usd_lst]
aud_usd_series = pd.Series(data=data, index=index)
#print(aud_usd_series)

index = [key for key, value in eur_aud_lst]
data = [value for key, value in eur_aud_lst]
eur_aud_series = pd.Series(data=data, index=index)
#print(eur_aud_series)

df = pd.DataFrame({'AUD/USD': aud_usd_series, 'EUR/AUD': eur_aud_series})
#print(df)