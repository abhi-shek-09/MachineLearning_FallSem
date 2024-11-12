import pandas as pd

df = pd.read_csv('FindS.csv')

def find_s_algorithm(df):
    # set all initial hypotheses to 0
    hypothesis = ['0'] * (6)
    
    for i in range(len(df)):
        # consider only the positive instance
        if df.iloc[i, -1] == 'Yes':  
            # compare the hypotheses with the actual values, if its equal then its satisfied so nothing to do
            # if its not equal then we need to change the hypothesis to the more general constraint
            for j in range(len(hypothesis)):
                actual_term = df.iloc[i, j]
                if hypothesis[j] == '0':  
                    hypothesis[j] = actual_term
                elif hypothesis[j] != actual_term:  
                    hypothesis[j] = '?'
    return hypothesis[:-1]

print(find_s_algorithm(df))

    

