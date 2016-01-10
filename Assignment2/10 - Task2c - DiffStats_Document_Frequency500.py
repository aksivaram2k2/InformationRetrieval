#       About - Create Dictionary for Class1 and Class 2 for Top 750,500, 200, 100, 50 items
#       Updated             28/10/2015

import os
from xml.dom import minidom
import operator
import numpy as np
import re
from nltk.stem import PorterStemmer
import copy

ps = PorterStemmer()

#Initialize collection to store results for term, log and augmented frequency
words_table_data = {}
words_sum_data = {}
words_diff_data = {}

#Read Stop words
fp = open("stop-words-english.txt")
data = fp.read().decode("utf-8-sig").encode("utf-8")
stopwords = data.split()
#print stopwords

fp = open("StopDocumentFrequencyTerms.txt")
data = fp.read().decode("utf-8-sig").encode("utf-8")
docfreqstopwords = data.split()

#File Parse Logic, Loop for every file in folder
def ParseFolder(path):
    for filename in os.listdir(path):
        fullname = os.path.join(path, filename)
        ParseFile(fullname)

#This method with fetch input data, data clean up
#Methods invoked - Frequency computing method ParseTerms
def ParseFile(fullname):
    doc = minidom.parse(fullname)
    txtData = doc.getElementsByTagName('TEXT')
    DataValue = txtData[0].firstChild.nodeValue
    DataValue = str(DataValue)
    DataValue = re.sub(r'[^a-zA-Z\n]', ' ',DataValue)
    DataValue = DataValue.strip()
    DataValue = DataValue.lower()
    ParseTerms(DataValue)

#Word count logic
def ParseTerms(DataValue):
    #print DataValue
    tempwords = DataValue.split()
    i = 0
    words = []
    for word in tempwords:
        stemmedword = PorterStemmer().stem_word(word)
        words.append(stemmedword)    
    uniqWords = sorted(set(words))
    #For every word in document
    for word in uniqWords:
        if word.lower() not in stopwords:
            if word.lower() not in docfreqstopwords:
                if word in words_table_data:
                    #Increment Document Frequency
                    words_table_data[word] = words_table_data[word]+1
                else:
                    #Intialize Document Frequency
                    words_table_data[word] = 1

#Difference of two DataSets
def comp_diff(list1, list2):
    for key, val in list1.items():
        for key1, val1 in list2.items():
            if key == key1:
                words_diff_data[key1] = val-val1
    return words_diff_data


#Write results to file
def diffresultfrequency(outputfilename, words_sum_data_sorted_ds1, CountVal):
    N=CountVal
    i = 0
    f = open(outputfilename, 'w')
    for k,v in words_sum_data_sorted_ds1:
        print >>f, k 
        i = i +1
        if(i ==N):
            break
    i = CountVal
    new_list = words_sum_data_sorted_ds1[-CountVal:]
    for k,v in new_list:
        print >>f, k 
        i = i-1
        if(i ==0):
            break
    f.close()

ParseFolder('Class1')
#dataset1 = words_table_data.items()
dataset1 = words_table_data

words_table_data = {}
ParseFolder('Class2')
#dataset2 = list.copy(words_table_data.items())
dataset2 = words_table_data

#Compute differences between two DataSets
words_diff_data = comp_diff(dataset1, dataset2)

#Sort based on value
words_sum_data_sorted_ds1 = sorted(words_diff_data.items(), key=operator.itemgetter(1), reverse=True)

#Print Results to File
diffresultfrequency('Diff_Document_Frequency_words_500.txt',words_sum_data_sorted_ds1, 500)
