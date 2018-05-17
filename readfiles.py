import re

import collections

text = open('1155-0.txt').read().lower()
print(type(text))
words = re.findall("\w+", text)
# \w+ means not white space, + includes one or more 
# print(type(words))
# print(words[0:11])

long_words = []
for word in words: 
    if len(word) >= 5: 
        long_words. append(word)
# This prints the most common words longer than 5 letters and gives their count. 

most_common = collections.Counter(long_words).most_common(10)

# This pulls out the most common words using the counter 

print(most_common)



