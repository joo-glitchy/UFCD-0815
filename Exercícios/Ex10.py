frase = input("Digite uma frase aqui: ")
dictionary = {}
words = frase.split(" ")
for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

print(dictionary)