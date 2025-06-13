import os
import random
import re

words = set()
for name in os.listdir("Data"):
    with open("Data/" + name, "r") as file:
        text = re.sub(r'[.,!?\]["\'\-;:\t\n]', " ", file.read())
        for word in text.split(" "):
            words.add(word.strip().lower())

words = list(words)

random.shuffle(words)

print(f"Kelime sayısı: { len(words) }")

for x in words:
    if x and (x[0] == "a" and x[-1] == "e"):
        print(x, end=" ")
