# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
magic = 'abracadabra'
# a. Retrieve the 5th character.
print(magic[4])
# b. Retrieve the second to last character.
print(magic[9])
# c. Find the first occurrence of the letter 'c'.
print(magic[4])

# Advanced Slicing:
# Given the string 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[0:13:2])
# c. Reverse the entire string using slicing.
print(alphabet[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the 
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote.find('John F. Kennedy'))
personality_name = quote[83:]
print(personality_name)

# Manipulating Words:
# Given the string info 
quote2 = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
print(quote2.find('subjective'))
subjective = quote2[36:]
print(subjective)
# b. Extract every third word.
third_word = quote2.split()[::3]
print(third_word)
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
reversed = quote2.split()[::-1]
reversed = ''.join(reversed)
print(reversed)

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: 
quote3 = "MAY THE FORCE BE WITH YOU."
print(quote3.lower())

# String Joining and Splitting:
# Given the list 
motto = ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
single_string =''.join(motto)
print(single_string)
# b. Now, split the string at every occurrence of the letter 'a'.
split_motto =single_string.split('a')
print(split_motto)

# Replacing Words:
# Modify the sentence: 
sentence =  "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
new_sentence = sentence.replace("busy","distracted")
print(new_sentence)
# b. Replace "plans" with "mistakes".
new_sentence2= sentence.replace("plans","mistakes")
print(new_sentence2)

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
word_one = "Interation"
result = word_one * 7 
print(result)

# Word Search:
# Check if the word "moonlight" appears in the quote: 
quote4 = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
if "moonlight" in quote4:
  print("The word 'moonlight' appears in the quote.")
else:
  print("The word 'moonlight' does not appear in the quote.")

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".

# b. Count the number of times the letter 'i' appears in the same word/phrase.
