from nltk.sentiment.vader import SentimentIntensityAnalyzer

#file = open("html_stripped_review.txt","r")

#rev = file.readlines()
def sen(rev):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = ""
    ss = sid.polarity_scores(rev)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
