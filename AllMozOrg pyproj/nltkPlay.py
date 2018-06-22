import nltk
text = nltk.word_tokenize("Don't you know that we are going out? Just you and me.")
print(nltk.pos_tag(text))
#
# [('We', 'PRP'), ('are', 'VBP'), ('going', 'VBG'), ('out.Just', 'JJ'),
#  ('you', 'PRP'), ('and', 'CC'), ('me', 'PRP'), ('.', '.')]