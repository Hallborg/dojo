import requests
words = requests.get("http://codekata.com/data/wordlist.txt").text.split()
