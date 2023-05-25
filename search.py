import json
import openai
import config
import re

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

  if is_in_dataset(searched_word):
    #this word is in dataset
    return words[searched_word]
  else:
    #AI generation
    result = []
    ai_definition = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Give a short definition of the word. If the definition is longer than 7 words, add new line symbols so that it would fit on a smartphone screen \"{searched_word}\"",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    ai_similar_words = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Give 5 examples of words similar to \"{searched_word}\", separated by spaces.",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    ai_subcultures = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Give a short list of youth subcultures of people, who might use the following word, separated by spaces. If a subculture has a space in it's name, make it a dash: \"{searched_word}\"",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    ai_ages = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Give a list of numbers indicating ages of young people who might use the following word, separated by spaces: \"{searched_word}\"",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    ai_category = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Classify the following word into a category (word, topic, activity, person): \"{searched_word}\"",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    definition = ai_definition['choices'][0]['text']
    similar_words = ai_similar_words['choices'][0]['text'].split()
    subcultures = ai_subcultures['choices'][0]['text'].split()
    ages_clean = re.sub("[a-zA-Z,]", "", ai_ages['choices'][0]['text'])
    ages = list(map(int, ages_clean.split()))
    category = ai_category['choices'][0]['text']
    new_word = {searched_word:[
                definition,
                similar_words,
                subcultures,
                ages,
                category]
                }

    with open("data.json", "r") as f:
      # Load the existing data into a dictionary using json.load function
      existing_data = json.load(f)
      # Close the file
      f.close()
      existing_data.update(new_word)

    with open("data.json", "w") as f:
      json.dump(existing_data, f)
      f.close()

    return new_word[searched_word]
  

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