#This is a utility to count the occurences of characters in file. It helps to see what characters are present in list of sequences. 
#Usage: python charCount.py  (Update the file name in file_input)
import collections
import pprint
file_input = './scripts/charcount.txt'
with open(file_input, 'r') as info:
  count = collections.Counter(info.read())
  value = pprint.pformat(count)
print(value)