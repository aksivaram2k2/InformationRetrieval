#       About - Compute Document Stats
#       Updated             28/10/2015
#       Step 1 - Iterate through all documents for Data set
#       Collective tf(word) = tf(word in file1) + tf(word in file2).. tf(word in file500) 
#       Collective logf(word) = logf(word in file1) + logf(word in file2).. logf(word in file500)
#       Collective augf(word) = augf(word in file1) + augf(word in file2).. augf(word in file500)
#       Stop words, Special Characters, Digits removed
#       Pre-requisites - DataSet1 and DataSet2 should be locally available in folder where program is run
#       Output will be 6 files for Input DataSet - Term, lograthmic, augmented and Top 50 of all of them

import os
from xml.dom import minidom
import math
import operator
import re
from collections import defaultdict

#Initialize collection to store results for term, log and augmented frequency
words_table_data = {}
d1_termfrequency = defaultdict(list)
d1_logfrequency  = defaultdict(list)
d1_augf  = defaultdict(list)

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
#Methods invoked - Frequency computing methods ParseTerms and building result set is done in outputdataresult method
def ParseFile(fullname):
    words_table_data = {}
    words_table_data_sorted_dataset1 = {}
    doc = minidom.parse(fullname)
    txtData = doc.getElementsByTagName('TEXT')
    DataValue = txtData[0].firstChild.nodeValue
    DataValue = str(DataValue)
    DataValue = re.sub(r'[|,?.!/;:\'#@!~^&*_:;?><$%()-]', ' ',DataValue) #Regex for removing special characters
    DataValue = filter(lambda c: not c.isdigit(), DataValue)
    DataValue = DataValue.strip()
    DataValue = DataValue.lower()
    words_table_data = ParseTerms(DataValue)
    words_table_data_sorted_dataset1 = sorted(words_table_data.items(), key=operator.itemgetter(1), reverse=True)
    inputfilename = os.path.splitext(fullname)[0]
    outputdataresult(words_table_data_sorted_dataset1) #Build the frequency dictionary for each file

#Word count logic
def ParseTerms(DataValue):
    words_table_data = {}
    words = DataValue.split()
    uniqWords = sorted(set(words))
    for word in uniqWords:
        if word.lower() not in stopwords:
                count = words.count(word)
                words_table_data[word] = count 
    return words_table_data

#Compute lograthmic term frequency
def log_tf(tf):
    if not tf:
        return 0.0
    return 1.0+math.log(tf,10)

#Compute augmented_tf term frequency
def augmented_tf(tf, max_tf):
    if not tf:  
        return 0.0
    else:
        x = 0.5+(0.5*float(tf/max_tf))
    return x

#Output Computed values of Term, Log and Augmented Term Frequency
def outputdataresult(words_table_data_sorted):
    #print 'max frequency'
    maxterm = ''
    maxterm = words_table_data_sorted[0]
    #print maxterm
    maxfrequency =  maxterm[1]
    #print maxfrequency
    for k,v in words_table_data_sorted:
        #print k,v
        d1_termfrequency[k].append(v)
        d1_logfrequency[k].append(log_tf(v))
        d1_augf[k].append(augmented_tf(v,maxfrequency))

#Specify the Input DataSet Folder
#ParseFolder('Dataset-1')
ParseFolder('Dataset-2')

d1 = dict((k, tuple(v)) for k, v in d1_termfrequency.iteritems())

d2 = dict((k, tuple(v)) for k, v in d1_logfrequency.iteritems())

d3 = dict((k, tuple(v)) for k, v in d1_augf.iteritems())

#Sum all Values for a particular key
d1_tf_sum = dict((k, sum(tuple(v))) for k, v in d1.iteritems())

#Sort by Value
d1_tf_sum_sorted = sorted(d1_tf_sum.items(), key=operator.itemgetter(1), reverse=True)

#Sum all Values for a particular key
d2_lf_sum = dict((k, sum(tuple(v))) for k, v in d2.iteritems())

#Sort by Value
d2_lf_sum_sorted = sorted(d2_lf_sum.items(), key=operator.itemgetter(1), reverse=True)

#Sum all Values for a particular key
d3_af_sum = dict((k, sum(tuple(v))) for k, v in d3.iteritems())

#Sort by Value
d3_af_sum_sorted = sorted(d3_af_sum.items(), key=operator.itemgetter(1), reverse=True)

print 'distinct words count'
print len(d1)

f = open('Task1c - TermFrequency_Top50.txt', 'w')
print 'tf'
for key, value in d1_tf_sum_sorted[:50]:
    print >>f, key, value
f.close()

print 'lf'
f = open('Task1c - LogFrequency_Top50.txt', 'w')
for key, value in d2_lf_sum_sorted[:50]:
    print >>f, key, value
f.close()

print 'augf'
f = open('Task1c - AugmentedFrequency_Top50.txt', 'w')
for key, value in d3_af_sum_sorted[:50]:
    print >>f, key, value
f.close()

noofwords = 0
f = open('Task1a - TermFrequency.txt', 'w')
print 'tf'
for key, value in d1_tf_sum_sorted:
    noofwords = noofwords  + value
    print >>f, key, value
f.close()

print 'lf'
f = open('Task1a - LogFrequency.txt', 'w')
for key, value in d2_lf_sum_sorted:
    print >>f, key, value
f.close()

print 'augf'
f = open('Task1a - AugmentedFrequency.txt', 'w')
for key, value in d3_af_sum_sorted:
    print >>f, key, value
f.close()

print 'total words count'
print noofwords

