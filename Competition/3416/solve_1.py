def code(word):
    save = ''
    counter = 0
    for letter in word:
        if letter == save:
            counter += 1
        else:
            if counter > 1:
                print(save, counter, sep='', end='')
            else:
                print(save, end='')
            save = letter
            counter = 1
    if counter > 1:
        print(save, counter, sep='', end='')
    else:
        print(save, end='')


def decode(word):
    save = ''
    num = []
    for letter in word:
        if not letter in '0123456789':
            counter = ''.join(num)
            if counter != '':
                print(save*int(counter), end='')
            else:
                print(save, end='')
            save = letter
            num = []
        else:
            num.append(letter)
    counter = ''.join(num)
    if counter != '':
        print(save*int(counter), end='')
    else:
        print(save, end='')


n = int(input())
for i in range(n):
    x = int(input())
    word = input()
    if x == 1:
        code(word)
        print()
    else:
        decode(word)
        print()

# Mohammad YousefiPour - Github.com/myp79
