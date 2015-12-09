#       About - Plot Document Stats
#       Updated             28/10/2015
#       Pre-requisites - DataSet1 and DataSet2 should be locally available in folder where program is run
#       Step 1 - Iterate through all documents for Data set
#       Step 2 - Compute document frequency for each of words excluding stop words
#           Formula - Document Frequency(word) = Occurrenceboolean(word in file1) + Occurrenceboolean(word in file2).. Occurrenceboolean(word in file500) 
#           Logic - Stop words, Special Characters, Digits removed
#       Step 3 - Based on Sorted by Document Frequency and position of Sorted order graph will be plotted,
#       Step 4 - X-Axis position and Y-Axis Document Frequency count
#       Step 5 - Output will be pdf file and plot image

import os
from xml.dom import minidom
import matplotlib.pyplot as plt
import numpy as np
import operator
import re

#Initialize collection to store results for term, log and augmented frequency
words_table_data = {}

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
                words_table_data[word] = words_table_data[word]+1
            else:
                words_table_data[word] = 1

ParseFolder('Dataset-1')
words_table_data_sorted_descending_dataset1 = sorted(words_table_data.items(), key=operator.itemgetter(1), reverse=True)

words_table_data = {}
ParseFolder('Dataset-2')
words_table_data_sorted_descending_dataset2 = sorted(words_table_data.items(),  key=operator.itemgetter(1), reverse=True)

def plotvalues(words_data,filename):
    i = 0
    #Initialize the X Coordinate Position
    for key, value in words_data:
        x = i
        #Fetch the Plot value for Y Axis (Sorted Order)
        y = value
        #Scatter Plot obtained X and Y Values
        plt.scatter(x, y)
        i = i+1
    #Save the plot as a Pdf file
    plt.savefig(filename)
    #Show the plotted values
    plt.show()

plotvalues(words_table_data_sorted_descending_dataset1,'Task2 - DataSet1_Plot.pdf')
plotvalues(words_table_data_sorted_descending_dataset2,'Task2 - DataSet2_Plot.pdf')
