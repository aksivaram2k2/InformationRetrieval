#       About - Compute Document Stats
#       Updated             28/10/2015
#       Step 1 - Iterate through all documents for Data set
#       Step 2 - Compute document frequency for each of words excluding stop words
#       Document Frequency(word) = Occurrenceboolean(word in file1) + Occurrenceboolean(word in file2).. Occurrenceboolean(word in file500) 
#       Stop words, Special Characters, Digits removed
#       Pre-requisites - DataSet1 and DataSet2 should be locally available in folder where program is run
#       Output will be 4 files for Input DataSet - Document Frequncy, Top 50 Document Frequency for both the DataSets

import os
from xml.dom import minidom
import math
import operator
import re

#Initialize collection to store results for term, log and augmented frequency
words_table_data = {}

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
    DataValue = re.sub(r'[|,?.!/;:\'#@!~^&*_:;?><$%()-]', ' ',DataValue)     #Remove Special Characters
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

#Output Document Frequency
def outputdataresult(outputfilename, words_table_data_sorted):
    f = open(outputfilename, 'w')
    for k,v in words_table_data_sorted:
        #Print document frequency
        print >>f, ' Term-', k, ',Document Frequency-', v
    f.close()

#Print Top 50 Words
def printtop50stats(filepath, outputfilepath):
    N=50
    #Open file
    f = open(filepath)
    fout = open(outputfilepath, 'w')
    #Fetch Top 50 results
    for i in range(N):
        line=f.next().strip()
        print>>fout, line
    f.close()
    fout.close()
    
ParseFolder('Dataset-1')
words_table_data_sorted_dataset1 = sorted(words_table_data.items(), key=operator.itemgetter(1), reverse=True)
words_table_data_sorted_alphabetically_dataset1 = sorted(words_table_data.items(), key=operator.itemgetter(0))
outputdataresult('Task1b_Dataset1_Document_frequency.txt',words_table_data_sorted_dataset1)
printtop50stats('Task1b_Dataset1_Document_frequency.txt','Task1c -Top50_Dataset1_Document_frequency.txt')

words_table_data = {}
ParseFolder('Dataset-2')
words_table_data_sorted_dataset2 = sorted(words_table_data.items(), key=operator.itemgetter(1), reverse=True)
words_table_data_sorted_alphabetically_dataset2 = sorted(words_table_data.items(), key=operator.itemgetter(0))
outputdataresult('Task1b_Dataset2_Document_frequency.txt',words_table_data_sorted_dataset2)
printtop50stats('Task1b_Dataset2_Document_frequency.txt','Task1c -Top50_Dataset2_Document_frequency.txt')
