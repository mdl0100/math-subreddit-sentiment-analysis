# r/math Sentiment Analysis
r/math is a popular subreddit on the subject of mathematics. Usually its topics revolve around news, compeitions updates, adnvances in mathematics, advice for students, faculty, and professionals alike. It is not usually used for things like homework help (shoutout r/learnmath)

### Summary
This project was done to see if the sentiment of a post affected the sentiment of the comments that followed. 
It was also wondered if the original post being phrased in the form of a question helped or hurt the sentiment of the comments. 
Sentiment Analysis was done twice, first with SpaCY and then with VADER

### Files
| name  |file   |
|---|---|
| main.py  | read the data set from the .csv downloaded from huggingface.co, replacing comments with sentiment scores, and separating statement and question posts  |
| q_analysis.py | Analysis on question posts with SpaCY |
| question.py | Futher data cleanup for q_analysis.py, outputs questions_clean.csv|
|questions.csv| Separated questions, one of the outputs of main.py|
| questions_clean.csv | Holds the resulting category for each post with a count for how many positive, negative, and neutral comments it had  | 
| s_analysis.py | Analysis on statement posts with SpaCY |
| statments.csv | Separated statements, one of the outputs of main.py|
| statements_clean.csv | Holds the resulting category for each post with a count for how many positive, negative, and neutral comments it had  | 
|vader_*.py | Same as above but using the VADER package for sentiment analysis instead of SpaCY|

### Methodogy
Each post was separated into Statements and Questions, and had sentiment analysis run on it to give it a grade of Positive, Negative, or Neutral tone. 
For each post, its comments were then also run through either SpaCY or VADER (different runs) to have their sentiment categorized in the same way. 

## Findings
Both SpaCY and VADER categorized mostly positive positive reponses posts regardless of it's seniment. However, onced comparred to the number of neutral comments for each category, it was clear that:
- A poster can expect roughly 3.081 positive comments on positive sounding postsformed as a question, and 2.654 postive comments on negative sounding posts.
- If the post is formed as a statement, this expectation does not change much.
- While posting a positive question increases the expected positive comments by 0.203 when compared to a neutral statement, forming the post as a statement shows almost no change from neutral questions.
- Posting a negative question increases negative comments by an expecation of 0.475 from neutral, with half coming from expected positive comments, and half from expected neutral comments.
- If poster gives a negative statement, they can expect only 0.364 more negative comments when compared to a neutral question.

  | Posts | Positive | Negative  |
  |--|-|-|
  |Questions | ↗️✅0.203 ↘️ ❌ 0.224 | ➖✅ 0.066 ↗️❌ 0.475 |
  | Statements| ➖✅0.026 ↘️❌ 0.230 | ➖✅ 0.004 ↗️❌ 0.364 | 
### Resources
Data was provided by [huggingface.co](https://huggingface.co/datasets/P1ayer-1/reddit-math), which had a all posts to r/math from inception up to March 2023, and recorded the top five comments for each post.  
- 78,177 posts with 390,885 total comments, some of which are null.

