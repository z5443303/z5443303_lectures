row_sel_q4 = ['2020-09-08', '2020-09-09']
col_sel_q4 = 'AUD/USD'
q4 = df.loc[row_sel_q4, col_sel_q4]

prc.sort_index(inplace=True)

rets = prc.loc[:, 'Close'].pct_change()
print(rets)