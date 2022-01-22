import random
import numpy as np


if __name__ == '__main__':
 hrac = np.array([2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14])
 print(type(hrac))
 random.shuffle(hrac)
 print(hrac)
 hrac1 = hrac[:int(len(hrac)/2)]
 hrac2 = hrac[int(len(hrac)/2):]
 print(f"hrac1={hrac1}")
 print(f"hrac2={hrac2}")
 a = 0
 b = 0
 while not(len(hrac1) == 0 or len(hrac2) == 0):
    if len(hrac1) == 0:
        print(f"hrac2 vyhral")
    if len(hrac2) == 0:
        print(f"hrac1 vyhral")
    x = hrac1[0]
    y = hrac2[0]
    if x > y:
        hrac1 = np.append(hrac1, hrac1[a])
        hrac1 = np.append(hrac1, hrac2[b])
        hrac1 = np.delete(hrac1, 0)
        hrac2 = np.delete(hrac2, 0)
        print(f"hrac1={hrac1}")
        print(f"hrac2={hrac2}")
    elif y > x:
        hrac2 = np.append(hrac2, hrac2[a])
        hrac2 = np.append(hrac2, hrac1[b])
        hrac1 = np.delete(hrac1, 0)
        hrac2 = np.delete(hrac2, 0)
        print(f"hrac1={hrac1}")
        print(f"hrac2={hrac2}")
    else:
        print(f"valka")
        c = 0
        d = 1
        while hrac1[a] == hrac2[b]:
                if len(hrac1) == 3 + c:
                    c = c-1
                if len(hrac1) == 2 + c:
                    c = c-2
                if len(hrac1) == 1 + c:
                    print(f"hrac1 malo karet, hrac2 vyhral")
                    hrac1 = []
                    break
                if len(hrac2) == 3 + c:
                    c = c - 1
                if len(hrac2) == 2 + c:
                    c = c - 2
                if len(hrac2) == 1 + c:
                    print(f"hrac2 malo karet, hrac1 vyhral")
                    hrac2 = []
                    break
                c += 3
                d = c + 1
                if hrac1[c] > hrac2[c]:
                    hrac1 = np.append(hrac1, hrac1[: d])
                    hrac1 = np.append(hrac1, hrac2[: d])
                    hrac1 = hrac1[d:]
                    hrac2 = hrac2[d:]
                    print(f"hrac1={hrac1}")
                    print(f"hrac2={hrac2}")
                    break
                elif hrac2[c] > hrac1[c]:
                    hrac2 = np.append(hrac2, hrac1[: d])
                    hrac2 = np.append(hrac2, hrac2[: d])
                    hrac1 = hrac1[d:]
                    hrac2 = hrac2[d:]
                    print(f"hrac1={hrac1}")
                    print(f"hrac2={hrac2}")
                    break
 if len(hrac1) == 0:
    print(f"hrac2 vyhral")
 if len(hrac2) == 0:
    print(f"hrac1 vyhral")
