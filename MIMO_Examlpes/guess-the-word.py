master = "tnetennba"
word = list(master)
length = len(word)
right = list("_" * length)
guess = input("Guess the letter! ")
for letter in word:
    if letter == guess:
print(right)
