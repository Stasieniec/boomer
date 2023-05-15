# Import the json module
import json


with open("data.json", "r") as f:
  words = json.load(f)

print(type(words))
print(len(words))


for word, info in words.items():
  print(word, info)

def is_in_dataset(searched_word: str):
  if searched_word in words:
    return True
  else:
    return False
