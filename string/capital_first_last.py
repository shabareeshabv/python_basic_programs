'''string="hello world"
string1=string.split()
print(string)
print("using upper")
print(string[0].upper()+string[1:-1]+(string[-1].upper()))
print("using capitalize")
print(string[0].capitalize()+string[1:-1]+(string[-1].capitalize()))

'''


###chatgpt code
input_string = "hello world"
words = input_string.split()  # Split the input string into words
result_words = []

for word in words:
    if len(word) > 1:
        # Capitalize the first character and add the rest of the word (excluding the last character)
        modified_word = word[0].capitalize() + word[1:-1] + word[-1].capitalize()
        print(modified_word)
      
    else:
        # If the word has only one character, capitalize it
        modified_word = word.capitalize()
   
    result_words.append(modified_word)

result_string = ' '.join(result_words)
print(result_string)