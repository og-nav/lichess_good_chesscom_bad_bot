from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer

#polarity -> [-1.0, 1.0]
#subjectivity -> [0.0, 1.0]
sentence = 'lichess is okay but I prefer chesscom.'


#analysis = TextBlob(sentence).sentiment
#print(analysis)
sia = SentimentIntensityAnalyzer('data/vader_lexicon/vader_lexicon.txt')
score = sia.polarity_scores(sentence)
print(score)