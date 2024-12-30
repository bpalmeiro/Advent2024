import numpy as np




if  __name__ == "__main__":
    lists = np.loadtxt("data/Day1.txt")
    list1 = np.sort(lists[:, 0])
    list2 = np.sort(lists[:, 1])
    diff  = np.abs(list2 - list1)
    print(f'La parte 1: {int(sum(diff))}')

    score = 0
    for li in list1:
        score += li * np.sum(list2 == li)
    print(f'La parte 2: {int(score)}')
