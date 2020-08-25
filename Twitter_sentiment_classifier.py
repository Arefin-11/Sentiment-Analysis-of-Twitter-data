punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# Removing punctuations
def strip_punctuation(w):
    new=""
    for i in range(len(w)):
        if w[i] not in punctuation_chars:
            new+=w[i]
    return new
# list of positive words to use
positive_words = []
pos_f=open("positive_words.txt")
for lin in pos_f:
    if lin[0] != ';' and lin[0] != '\n':
        positive_words.append(lin.strip())
def get_pos(stri):
    words=stri.strip().split()
    ct=0
    for word in words:
        word=strip_punctuation(word).lower()
        if word in positive_words:
            ct+=1
    return ct
# list of negative words to use
negative_words = []
neg_f=open("negative_words.txt")
for lin in neg_f:
    if lin[0] != ';' and lin[0] != '\n':
        negative_words.append(lin.strip())
def get_neg(stri):
    words=stri.strip().split()
    ct=0
    for word in words:
        word=strip_punctuation(word).lower()
        if word in negative_words:
            ct+=1
    return ct

# Opening CSV file
outfile=open("project_twitter_data.csv",'r')
# list of all words
n_pos_w={}
n_neg_w={}
n_ret={}
n_rep={}
words_lst=[]
for line in outfile:
    text = line.strip().split(',')
    n_ret[text[0]] = text[1]
    n_rep[text[0]] = text[2]
    n_pos_w[text[0]] = get_pos(text[0])
    n_neg_w[text[0]] = get_neg(text[0])
    if text[0]!="tweet_text":
        words_lst.append(text[0])

# Creating a new CSV
new_file=open("resulting_data.csv",'w')
new_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
new_file.write("\n")
for tweet in words_lst:
    new_lin='{},{},{},{},{}'.format(n_ret[tweet],n_rep[tweet],n_pos_w[tweet],n_neg_w[tweet],(n_pos_w[tweet]-n_neg_w[tweet]))
    new_file.write(new_lin)
    new_file.write("\n")
new_file.close()
