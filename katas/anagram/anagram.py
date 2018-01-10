import requests
anagrams = []
words = requests.get("http://codekata.com/data/wordlist.txt").text.split()
for word in words:
  if len(anagrams) is 0:
    anagrams.append([word])
  else:
    found = False
    for i, sets in enumerate(anagrams):
      if ''.join(sorted(word)) == ''.join(sorted(sets[0])):
        anagrams[i].append(word)
        found = True
        break

    if found is False:
      anagrams.append([word])

print len(anagrams)