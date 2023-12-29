text = open("lorem_ipsum.txt")
text = text.read()

wordcount = dict()
nonalpha = [".", ",","-", "(", ")", "\"", ":"] #Make a list of special characters likely to show up in written text.

for specchar in nonalpha:
    text = text.replace(specchar, "")

words = text.split()

#for line in text:
#    words = line.split() #Problem with split: Does not account for special characters, needs to be adjusted as Lorem and Lorem, are different words.

for word in words:
    wordcount[word] = wordcount.get(word, 0) +1

# Try to use a more elegant, sorted tuple, comment out old solution
#largest_count = None
#largest_word = None

#for word, number in wordcount.items():
#    if largest_count is None or number > largest_count:
#        largest_count = number
#        largest_word = word
#print(largest_word, largest_count)

# In words: Print a sorted list of variables and keys from the Dictionary, cutting off at index position 10.
print(sorted([(v, k) for (k, v) in wordcount.items()], reverse=True)[:10])


