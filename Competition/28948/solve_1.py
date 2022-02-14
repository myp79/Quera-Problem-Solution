txt = input()
word = []
for letter in txt:
    if letter == '=' and len(word) > 0:
        word.pop()
    elif letter == '=' and len(word) == 0:
        continue
    else:
        word.append(letter)

print(''.join(word))
# Mohammad YousefiPour - Github.com/myp79
