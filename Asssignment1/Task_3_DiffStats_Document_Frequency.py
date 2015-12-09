#       About - Compute Document Stats for Sum, Differences
#       Updated             28/10/2015
#       Step 1 - Iterate through all documents for Data set
#       Step 2 - Compute document frequency for each of words excluding stop words
#       Document Frequency(word) = Occurrenceboolean(word in file1) + Occurrenceboolean(word in file2).. Occurrenceboolean(word in file500) 
#       Stop words, Special Characters, Digits removed
#       Pre-requisites - DataSet1 and DataSet2 should be locally available in folder where program is run
#       Output will be 2 files for each Input DataSets - Sum_Document_Frequency_words and Diff_Document_Frequency_words

import os
from xml.dom import minidom
import operator
import numpy as np
import re

#Initialize collection to store results for term, log and augmented frequency
words_table_data = {}
words_sum_data = {}
words_diff_data = {}

#Read Stop words
fp = open("stop-words-english.txt")
data = fp.read().decode("utf-8-sig").encode("utf-8")
stopwords = data.split()
#print stopwords

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
    DataValue = re.sub(r'[|,?.!/;:\'#@!~^&*_:;?><$%()-]', ' ',DataValue)
    DataValue = filter(lambda c: not c.isdigit(), DataValue)
    DataValue = DataValue.strip()
    DataValue = DataValue.lower()
    ParseTerms(DataValue)

#Word count logic
def ParseTerms(DataValue):
    #print DataValue
    words = DataValue.split()
    uniqWords = sorted(set(words))
    #For every word in document
    for word in uniqWords:
        if word.lower() not in stopwords:
            if word in words_table_data:
                #Increment Document Frequency
                words_table_data[word] = words_table_data[word]+1
            else:
                #Intialize Document Frequency
                words_table_data[word] = 1

ParseFolder('Dataset-1')
dataset1 = words_table_data.items()

words_table_data = {}
ParseFolder('Dataset-2')
dataset2 = words_table_data.items()

#Sum of two DataSets
def comp_sum(list1, list2):
    for key, val in list1:
        for key1, val1 in list2:
            if key == key1:
                words_sum_data[key1] = val+val1
    return

#Difference of two DataSets
def comp_diff(list1, list2):
    for key, val in list1:
        for key1, val1 in list2:
            if key == key1:
                words_diff_data[key1] = val-val1
    return

#Write results to file
def sumresultfrequency(outputfilename, words_table_data_sorted):
    f = open(outputfilename, 'w')
    for k,v in words_table_data_sorted:
        print >>f, ' Term-', k, ',sum document frequency-', v
    f.close()

#Write results to file
def diffresultfrequency(outputfilename, words_table_data_sorted):
    f = open(outputfilename, 'w')
    for k,v in words_table_data_sorted:
        print >>f, ' Term-', k, ',Diff document frequency-', v
    f.close()

#Compute sum between two DataSets
comp_sum(dataset1, dataset2)

#Compute differences between two DataSets
comp_diff(dataset1, dataset2)

#Sort based on value
words_sum_data_sorted = sorted(words_sum_data.items(), key=operator.itemgetter(1), reverse=True)
#Sort based on value
words_diff_data_sorted = sorted(words_diff_data.items(), key=operator.itemgetter(1), reverse=True)

#Print Results to File
sumresultfrequency('Task3 - Sum_Document_Frequency_words.txt',words_sum_data_sorted)

#Print Results to File
diffresultfrequency('Task3 - Diff_Document_Frequency_words.txt',words_diff_data_sorted)
