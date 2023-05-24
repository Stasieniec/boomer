import json
import openai
import config

openai.api_key = config.key


with open("data.json", "r") as f:
  words = json.load(f)

def add_saved_word(word): 
  with open("saved_words.txt", "r+") as f:
    lines = f.readlines()
    if word not in lines:
      f.write('\n' + word)

def get_saved_words(): 
  with open("saved_words.txt", "r") as f:
    saved_words = []
    for line in f:
      saved_words.append(line.strip())
  return saved_words


def is_in_dataset(searched_word: str):
  if searched_word in words:
    return True
  else:
    return False

def search_by_word(searched_word: str):
  result = words[searched_word]
  return result # It is a list of lists

def search_by_age(start_age, end_age):
  list_of_results = []
  
  for word in words:
    ages = words[word][3]
    is_in = False
    for age in ages:
      if age >= start_age and age <= end_age:
        is_in = True
      
    if is_in == True:
      single_result = words[word]
      single_result.insert(0, word)
      list_of_results.append(single_result)

  return list_of_results
  


