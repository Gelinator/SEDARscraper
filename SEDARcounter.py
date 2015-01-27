import urllib
import re

counts = dict()
fhand = urllib.urlopen('http://www.sec.gov/Archives/edgar/data/51143/000104746914001302/0001047469-14-001302.txt')
for line in fhand:
    words = line.split()    
    for word in words:
        if word.startswith('<'):
            pass
        else:
            counts[word] = counts.get(word,0) + 1   
print counts
