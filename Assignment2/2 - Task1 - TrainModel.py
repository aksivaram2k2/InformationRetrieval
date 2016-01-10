#       About - Compute Model (Training Data) and output to text file
#       Updated             18/11/2015
#       Prerequisites - File stop-words-english.txt, StopDocumentFrequencyTerms.txt and two folders Class1 and Class2 locally available
#       Output - ModelFile.txt containing values for terms in class1 and class2

import os
from xml.dom import minidom
import math
import operator
import re
from collections import defaultdict
from decimal import Decimal, Context
from nltk.stem import PorterStemmer
import timeit

#Initialize collection to store results for term, log and augmented frequency
words_table_data = {}
d1_termfrequency = defaultdict(list)
d1_tf_sum_logval = {}
modeldata = {}
d1_tf_sum_sorted = {}

#Read Stop words
fp = open("stop-words-english.txt")
data = fp.read().decode("utf-8-sig").encode("utf-8")
stopwords = data.split()

ps = PorterStemmer()
fp = open("StopDocumentFrequencyTerms.txt")
data = fp.read().decode("utf-8-sig").encode("utf-8")
docfreqstopwords = data.split()

#File Parse Logic, Loop for every file in folder
def ParseFolder(path):
    for filename in os.listdir(path):
        fullname = os.path.join(path, filename)
        ParseFile(fullname)
    return d1_tf_sum_logval

#This method with fetch input data, data clean up, Frequency computing methods ParseTerms and building result set is done in outputdataresult method
def ParseFile(fullname):
    words_table_data = {}
    words_table_data_sorted_dataset1 = {}
    doc = minidom.parse(fullname)
    txtData = doc.getElementsByTagName('TEXT')
    DataValue = txtData[0].firstChild.nodeValue
    DataValue = str(DataValue)
    DataValue = re.sub(r'[^a-zA-Z\n]', ' ',DataValue)
    DataValue = DataValue.strip()
    DataValue = DataValue.lower()
    words_table_data = ParseTerms(DataValue)
    words_table_data_sorted_dataset1 = sorted(words_table_data.items(), key=operator.itemgetter(1), reverse=True)
    inputfilename = os.path.splitext(fullname)[0]
    outputdataresult(words_table_data_sorted_dataset1)  

#Word count logic
def ParseTerms(DataValue):
    words_table_data = {}
    tempwords = DataValue.split()
    i = 0
    words = []
    for word in tempwords:
        stemmedword = PorterStemmer().stem_word(word)
        words.append(stemmedword)
    uniqWords = sorted(set(words))
    for word in uniqWords:
        if word.lower() not in stopwords:
            if word.lower() not in docfreqstopwords:
                    count = words.count(word)
                    words_table_data[word] = count 
    return words_table_data

#Output Computed values of Term, Log and Augmented Term Frequency
def outputdataresult(words_table_data_sorted):
    #print maxfrequency
    for k,v in words_table_data_sorted:
        d1_termfrequency[k].append(v)

#compute distinct words, terms, Intermediate results
def computewordstats():
    d1 = dict((k, tuple(v)) for k, v in d1_termfrequency.iteritems())
    d1_tf_sum = dict((k, sum(tuple(v))) for k, v in d1.iteritems())
    d1_tf_sum_sorted = sorted(d1_tf_sum.items(), key=operator.itemgetter(1), reverse=True)
    noofwords = 0
    for k,v in d1_tf_sum_sorted:
        d1_tf_sum_logval[k] = v
    for key, value in d1_tf_sum_sorted:
        noofwords = noofwords  + value
    return noofwords,  len(d1)

#Compute values for Class1
ParseFolder('Class1')
(noofwordsds1, distinctwordsds1) = computewordstats()
print noofwordsds1, distinctwordsds1
ds1_model = d1_tf_sum_logval

#Compute values for Class2
words_table_data = {}
d1_termfrequency = defaultdict(list)
d1_tf_sum_logval = {}
d1_tf_sum_sorted = {}
ParseFolder('Class2')
(noofwordsds2, distinctwordsds2) = computewordstats()
print noofwordsds2, distinctwordsds2
ds2_model = d1_tf_sum_logval
print len(ds2_model)

#merge two Class1 and Class2 dictionary
start = timeit.default_timer()
model_words = dict(list(ds1_model.items()) + list(ds2_model.items()))
print len(model_words)

#compute and write to model file
f = open('ModelFile.txt', 'w')
for k,v in model_words.items():
    #Term in both classes
    if((k in ds1_model) and (k in ds2_model)):
        val1 = ds1_model[k]
        val2 = ds2_model[k]
        temp1 = noofwordsds1+len(model_words)
        temp2 = val1+1
        result1 = 0.000
        result1 = temp2/float(temp1)
        temp1 = noofwordsds2+len(model_words)
        temp2 = val2+1
        result2 = 0.000
        result2 = temp2/float(temp1)
        print >>f,k,result1,result2
    #Term in Class2
    elif(k in ds2_model):
        val1 = 0
        val2 = ds2_model[k]
        temp1 = noofwordsds1+len(model_words)
        temp2 = val1+1
        result1 = 0.000
        result1 = temp2/float(temp1)
        temp1 = noofwordsds2+len(model_words)
        temp2 = val2+1
        result2 = 0.000
        result2 = temp2/float(temp1)
        print >>f,k,result1,result2
    #term in Class1
    elif (k in ds1_model):
        val1 = ds1_model[k]
        val2 = 0
        temp1 = noofwordsds1+len(model_words)
        temp2 = val1+1
        result1 = 0.000
        result1 = temp2/float(temp1)
        temp1 = noofwordsds2+len(model_words)
        temp2 = val2+1
        result2 = 0.000
        result2 = temp2/float(temp1)
        print >>f,k,result1,result2
f.close()
stop = timeit.default_timer()

print 'Time to Train'
print stop-start 

f = open('ModelFileStats.txt', 'w')
print >>f,'Distinct Words in Class 1 -', str(distinctwordsds1)
print >>f,'Total Words in Class 1 -', str(noofwordsds1)
print >>f,'Distinct Words in Class 2 -', str(distinctwordsds2)
print >>f,'Total Words in Class 2 -', str(noofwordsds2)
print >>f,'Total Words in Dictinary -', str(len(model_words))
print >>f,'Time taken for training -', str(stop-start)
f.close()
