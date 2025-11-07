def manipulating1():
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