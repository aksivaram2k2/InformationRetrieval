#       About - Run Tests and Predict Accuracy
#       Updated             18/11/2015
#       Prerequisites - File ModelFile50.txt, stop-words-english.txt, StopDocumentFrequencyTerms.txt and two folders Test\\Class1 and Test\\Class2 available
#       Output - Results for Class1 and Class2 Test Files

import os
from xml.dom import minidom
import operator
import numpy as np
import re
from collections import defaultdict
import math
from nltk.stem import PorterStemmer
import timeit

ps = PorterStemmer()

#Read Stop words
fp = open("stop-words-english.txt")
data = fp.read().decode("utf-8-sig").encode("utf-8")
stopwords = data.split()

fp = open("StopDocumentFrequencyTerms.txt")
data = fp.read().decode("utf-8-sig").encode("utf-8")
docfreqstopwords = data.split()

#python load data into dictionary
d1 = {}
d2 = {}

#Load Class Data from Model File, For Class1
with open("ModelFile50.txt") as f:
    for line in f:
        (key1, val1, val2) = line.split()
        d1[key1] = val1

#Load Class Data from Model File, For Class2
with open("ModelFile50.txt") as f:
    for line in f:
        (key1, val1, val2) = line.split()
        d2[key1] = val2

words_table_data = {}
d1_testresult = defaultdict(list)
d1_tiesresult = defaultdict(list)

#File Parse Logic, Loop for every file in folder
def ParseFolder(path):
    for filename in os.listdir(path):
        fullname = os.path.join(path, filename)
        ParseFile(fullname)

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
    dataset1val = 0.00
    dataset2val = 0.00

    #Compute log(probability value) obtained in earlier steps    
    for k,v in words_table_data_sorted_dataset1:
        if(d1.has_key(k)):
                val1 = float(d1[k])
                lvalds1 = float(math.log(val1,10))
                dataset1val = float(dataset1val + lvalds1)

    #Compute log(probability value) obtained in earlier steps
    for k,v in words_table_data_sorted_dataset1:
            if(d2.has_key(k)):
                val2 = float(d2[k])
                lvalds2 = float(math.log(val2,10))
                dataset2val = float(dataset2val + lvalds2)

    if dataset1val == dataset2val:
        d1_tiesresult[inputfilename] = 1
    elif(dataset1val > dataset2val):
        # 1 refers class1 match
        d1_testresult[inputfilename] = 1
    else:
        # 0 refers class2 match
        d1_testresult[inputfilename] = 0
    
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

start = timeit.default_timer()

#Class 1 Test Run
ParseFolder('Test\\Class1')
print 'Class1 Results'
print 'Class1 match is  - Pass Cases -', str(sum(d1_testresult.values()))
print 'Class2 match is - Fail Cases -',str(50-sum(d1_testresult.values())-sum(d1_tiesresult.values()))
print 'ties -', str(sum(d1_tiesresult.values()))
print 'Class 1 Failed Cases - Files'
for key, value in d1_testresult.iteritems() :
    if value ==0:
        print key, value

#Class 2 Test Run
d1_testresult = { }
ParseFolder('Test\\Class2')
print 'Class2 Results'
print 'Class1 match is - Failed Cases - ', str(sum(d1_testresult.values()))
print 'Class2 match is - Pass Cases - ', str(50-sum(d1_testresult.values())-sum(d1_tiesresult.values()))
print 'ties - ', str(sum(d1_tiesresult.values()))

print 'Class 2 Failed Cases - Files'
for key, value in d1_testresult.iteritems() :
    if value ==1:
        print key, value

stop = timeit.default_timer()
print 'Time to Test - ', str(stop-start)
print 'Size of Model file in KB -', str((os.path.getsize('ModelFile50.txt')/1000))

