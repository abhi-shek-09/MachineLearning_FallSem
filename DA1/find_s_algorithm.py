import pandas as pd

df = pd.read_csv('FindS.csv')

def find_s_algorithm(df):
    hypothesis = ['0'] * (len(df.columns))
    for i in range(len(df)):
        if df.iloc[i, -1] == 'Yes':  
            for j in range(len(hypothesis)):
                actual_term = df.iloc[i, j]
                if hypothesis[j] == '0':  
                    hypothesis[j] = actual_term
                elif hypothesis[j] != actual_term:  
                    hypothesis[j] = '?'
    return hypothesis[:-1]

print(find_s_algorithm(df))

    

