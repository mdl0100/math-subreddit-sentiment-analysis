############################################
##              Marcos Lopez              ##
##      Natural Language Processing       ##
##     VADER Cleanup and Processing       ##
############################################

# Description
# This file reads in the math.csv file and applies the VADER sentiment analysis to the post titles and comments.
# It then replaces the comments with the sentiment scores and saves the data to two new files: vader_questions.csv and vader_statements.csv
# More data cleaning is then done in vader_analysis.py to analyze the data further.

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 

with open('math.csv', encoding='utf-8') as f:
    data = pd.read_csv(f)  # Read the data from the file

# Convert the Comment columns to strings
data['C1'] = data['C1'].astype(str) 
data['C2'] = data['C2'].astype(str) 
data['C3'] = data['C3'].astype(str) 
data['C4'] = data['C4'].astype(str) 
data['C5'] = data['C5'].astype(str) 


# Split the dataframe into questions and statements
questions = data[data['title'].str.endswith('?')].copy() # Get the questions
statements = data[~data['title'].str.endswith('?')].copy() # Get the statements

sia_obj = SentimentIntensityAnalyzer() # Load the English sentiment analyzer

###########################################
##              Questions                ##
###########################################

questions['sentiment'] = questions['title'].apply(lambda x: sia_obj.polarity_scores(x)['compound']) # Apply the sentiment function to the questions


# Go through the Comments and replace each comment with its sentiment score
questions['C1'] = questions['C1'].apply(lambda x: sia_obj.polarity_scores(x))
questions['C1'] = questions['C1'].apply(lambda x: x['compound']) # Apply the sentiment function to the questions

questions['C2'] = questions['C2'].apply(lambda x: sia_obj.polarity_scores(x))
questions['C2'] = questions['C2'].apply(lambda x: x['compound']) # Apply the sentiment function to the questions

questions['C3'] = questions['C3'].apply(lambda x: sia_obj.polarity_scores(x))
questions['C3'] = questions['C3'].apply(lambda x: x['compound']) # Apply the sentiment function to the questions

questions['C4'] = questions['C4'].apply(lambda x: sia_obj.polarity_scores(x))
questions['C4'] = questions['C4'].apply(lambda x: x['compound']) # Apply the sentiment function to the questions

questions['C5'] = questions['C5'].apply(lambda x: sia_obj.polarity_scores(x))
questions['C5'] = questions['C5'].apply(lambda x: x['compound']) # Apply the sentiment function to the questions

def analyzer(x):
    if x >= 0.05:
        return 'positive'
    elif x <= -0.05:
        return 'negative'
    else:
        return 'neutral'

questions['sentiment'] = questions['sentiment'].apply(analyzer) # Get the sentiment scores
questions['C1'] = questions['C1'].apply(analyzer)
questions['C2'] = questions['C2'].apply(analyzer)
questions['C3'] = questions['C3'].apply(analyzer)
questions['C4'] = questions['C4'].apply(analyzer)
questions['C5'] = questions['C5'].apply(analyzer)


comments = ['C1', 'C2', 'C3', 'C4', 'C5']
def count_values(row):
    counts = {value: row[comments].tolist().count(value) for value in ['positive', 'negative', 'neutral']}
    return pd.Series(counts)

counts_df = questions.apply(count_values, axis=1)

# Concatenate the counts DataFrame with the original one
questions = pd.concat([questions, counts_df], axis=1)
questions.drop(columns=comments, inplace=True)

print(questions.head())

###########################################
##              Statements               ##
###########################################

statements['sentiment'] = statements['title'].apply(lambda x: sia_obj.polarity_scores(x)['compound']) # Apply the sentiment function to the statements

# Go through the Comments and replace each comment with its sentiment score
statements['C1'] = statements['C1'].apply(lambda x: sia_obj.polarity_scores(x))
statements['C1'] = statements['C1'].apply(lambda x: x['compound']) # Apply the sentiment function to the statements

statements['C2'] = statements['C2'].apply(lambda x: sia_obj.polarity_scores(x))
statements['C2'] = statements['C2'].apply(lambda x: x['compound']) # Apply the sentiment function to the statements

statements['C3'] = statements['C3'].apply(lambda x: sia_obj.polarity_scores(x))
statements['C3'] = statements['C3'].apply(lambda x: x['compound']) # Apply the sentiment function to the statements

statements['C4'] = statements['C4'].apply(lambda x: sia_obj.polarity_scores(x))
statements['C4'] = statements['C4'].apply(lambda x: x['compound']) # Apply the sentiment function to the statements

statements['C5'] = statements['C5'].apply(lambda x: sia_obj.polarity_scores(x))
statements['C5'] = statements['C5'].apply(lambda x: x['compound']) # Apply the sentiment function to the statements

statements['sentiment'] = statements['sentiment'].apply(analyzer) # Get the sentiment scores
statements['C1'] = statements['C1'].apply(analyzer)
statements['C2'] = statements['C2'].apply(analyzer)
statements['C3'] = statements['C3'].apply(analyzer)
statements['C4'] = statements['C4'].apply(analyzer)
statements['C5'] = statements['C5'].apply(analyzer)

counts_df = statements.apply(count_values, axis=1)

# Concatenate the counts DataFrame with the original one
statements = pd.concat([statements, counts_df], axis=1)
statements.drop(columns=comments, inplace=True)

print(statements.head())

questions.to_csv('vader_questions.csv', index=False)
statements.to_csv('vader_statements.csv', index=False)

