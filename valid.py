import pandas as pd
def valid_number(*args):
    for i in args: 
        try:
            float(i) #strings can't be converted to float, so filter them out
            not_a_number = False #if all the i are numbers, then this "not a number" remains False
                                #if any i is string then it goes to except
        except:                     
            not_a_number = True #this runs only once..if any string found then breaks
            break
    data_okay = not(pd.isna(i) or pd.isnull(i) or not_a_number)
    return data_okay

