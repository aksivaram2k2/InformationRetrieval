#       Objective - Identify Words to be ignored based on - Ignore any word that occurs in more than 50%
#       Updated             18/11/2015
#       
#       Pre-requisites - Two local folders Class1 and Class2 are available in folder where program is run, stop-words-english.txt also present 
#       Output will be program StopDocumentFrequencyTerms.txt which will contain words that need to be skipped in successive steps
#

import os
from xml.dom import minidom
import operator
import numpy as np
import re
from nltk.stem import PorterStemmer

#Initialize collection to store results for term, log and augmented frequency
words_table_data = {}
words_sum_data = {}
words_diff_data = {}
ps = PorterStemmer()
regex = re.compile('[^a-zA-Z]')
    
#Read Stop words
fp = open("stop-words-english.txt")
data = fp.read().decode("utf-8-sig").encode("utf-8")
stopwords = data.split()

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
            if word in words_table_data:
                #Increment Document Frequency
                words_table_data[word] = words_table_data[word]+1
            else:
                #Intialize Document Frequency
                words_table_data[word] = 1

ParseFolder('Class1')
dataset1 = words_table_data.items()

words_table_data = {}
ParseFolder('Class2')
dataset2 = words_table_data.items()

#Sum of two DataSets and consider only those > 500 occurences
def comp_sum(list1, list2):
    for key, val in list1:
        for key1, val1 in list2:
            #sum up values for matching keys
            if key == key1:
                if((val+val1 >= 500)):
                    words_sum_data[key1] = val+val1
    return

#Write results to file
def sumresultfrequency(outputfilename, words_table_data_sorted):
    f = open(outputfilename, 'w')
    for k,v in words_table_data_sorted:
        print >>f, k
    f.close()

#Compute sum between two DataSets
comp_sum(dataset1, dataset2)

#Sort based on value
words_sum_data_sorted = sorted(words_sum_data.items(), key=operator.itemgetter(1), reverse=True)

#Print Results to File
sumresultfrequency('StopDocumentFrequencyTerms.txt',words_sum_data_sorted)
