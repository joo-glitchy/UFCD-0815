palavra = input("Intoduza uma palavra: ")
dictionary = {}

for letter in palavra:
    if letter in dictionary:
        dictionary[letter] += 1
    else:
        dictionary[letter] = 1

print(dictionary)