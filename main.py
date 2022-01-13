import random
import numpy as np

def plustri(c):
   return(c+3)


if __name__ == '__main__':
 hrac=np.array([2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14])
 print(type(hrac))
 random.shuffle(hrac)
 print(hrac)
 hrac1 = hrac[:int(len(hrac)/2)]
 hrac2 = hrac[int(len(hrac)/2):]
 print(f"hrac1={hrac1}")
 print(f"hrac2={hrac2}")
 a=0
 b=0
 hrac1a = []
 hrac2a = []
 while 1:
         if len(hrac1) == 0:
             if len(hrac1a) == 0:
                 print(f"hrac2 vyhral")
                 break
             hrac1 = hrac1a
             print(f"nove karty, hrac1={hrac1}")
             hrac1a=[]
         if len(hrac2) == 0:
             if len(hrac2a) == 0:
                 print(f"hrac1 vyhral")
                 break
             hrac2 = hrac2a
             print(f"nove karty, hrac2={hrac2}")
             hrac2a=[]
         x = hrac1[0]
         y = hrac2[0]
         if x > y:
             hrac1a = np.append(hrac1a, hrac1[a])
             hrac1a = np.append(hrac1a, hrac2[b])
             hrac1 = np.delete(hrac1, 0)
             hrac2 = np.delete(hrac2, 0)
             print(f"hrac1a={hrac1a}")
             print(f"hrac1={hrac1}")
             print(f"hrac2={hrac2}")
         elif y > x:
             hrac2a = np.append(hrac2a, hrac1[a])
             hrac2a = np.append(hrac2a, hrac2[b])
             hrac1 = np.delete(hrac1, 0)
             hrac2 = np.delete(hrac2, 0)
             print(f"hrac2a={hrac2a}")
             print(f"hrac1={hrac1}")
             print(f"hrac2={hrac2}")
         else:
             print(f"valka")
             c = 0
             d = 1
             while 1:
                 if len(hrac1) == 3 + c:
                     if len(hrac1a) == 0:
                         c = c-1
                         print(f"doplneni karet, hrac1={hrac1}"
                               f"hrac1a={hrac1a}")
                     else:
                         hrac1 = np.append(hrac1, hrac1a[a])
                         hrac1a = np.delete(hrac1a, 0)
                         print(f"doplneni karet, hrac1={hrac1}"
                            f"hrac1a={hrac1a}")
                 if len(hrac1) == 2 + c:
                     if len(hrac1a) == 0:
                         c = c-2
                         print(f"doplneni karet, hrac1={hrac1}"
                               f"hrac1a={hrac1a}")
                     elif len(hrac1a) == 1:
                         c = c-1
                         hrac1 = np.append(hrac1, hrac1a[a])
                         hrac1a = np.delete(hrac1a, 0)
                         print(f"doplneni karet, hrac1={hrac1}"
                               f"hrac1a={hrac1a}")
                     else:
                         hrac1 = np.append(hrac1, hrac1a[a])
                         hrac1 = np.append(hrac1, hrac1a[a + 1])
                         hrac1a = np.delete(hrac1a, 0)
                         hrac1a = np.delete(hrac1a, 0)
                         print(f"doplneni karet, hrac1={hrac1}"
                               f"hrac1a={hrac1a}")
                 if len(hrac1) == 1 + c:
                     if len(hrac1a) == 0:
                         print(f"hrac2 vyhral")
                     elif len(hrac1a) == 1:
                         hrac1 = np.append(hrac1, hrac1a[a])
                         hrac1a = np.delete(hrac1a, 0)
                         c = c-2
                         print(f"doplneni karet, hrac1={hrac1}"
                               f"hrac1a={hrac1a}")
                     elif len(hrac1a) == 2:
                         hrac1 = np.append(hrac1, hrac1a[a])
                         hrac1 = np.append(hrac1, hrac1a[a + 1])
                         hrac1a = np.delete(hrac1a, 0)
                         hrac1a = np.delete(hrac1a, 0)
                         print(f"doplneni karet, hrac1={hrac1}"
                               f"hrac1a={hrac1a}")
                         c = c-1
                     else:
                         hrac1 = np.append(hrac1, hrac1a[a])
                         hrac1 = np.append(hrac1, hrac1a[a + 1])
                         hrac1 = np.append(hrac1, hrac1a[a + 2])
                         hrac1a = np.delete(hrac1a, 0)
                         hrac1a = np.delete(hrac1a, 0)
                         hrac1a = np.delete(hrac1a, 0)
                         print(f"doplneni karet, hrac1={hrac1}"
                               f"hrac1a={hrac1a}")
                 if len(hrac2) == 3 + c:
                     if len(hrac2a) == 0:
                         c = c - 1
                         print(f"doplneni karet, hrac2={hrac2}"
                               f"hrac2a={hrac2a}")
                     else:
                         hrac2 = np.append(hrac2, hrac2a[a])
                         hrac2a = np.delete(hrac2a, 0)
                         print(f"doplneni karet, hrac2={hrac2}"
                               f"hrac2a={hrac2a}")
                 if len(hrac2) == 2 + c:
                     if len(hrac2a) == 0:
                         c = c - 2
                         print(f"doplneni karet, hrac2={hrac2}"
                               f"hrac2a={hrac2a}")
                     elif len(hrac2a) == 1:
                         c = c - 1
                         hrac2 = np.append(hrac2, hrac2a[a])
                         hrac2a = np.delete(hrac2a, 0)
                         print(f"doplneni karet, hrac2={hrac2}"
                               f"hrac2a={hrac2a}")
                     else:
                         hrac2 = np.append(hrac2, hrac2a[a])
                         hrac2 = np.append(hrac2, hrac2a[a + 1])
                         hrac2a = np.delete(hrac2a, 0)
                         hrac2a = np.delete(hrac2a, 0)
                         print(f"doplneni karet, hrac2={hrac2}"
                               f"hrac2a={hrac2a}")
                 if len(hrac2) == 1 + c:
                     if len(hrac2a) == 0:
                         print(f"hrac1 vyhral")
                     elif len(hrac2a) == 1:
                         hrac2 = np.append(hrac2, hrac2a[a])
                         hrac2a = np.delete(hrac2a, 0)
                         c = c - 2
                         print(f"doplneni karet, hrac2={hrac2}"
                               f"hrac2a={hrac2a}")
                     elif len(hrac2a) == 2:
                         hrac2 = np.append(hrac2, hrac2a[a])
                         hrac2 = np.append(hrac2, hrac2a[a + 1])
                         hrac2a = np.delete(hrac2a, 0)
                         hrac2a = np.delete(hrac2a, 0)
                         print(f"doplneni karet, hrac2={hrac2}"
                               f"hrac2a={hrac2a}")
                         c = c-1
                     else:
                         hrac2 = np.append(hrac2, hrac2a[a])
                         hrac2 = np.append(hrac2, hrac2a[a + 1])
                         hrac2 = np.append(hrac2, hrac2a[a + 2])
                         hrac2a = np.delete(hrac2a, 0)
                         hrac2a = np.delete(hrac2a, 0)
                         hrac2a = np.delete(hrac2a, 0)
                         print(f"doplneni karet, hrac2={hrac2}"
                               f"hrac2a={hrac2a}")
                 c = plustri(c)
                 d = plustri(d)
                 if hrac1[c] > hrac2[c]:
                     hrac1a = np.append(hrac1a, hrac1[: d])
                     hrac1a = np.append(hrac1a, hrac2[: d])
                     hrac1 = hrac1[d :]
                     hrac2 = hrac2[d :]
                     print(f"hrac1a={hrac1a}")
                     print(f"hrac1={hrac1}")
                     print(f"hrac2={hrac2}")
                     break
                 elif hrac2[c] > hrac1[c]:
                     hrac2a = np.append(hrac2a, hrac1[: d])
                     hrac2a = np.append(hrac2a, hrac2[: d])
                     hrac1 = hrac1[d:]
                     hrac2 = hrac2[d:]
                     print(f"hrac2a={hrac2a}")
                     print(f"hrac1={hrac1}")
                     print(f"hrac2={hrac2}")
                     break

