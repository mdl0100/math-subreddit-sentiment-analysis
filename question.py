############################################
##              Marcos Lopez              ##
##      Natural Language Processing       ##
##      Futher Data cleanup for SpaCY     ##
############################################

# Description
# This script will further clean the data and prepare it for analysis in the next script.
# It will remove the 'C1', 'C2', 'C3', 'C4', 'C5' columns and replace them with the counts of positive, negative, and neutral comments.
# It will also remove the 'sentiment' and 'title' columns and save the data to a new file.


import pandas as pd 

with open('statements.csv', encoding='utf-8') as f:
    questions = pd.read_csv(f)  # Read the data from the file

# print(questions.head())


comments = ['C1', 'C2', 'C3', 'C4', 'C5']

def count_values(row):
    counts = {value: row[comments].tolist().count(value) for value in ['positive', 'negative', 'neutral']}
    return pd.Series(counts)

counts_df = questions.apply(count_values, axis=1)

# Concatenate the counts DataFrame with the original one
questions = pd.concat([questions, counts_df], axis=1)
questions.drop(columns=comments, inplace=True)
questions.drop(columns=['sentiment', 'title'], inplace=True)

print(questions.head())

# Save the data to a new file
questions.to_csv('statements_clean.csv', index=False)