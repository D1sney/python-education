import random
def steps():
    x = random.randint(1,10)
    if x in [1,2]:
        return random.randint(1,5000)
    elif x in [3,4,5,6,7,8]:
        return random.randint(5001,15000)
    elif x in [9,10]:
        return random.randint(15001,25000)

if __name__ == '__main__':
    print(steps())