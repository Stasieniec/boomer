# Import the json module
import json


with open("data.json", "r") as f:
  words = json.load(f)

print(type(words))
print(len(words))


for word, info in words.items():
  print(word, info)
