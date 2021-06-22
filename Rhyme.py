import requests

user = input('Enter a word: ')
parameter = {}
parameter['rel_rhy'] = user

request = requests.get('https://api.datamuse.com/words', parameter)

rhyme = request.json()

for i in rhyme[0:3]:
  print(i['word'])
