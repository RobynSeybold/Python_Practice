text = open("lorem_ipsum.txt")

wordcount = dict()
for line in text:
    words = line.split()
    for word in words:
        wordcount[word] = wordcount.get(word, 0) +1

largest_count = None
largest_word = None

for word, number in wordcount.items():
    if largest_count is None or number > largest_count:
        largest_count = number
        largest_word = word

print(largest_word, largest_count)