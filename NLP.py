# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:24:02 2019

@author: Pranit
"""

import nltk
nltk.download()
import re
sent1 = "this is my first sentense. this sentense has some lines and words. this is the third sentense"

# split para into words
# \s = space
re.split(r"\s", sent1)

# split at a letter - exlcude letter
re.split("e", sent1)

## spilt at word
re.split("sentense",sent1)

## spilt on range of characters
re.split(r"[a-z]",sent1)

## spilt on combination of words
re.split(r"is [a-z]",sent1)

# 2) pattern matching
sent2 = "The Cat is chasing the Mouse in the Room"

# extract all capital letters
re.findall(r'[A-Z][a-z]+',sent2)
re.findall(r'[A-Z][a-z]*',sent2)  # *for stating with zero

# extract all word start with small letters
re.findall(r'\s[a-z]+',sent2)
re.findall(r'\s[a-z]*',sent2)

# get all email ids from yhe sentence
sent3  = "primary email id is pranitshinde@gmail.com, secondary email id pranit@hotmail.com"

re.findall(r'\s[\w]+@[\w]+', sent3)

# find one particular pattern of email eg : gmail
sent4  = "primary email id is pranitshinde@gmail.com, secondary email id pranit@hotmail.com, pranit@gmail.com"

re.findall(r"\s[\w]+@gmail[\w.]+", sent4)


# find values within an XMl tag
sent5 = "<itemcode>BK100IM10018</itemcode>"


re.findall(r'>(\w+)</', sent5)

# 3) extract number from sentence

sent6 = "there are 7 days , 12 week , 3600, 54862"

re.findall(r"\d{5}", sent6) # all 5 digit
re.findall(r'\d{4}', sent6)
re.findall(r'(?<=\s)\d{4}(?![0-9])', sent6)

re.findall(r'(?<=\s)\d{1}(?![0-9])', sent6)


#################################################
## NLTK

import nltk

sent1 = "the resources can be classified as Natural and aman-made.Natural resources are unlimited .man made resources can get depleted sooner or later "

nltk.word_tokenize(sent1)  # word split

nltk.sent_tokenize(sent1)  # sentence

# stop words
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

stop_words.update({"|-","--", ">"})

print(stop_words)

sent2 = "the boy was behaving badly and very impolite "

words = nltk.word_tokenize(sent2)

set(words).difference(stop_words)

## Part of speech tagging POS

sent3 = "the old man is walking on the road slowly"

words = nltk.word_tokenize(sent3)
print(words)

pos_words = nltk.pos_tag(words)

print(pos_words)

## get only the Nouns

nouns = ['NN', 'NNS', 'NNP', 'NNPS']

for w,p in pos_words:
    if (p in nouns):
        print("{0} is a noun". format(w))
        
        
## similarly extract the adjective adverbs, verbs

## n-grams        

from textblob import TextBlob as tb

blob = tb(sent3)

n1 = blob.ngrams(n=1)
n2 = blob.ngrams(n=2)
n3 = blob.ngrams(n=3)
n4 = blob.ngrams(n=4)

n2

