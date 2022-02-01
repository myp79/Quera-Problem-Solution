import os

current_dir = os.getcwd()


def makeinput(num):
    full_path = os.path.join(current_dir, 'in')
    os.mkdir(full_path)
    os.chdir('in')
    for i in range(1, num+1):
        with open('input%d.txt' % (i), 'w') as f:
            pass
        f.close()


def makeoutput(num):

    full_path = os.path.join(current_dir, 'out')
    os.mkdir(full_path)
    os.chdir(full_path)
    for i in range(1, num+1):
        with open('output%d.txt' % (i), 'w') as f:
            pass
        f.close()


if __name__ == '__main__':
    num = int(input('How many test case do you need? \n'))
    makeinput(num)
    makeoutput(num)

# Mohammad YousefiPour - Github.com/myp79
