import numpy as np 
import pandas as pd

data = pd.read_csv('./CandidateElimination.csv')
# separate into concepts and target, i.e. features and target
concepts = np.array(data.iloc[:,0:-1])
target = np.array(data.iloc[:,-1])

def learn(concepts, target): 

    # initialize the specific hypothesis to the first positive instance
    specific_h = concepts[0].copy()
    print("\nSpecific Boundary: ", specific_h)

    # initialize the general hypothesis to the most general instance
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print("\nGeneric Boundary: ",general_h)  

    for i, h in enumerate(concepts):
        print("\nInstance", i+1 , "is ", h)
        if target[i] == "Positive":
            for x in range(len(specific_h)):
                # generalise specific_h to allow positive instance 
                if h[x]!= specific_h[x]:                    
                    specific_h[x] ='?'                     
                    general_h[x][x] ='?'
                   
        if target[i] == "Negative":            
            for x in range(len(specific_h)): 
                # specialise general_h to allow negative instance
                if h[x]!= specific_h[x]:                    
                    general_h[x][x] = specific_h[x]                
                else:                    
                    general_h[x][x] = '?'        
        # print out the boundaries
        print("Specific Boundary after ", specific_h)         
        print("Generic Boundary after ", general_h)
        print("\n")

    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?']]    
    for i in indices:   
        general_h.remove(['?', '?', '?', '?', '?']) 
    return specific_h, general_h 

s_final, g_final = learn(concepts, target)

print("Final Specific_h: ", s_final, sep="\n")
print("Final General_h: ", g_final, sep="\n")