###############################################
##                Marcos Lopez               ##
##        Natural Language Processing        ##
##initial Data Processing and SpaCY analysis ##
###############################################

# Description
# This script will read the math.csv file and apply the sentiment analysis to the post titles and comments
# It then replaces the comments with the sentiment scores
# Splits the data into questions and statements
# And then saves the data to two new files: questions.csv and statements.csv
# More data cleaning is then done in question.py to clean the data further

import pandas as pd 
import eng_spacysentiment 

# This code is used to read the math.csv file and apply the sentiment analysis to the post titles and comments
# It then replaces the comments with the sentiment scores
# Splits the data into questions and statements
# And then saves the data to two new files: questions.csv and statements.csv
# More data cleaning is then done in question.py to clean the data further


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

analyzer = eng_spacysentiment.load() # Load the English sentiment analyzer

###########################################
##              Questions                ##
###########################################

questions['sentiment'] = questions['title'].apply(analyzer) # Apply the sentiment function to the questions
questions['Spacy_sentiment'] = questions['sentiment'].apply(lambda x: x.cats) # Get the sentiment scores
questions['Spacy_sentiment'] = questions['Spacy_sentiment'].apply(lambda x: max(x, key=x.get)) # Get the sentiment with the highest score


# Go through the Comments and replace each comment with its sentiment score
questions['C1'] = questions['C1'].apply(analyzer)
questions['C1'] = questions['C1'].apply(lambda x: max(x.cats, key=x.cats.get)) # Apply the sentiment function to the questions

questions['C2'] = questions['C2'].apply(analyzer)
questions['C2'] = questions['C2'].apply(lambda x: max(x.cats, key=x.cats.get)) # Apply the sentiment function to the questions

questions['C3'] = questions['C3'].apply(analyzer)
questions['C3'] = questions['C3'].apply(lambda x: max(x.cats, key=x.cats.get)) # Apply the sentiment function to the questions

questions['C4'] = questions['C4'].apply(analyzer)
questions['C4'] = questions['C4'].apply(lambda x: max(x.cats, key=x.cats.get)) # Apply the sentiment function to the questions

questions['C5'] = questions['C5'].apply(analyzer)
questions['C5'] = questions['C5'].apply(lambda x: max(x.cats, key=x.cats.get)) # Apply the sentiment function to the questions

# print(questions.head())

# Save the questions to a new file
questions.to_csv('questions.csv', index=False) # Save the data without actual comments, just the sentiment replacing comments
###########################################
##              Statements               ##
###########################################
statements['sentiment'] = statements['title'].apply(analyzer) # Apply the sentiment function to the statements
statements['Spacy_sentiment'] = statements['sentiment'].apply(lambda x: x.cats) # Get the sentiments scores
statements['Spacy_sentiment'] = statements['Spacy_sentiment'].apply(lambda x: max(x, key=x.get)) # Get the sentiment with the highest score

statements['C1'] = statements['C1'].apply(analyzer) # Apply the sentiment function to the statements
statements['C1'] = statements['C1'].apply(lambda x: max(x.cats, key=x.cats.get)) # Get the sentiment with the highest score

statements['C2'] = statements['C2'].apply(analyzer) # Apply the sentiment function to the statements
statements['C2'] = statements['C2'].apply(lambda x: max(x.cats, key=x.cats.get)) # Get the sentiment with the highest score

statements['C3'] = statements['C3'].apply(analyzer) # Apply the sentiment function to the statements
statements['C3'] = statements['C3'].apply(lambda x: max(x.cats, key=x.cats.get)) # Get the sentiment with the highest score

statements['C4'] = statements['C4'].apply(analyzer) # Apply the sentiment function to the statements
statements['C4'] = statements['C4'].apply(lambda x: max(x.cats, key=x.cats.get)) # Get the sentiment with the highest score

statements['C5'] = statements['C5'].apply(analyzer) # Apply the sentiment function to the statements
statements['C5'] = statements['C5'].apply(lambda x: max(x.cats, key=x.cats.get)) # Get the sentiment with the highest score

print(statements.head())

# Save the data to a new file
statements.to_csv('statements.csv', index=False) # Save the data without actual comments, just the sentiment replacing comments
