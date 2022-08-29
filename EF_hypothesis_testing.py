import numpy as np
import pandas as pd
import csv
import math
import scipy.stats as st

# Define the null and alternative hypothesis
# Null Hypothesis: p_0 = 0.38
# Althernative Hypothesis: p_0 < 0.38
# Level of Confidence = 0.05 (5%)

# Read the data file                          
with open('ad_click.csv') as file:
    reader = csv.DictReader(file)

# Extract the CTR column from the data
    visit = []                      
    count = 0
    for column in reader:
        visit.append(int(column["var_1"]))
        if count > 1000000000000:                
            break
        count +=1              

p = sum(visit)/len(visit)
print(f"CTR = {p}")

# Compute the p-value
p_0=0.38
p_value=math.sqrt(len(visit))*(p-p_0)/math.sqrt(p_0 *(1-p_0))
print(p_value)

# Compute the z-score
norm_value = st.norm.cdf(p_value)     
print(norm_value)

# Test the market hypothesis
if norm_value >0.05:
    print("Test Hypothesis is true with \u03B1 = 0.05.")
else:
    print("Test Hypothesis is false.")       

