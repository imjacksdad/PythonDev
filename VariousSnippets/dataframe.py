##import pandas as pd
##import numpy as np
##
##df = pd.read_csv('..\\Support Files\\StoneX\\GAVPOS.csv')
##
###print(df.head())
##
##to_drop = ['PRECID','PDEAL']
##
##df.drop(to_drop, inplace=True, axis=1)
##
###print(df.head())
##
##pmt = df['PCMNT1']
##pmtcode = pmt.str.contains('2')
##print(pmtcode[:2])
##
#################################
##
##def countdown(n):
##    print(n)
##    if n > 0:
##        countdown(n-1)
##
##countdown(7)
##
##################################
##


#https://realpython.com/natural-language-processing-spacy-python/
import spacy

text = """Dave watched as the forest burned up on the hill,
only a few miles from his house. The car had
been hastily packed and Marta was inside trying to round
up the last of the pets. "Where could she be?" he wondered
as he continued to wait for Marta to appear with the pets."""

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
#print ([token.text for token in doc])

##sentences = list(doc.sents)
##print(len(sentences))
##
##for sentence in sentences:
##    print (sentence)

for token in doc:
    if token.text == "Marta":  #tokens are not strings.  Use .text to make a string
        print(token, token.idx, token.text_with_ws,
            token.is_alpha, token.is_punct, token.is_space,
            token.shape_, token.is_stop)
    else:
        print(token)


              
