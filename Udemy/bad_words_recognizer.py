# Develop an algorithm that hides bad words to *******
# If a bad word is recognized, it will replace with * times the lenght of that word

bad_words = []  #put tha bad words in this list

text = input('Type your message here: ').lower()

for word in bad_words:
    text = text.replace(word, len(word)*'*')

print('')
print(text)
