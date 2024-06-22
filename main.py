import string
import random
from textblob import TextBlob
from nltk.util import ngrams
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer('data/vader_lexicon/vader_lexicon.txt')

tag = "\n\n  &nbsp;  \n\n  &nbsp;  \n\n [^(mrhypnopotato)](https://www.reddit.com/user/mrhypnopotato) ^| [^(github)]({})".format("https://github.com/og-nav/lichess_good_chesscom_bad_bot")


#RUDIMENTARY SENTIMENT ANALYSIS (DECIDES WHETHER OR NOT TO REPLY OR NOT)
def sentiment(comment):
	if('lichess is better' in comment):# or 'preferred lichess' in comment or 'prefer lichess' in comment):
		return True
	
	total = sia.polarity_scores(comment) #entire comment
	totaltb = TextBlob(comment).sentiment
	c = []
	l = []
	r = []

	ccom = 0	
	lcom = 0
	rcom = 0
	tcom = total['compound']

	for n in range(2, 6):
		grams = [' '.join(gram) for gram in ngrams(comment.split(' '), n)]
		for gram in grams:
			res = sia.polarity_scores(gram)
			if('chesscom' in gram):
				c.append(res)
				ccom += res['compound']
			elif('lichess' in gram):
				l.append(res)
				lcom += res['compound']
			else:
				r.append(res)
				rcom += res['compound']
	
	
	#basic criteria: overall comment is opionated and lichess is rated more favorably than chesscom
	#this is a satire bot anyways so it is fine to get some wrong, but also need to avoid spam

	ccom /= max(len(c), 1) #try to normalize + avoid divide by 0
	lcom /= max(len(l), 1)
	rcom /= max(len(r), 1)

	if(totaltb.subjectivity > 0.6 and totaltb.polarity <= 0 or (ccom < lcom and rcom < 0) or tcom < -0.5):
		return True

	return False

#QUICKLY CHECKS FOR APPLICABLE KEYWORDS BEFORE ANY SENTIMENT STUFF ETC
def keywords_exist(comment):
	#TODO INCLUDE TYPOS AND DIFFERENT SPELLINGS maybe precompute Levenshtein distances < 2 + MINIMIZE HARDCODED VALUES
	if('lichess is better' in comment or ('lichess' in comment and 'chesscom' in comment)):
		return True
	return False


def normalize_string(comment):
	return comment.translate(str.maketrans('', '', string.punctuation)).lower()


def main():
	#AGGREGATING BOT REPLIES + STRIPPING \n
	file_bot_replies = open('bot_replies.txt', 'r')
	bot_replies = [row[0:len(row) - 1] for row in file_bot_replies.readlines()]
	file_bot_replies.close()

	main_reply = 'lichess good, chesscom bad!'

	#REDDIT AUTH
	import praw
	import os
	from dotenv import load_dotenv
	load_dotenv()
	CLIENT_ID = os.getenv('CLIENT_ID')
	CLIENT_SECRET = os.getenv('CLIENT_SECRET')
	USERNAME = os.getenv('USERNAME')
	PASSWORD = os.getenv('PASSWORD')
	USER_AGENT = os.getenv('USER_AGENT')
	reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, username=USERNAME, password=PASSWORD, user_agent=USER_AGENT)
	subreddit = reddit.subreddit('chess+AnarchyChess')

	#STREAM READS IN ALL NEW COMMENTS
	for comment in subreddit.stream.comments(skip_existing=True):
		normalized_comment = normalize_string(comment.body)
		if(not keywords_exist(normalized_comment)):
			continue
		if(sentiment(normalized_comment)):
			comment.reply(random.choice(bot_replies) + ' ' + main_reply + tag)
			print('REPLIED')
		


if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print(e)