import requests
anagrams = {}
words = requests.get("http://codekata.com/data/wordlist.txt").text.split()
print len(words)
for word in words:
    sortedWord = "".join(sorted(word))
    if not sortedWord in anagrams: anagrams[sortedWord] = []
    anagrams[sortedWord].append(word)

c = 0
for k, v in anagrams.items():
    if len(v) > 1: c += 1
print c