from operator import index
import pandas as pd
import numpy 

TOTAL_TEACHERS = 28
MATH_TEACHERS = 10
df = pd.read_csv("survey_responses.csv")


# Probability of teachers having high confidence in their
# tech capabilities given they teach English
high_confidence = 0
total = 0
for col in range(3, 17):
    for row in range(7, 17):
        current = df.iloc[row][col]
        total += 1
        if current > 3:
            high_confidence += 1

p_high_given_math = high_confidence / total
print("P(High Technology Confidence | Math Teacher): ", p_high_given_math)

# Probability of teachers viewing technology having positive 
# impact on students given they teach English
positive = 0
total2 = 0
for col in range(24, 33):
    for row in range(7, 17):
        current = df.iloc[row][col]
        total2 += 1
        if current > 3:
            positive += 1

p_positive_given_math = positive / total2
print("P(Positive Student Impact Perception | Math Teacher: ", p_positive_given_math)

# Probability of teachers being optimisitc about increased
# reliance on edtech (esp after COVID)

optimism = 0
col = 50
for row in range(7, 17):
    current = df.iloc[row][col]
    if current > 3:
        optimism += 1
p_optimism_given_math = optimism / MATH_TEACHERS
print("P(Optimistic About EdTech Reliance | Math Teacher: ", p_optimism_given_math)