############################################
##              Marcos Lopez              ##
##      Natural Language Processing       ##
##      Question Analysis with SpaCY      ##
############################################

# Description
# This script will analyze the SpaCY sentiment analysis results for both questions and statements.
# and print the results to the console.

import pandas as pd

# Load the data
with open('questions_clean.csv', encoding='utf-8') as f:
    df = pd.read_csv(f)

pos_qs = df[df['Spacy_sentiment'] == 'positive']
neg_qs = df[df['Spacy_sentiment'] == 'negative']
nuet_qs = df[df['Spacy_sentiment'] == 'neutral']

print('Positive questions:', len(pos_qs))
print('Negative questions:', len(neg_qs))
print('Neutral questions:', len(nuet_qs))
print()

# Find avg pos, neg, and nuet scores
print('Positive sentiment')

pq_pos_avg = pos_qs['positive'].mean()
pq_pos_count = pos_qs['positive'].sum()
print('Positive questions avg:', pq_pos_avg, 'count:', pq_pos_count)
nq_pos_avg = neg_qs['positive'].mean()
nq_pos_count = neg_qs['positive'].sum()
print('Negative questions avg:', nq_pos_avg, 'count:', nq_pos_count)
neuq_pos_avg = nuet_qs['positive'].mean()
neuq_pos_count = nuet_qs['positive'].sum()
print('Neutral questions avg:', neuq_pos_avg, 'count:', neuq_pos_count)

print()
print('Negative sentiment')

pq_neg_avg = pos_qs['negative'].mean()
pq_neg_count = pos_qs['negative'].sum()
print('Positive questions avg:', pq_neg_avg, 'count:', pq_neg_count)
nq_neg_avg = neg_qs['negative'].mean()
nq_neg_count = neg_qs['negative'].sum()
print('Negative questions avg:', nq_neg_avg, 'count:', nq_neg_count)
neuq_neg_avg = nuet_qs['negative'].mean()
neuq_neg_count = nuet_qs['negative'].sum()
print('Neutral questions avg:', neuq_neg_avg, 'count:', neuq_neg_count)

print()
print('Neutral sentiment')
pq_neut_avg = pos_qs['neutral'].mean()
pq_neut_count = pos_qs['neutral'].sum()
print('Positive questions avg:', pq_neut_avg, 'count:', pq_neut_count)
nq_neut_avg = neg_qs['neutral'].mean()
nq_neut_count = neg_qs['neutral'].sum()
print('Negative questions avg:', nq_neut_avg, 'count:', nq_neut_count)
neuq_neut_avg = nuet_qs['neutral'].mean()
neuq_neut_count = nuet_qs['neutral'].sum()
print('Neutral questions avg:', neuq_neut_avg, 'count:', neuq_neut_count)

