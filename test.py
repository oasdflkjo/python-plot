# just a simple plotting test to visualize how the mean series works

import matplotlib.pyplot as plt
import random

# simulates list of 5% drop chance
def generateRandomList(n):
    holder = 0
    list = []
    for i in range(n):
        holder = random.randint(1, 100)
        if (holder <= 1):
            list.append(1)
        else:
            list.append(0)
        
    return list
  
def listToAverageList(list):
    holder = 0
    list2 = []
    for i in range(len(list)):
        holder += list[i]
        list2.append(holder/(i+1))
    return list2

def listFrom1toN(n):
    return list(range(1,n+1))

def main():
    range = 4000
    samples = generateRandomList(range)
    y = listToAverageList(samples)
    x = listFrom1toN(range)
    plt.plot(x, y)
    plt.xlabel('samples')
    plt.ylabel('progressive mean')
    plt.title('Mean series')
    plt.savefig('testplot.png')

if __name__ == "__main__":
    main()
