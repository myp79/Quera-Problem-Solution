def game(number):
    digits = [number//10, number % 10]
    if digits[0] > digits[1]:
        return digits[0]-digits[1]
    else:
        return digits[1]-digits[0]


# Mohammad YousefiPour - Github.com/myp79
