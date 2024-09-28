import numpy as np
import pandas as pd
from valid import *
from initialize import *

#initialize returns which diseases the user is suffering from
disease_list, food_choices  = initialize()

if not disease_list:
    quit()

print("Finding the best food for you...")

file_name_data = r"data.xlsx"
#creating DataFrame from data.xlsx file
df_foods = pd.read_excel(file_name_data, usecols = range(20), index_col = 0)

df_foods = df_foods[df_foods['Food Group'].isin(food_choices)]

#prescriptions file contains the prescriptions for all disease
file_name_prescriptions = "prescriptions.xlsx"
df_prescriptions = pd.read_excel(file_name_prescriptions ,usecols= range(20),index_col = 0)
df_prescriptions = df_prescriptions

food_list = df_foods.index

nutrient_list = df_foods.columns[1:]

required_nutrients_list = df_prescriptions.columns

def filtering(disease_list):
    if disease_list:
        
        for i,disease in enumerate(disease_list):
            this_disease_score = []
            
            #for every food of FOOD LIST
            for food in food_list:
    
                final_score = 0

                #runs for each nutrients specified in the prescriptions list
                for nutrient in required_nutrients_list:
                    
                    if nutrient in nutrient_list:
                        

                        #accessing the values of the nutrient
                        a = df_foods.loc[food, nutrient] 
                        
                        b = df_prescriptions.loc[disease, nutrient]
                        

                        #checking if the numbers are valid (no multiplication if null or nan)
                        if valid_number(a,b):
                            product= a*b
                            
                            final_score+= product
                            
                #adding the score of every food in current disease(of the loop)
                this_disease_score.append(final_score)

            #adding the scores of each disease to dataframe
            df_foods[f"Score for {disease_list[i]}"] = this_disease_score

        #making a list of the scores of all the diseases
        sum_list = [f"Score for {disease}" for disease in disease_list]

        df_foods["Combined Score"] = df_foods[sum_list].sum(axis = 1)

        print(f"\nthe best foods for you to eat are\n")
        best_foods = df_foods.sort_values(by = "Combined Score", ascending=False)
        return best_foods


# print(df_foods)
# print(df_prescriptions)
show = filtering(disease_list)
print(show.iloc[:, -len(disease_list)-1:].head(30))


