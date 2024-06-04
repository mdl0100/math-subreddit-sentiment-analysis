############################################
##              Marcos Lopez              ##
##      Natural Language Processing       ##
##              VADER Analysis            ##
############################################

# Description
# This script will analyze the VADER sentiment analysis results for both questions and statements.
# and print the results to the console.

import pandas as pd

with open('vader_questions.csv', encoding='utf-8') as f:
    df = pd.read_csv(f)

pos_qs = df[df['sentiment'] == 'positive']
neg_qs = df[df['sentiment'] == 'negative']
nuet_qs = df[df['sentiment'] == 'neutral']

print('Questions:')
print('-'*10)
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

############################################
##              Statements               ##
############################################

with open('vader_statements.csv', encoding='utf-8') as f:
    df = pd.read_csv(f)

pos_qs = df[df['sentiment'] == 'positive']
neg_qs = df[df['sentiment'] == 'negative']
nuet_qs = df[df['sentiment'] == 'neutral']

print('\nStatements:')
print('-'*10)
print('Positive statements:', len(pos_qs))
print('Negative statements:', len(neg_qs))
print('Neutral statements:', len(nuet_qs))

# Find avg pos, neg, and nuet scores
print('Positive sentiment')

pq_pos_avg = pos_qs['positive'].mean()
pq_pos_count = pos_qs['positive'].sum()
print('Positive statements avg:', pq_pos_avg, 'count:', pq_pos_count)

nq_pos_avg = neg_qs['positive'].mean()
nq_pos_count = neg_qs['positive'].sum()
print('Negative statements avg:', nq_pos_avg, 'count:', nq_pos_count)

neuq_pos_avg = nuet_qs['positive'].mean()
neuq_pos_count = nuet_qs['positive'].sum()
print('Neutral statements avg:', neuq_pos_avg, 'count:', neuq_pos_count)

print()

print('Negative sentiment')

pq_neg_avg = pos_qs['negative'].mean()
pq_neg_count = pos_qs['negative'].sum()
print('Positive statements avg:', pq_neg_avg, 'count:', pq_neg_count)

nq_neg_avg = neg_qs['negative'].mean()
nq_neg_count = neg_qs['negative'].sum()
print('Negative statements avg:', nq_neg_avg, 'count:', nq_neg_count)

neuq_neg_avg = nuet_qs['negative'].mean()
neuq_neg_count = nuet_qs['negative'].sum()
print('Neutral statements avg:', neuq_neg_avg, 'count:', neuq_neg_count)

print()

print('Neutral sentiment')

pq_neut_avg = pos_qs['neutral'].mean()
pq_neut_count = pos_qs['neutral'].sum()
print('Positive statements avg:', pq_neut_avg, 'count:', pq_neut_count)

nq_neut_avg = neg_qs['neutral'].mean()
nq_neut_count = neg_qs['neutral'].sum()
print('Negative statements avg:', nq_neut_avg, 'count:', nq_neut_count)

neuq_neut_avg = nuet_qs['neutral'].mean()
neuq_neut_count = nuet_qs['neutral'].sum()
print('Neutral statements avg:', neuq_neut_avg, 'count:', neuq_neut_count)

