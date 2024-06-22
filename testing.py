from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer

#polarity -> [-1.0, 1.0]
#subjectivity -> [0.0, 1.0]
sentence = 'What\'s wrong with chess.com? Is that normal?'


analysis = TextBlob(sentence).sentiment
print(analysis.subjectivity)
#sia = SentimentIntensityAnalyzer('data/vader_lexicon/vader_lexicon.txt')
#score = sia.polarity_scores(sentence)
#print(score)

#Pickle NOTE
#with open('data/posts_replied_to.pickle', 'wb') as handle:
	#pickle.dump({'Navin': ['sup', 'chilling', 'u']}, handle, protocol=pickle.HIGHEST_PROTOCOL)

#with open('data/posts_replied_to.pickle', 'rb') as handle:
#	d = pickle.load(handle)

#for submission in subreddit.hot(limit=5):
	#print('Title', submission.comments)

#test cases
#print(sentiment('chesscom is terrible but lichess is much better'))
#print(sentiment(normalize_string('chesscom is worse than lichess. its ui is ugly. lichess is great')))
#print(sentiment(normalize_string('What\'s wrong with chess.com? Is that normal?')))
#print(sentiment(normalize_string('chesscom gets something like 16,000 moves per second according to their recent blog post. I feel like Lichess is going to a good bit lower than that. For all the huffing and comparison between the two, imo Chesscom is handling things pretty well. And personally after a couple of bad days, I haven\'t had any issue, probably for the past 5-7 days. I just avoid peak hours (12-4pm EST) and aside from the occasional momentary disconnect while I\'m thinking, I have no issues That said, if I played blitz or bullet, maybe I\'d have more of an issue. but in Rapid I don\'t feel anything wrong. I think the best thing about Lichess comparisons is that Lichess helps deflect some of the traffic which improves the situation for everyone')))
	

#graveyard
#def save_reply(username, comment_id):#called after replying and username with comment id are saved in a public registry
#	with open('data/posts_replied_to.pickle', 'rb') as handle:
#		data = pickle.load(handle)
#	
#	if(username in data):
#		data[username].append(comment_id)
#	else:
#		data[username] = [comment_id]
#
#	with open('data/posts_replied_to.pickle', 'wb') as handle:
#		pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)