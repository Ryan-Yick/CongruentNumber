import math

def isCongruent(n):
    #check if n is sqarefree
    if not isSquareFree(n):
        return "Input is not squarefree, please enter a squarefree number"
    if n%2 == 1:
        a = f_n(n)
        b = g_n(n)
        if a == 2*b:
            return "Inconclusive"
        else:
            return "Not Congruent"
    else:
        c = h_n(n)
        d = k_n(n)
        if c == 2*d:
            return "Inconclusive"
        else:
            return "Not Congruent"

def isSquareFree(n): #checks if all squares less than n can divide n
    for i in range(2, int(math.sqrt(n))+ 1):
        if (n % i**2) == 0:
            return False
    return True

def f_n(n): #finds the number of solutions to f(n)
    count = 0
    #check for x = 0
    for y in range(0, int(math.sqrt(n/2) + 1)):
        for z in range(0, int(math.sqrt(n/8) + 1)):
            if (2*y**2 + 8*z**2 == n):
                count = count + 4  #4 different combinations of +-
                #solutions with 0 have less permutations
                if y == 0:
                    count = count - 2
                    if z == 0:
                        count = count - 2
                elif z == 0:
                    count = count - 2

    #check for all other x
    for x in range(1, int(math.sqrt(n) + 1), 2): #x has to be odd
        for y in range(0, int(math.sqrt(n/2) + 1)):
            for z in range(0, int(math.sqrt(n/8) + 1)):
                if (x**2 + 2*y**2 + 8*z**2 == n):
                    count = count + 8  #8 different combinations of +-
                    #solutions with 0 have less permutations
                    if y == 0:
                        count = count - 4
                        if z == 0:
                            count = count - 2
                    elif z == 0:
                        count = count - 4
    return count

def g_n(n):
    count = 0
    zeroCount = 0
    #check for x = 0
    for y in range(0, int(math.sqrt(n/2) + 1)):
        for z in range(0, int(math.sqrt(n/32) + 1)):
            if (2*y**2 + 32*z**2 == n):
                count = count + 4  #4 different combinations of +-
                #solutions with 0 have less permutations
                if y == 0:
                    count = count - 2
                    if z == 0:
                        count = count - 2
                elif z == 0:
                    count = count - 2

    #check for all other x
    for x in range(1, int(math.sqrt(n) + 1), 2): #x has to be odd
        for y in range(0, int(math.sqrt(n/2) + 1)):
            for z in range(0, int(math.sqrt(n/32) + 1)):
                if (x**2 + 2*y**2 + 32*z**2 == n):
                    count = count + 8  #8 different combinations of +-
                    #solutions with 0 have less permutations
                    if y == 0:
                        count = count - 4
                        if z == 0:
                            count = count - 2
                    elif z == 0:
                        count = count - 4
    return count

#n is odd
def h_n(n):
    count = 0
    #check for x = 0
    for y in range(0, int(math.sqrt(n/8) + 1)):
        for z in range(0, int(math.sqrt(n/16) + 1)):
            if (4*y**2 + 8*z**2 == n/2):
                count = count + 4  #4 different combinations of +-
                #solutions with 0 have less permutations
                if y == 0:
                    count = count - 2
                    if z == 0:
                        count = count - 2
                elif z == 0:
                    count = count - 2

    #check for all other x
    for x in range(1, int(math.sqrt(n/2) + 1), 2): #x has to be odd
        for y in range(0, int(math.sqrt(n/8) + 1)):
            for z in range(0, int(math.sqrt(n/16) + 1)):
                if (x**2 + 4*y**2 + 8*z**2 == n/2):
                    count = count + 8  #8 different combinations of +-
                    #solutions with 0 have less permutations
                    if y == 0:
                        count = count - 4
                        if z == 0:
                            count = count - 2
                    elif z == 0:
                        count = count - 4
    return count

def k_n(n):
    count = 0
    #check for x = 0
    for y in range(0, int(math.sqrt(n/8) + 1)):
        for z in range(0, int(math.sqrt(n/64) + 1)):
            if (4*y**2 + 32*z**2 == n/2):
                count = count + 4  #4 different combinations of +-
                #solutions with 0 have less permutations
                if y == 0:
                    count = count - 2
                    if z == 0:
                        count = count - 2
                elif z == 0:
                    count = count - 2

    #check for all other x
    for x in range(1, int(math.sqrt(n/2) + 1), 2): #x has to be odd
        for y in range(0, int(math.sqrt(n/8) + 1)):
            for z in range(0, int(math.sqrt(n/64) + 1)):
                if (x**2 + 4*y**2 + 32*z**2 == n/2):
                    count = count + 8  #8 different combinations of +-
                    #solutions with 0 have less permutations
                    if y == 0:
                        count = count - 4
                        if z == 0:
                            count = count - 2
                    elif z == 0:
                        count = count - 4
    return count

def checkCongruentNumbers():
    congruentNumbers = [5, 6, 7, 13, 14, 15, 20, 21, 22, 23, 24, 28, 29, 30, 31, 34, 37, 38, \
                        39, 41, 45, 46, 47, 52, 53, 54, 55, 56, 60, 61, 62, 63, 65, 69, 70, \
                        71, 77, 78, 79, 80, 84, 85, 86, 87, 88, 92, 93, 94, 95, 96, 101, 102,\
                        103, 109, 110, 111, 112, 116, 117, 118, 119, 120, 124, 125, 126]
    nonSquareFree = []
    for n in range(1, 126):
        if isCongruent(n) == "Inconclusive":
            if n not in congruentNumbers:
                nonSquareFree.append(n)
    return nonSquareFree

'''def f(n):
    count = 0
    for x in range(-n, n):
        for y in range(-n, n):
            for z in range(-n, n):
                if x**2 + 2*y**2 + 8*z**2 == n:
                    print(str(x) + str(y) + str(z))
                    count = count + 1
    return count

def g(n):
    count = 0
    for x in range(-n, n):
        for y in range(-n, n):
            for z in range(-n, n):
                if x**2 + 2*y**2 + 32*z**2 == n:
                    print(str(x) + str(y) + str(z))
                    count = count + 1
    return count

def h(n):
    count = 0
    for x in range(-n, n):
        for y in range(-n, n):
            for z in range(-n, n):
                if x**2 + 4*y**2 + 8*z**2 == n/2:
                    count = count + 1
    return count

def k(n):
    count = 0
    for x in range(-n, n):
        for y in range(-n, n):
            for z in range(-n, n):
                if x**2 + 4*y**2 + 32*z**2 == n/2:
                    count = count + 1
    return count

def fTest(n):
    count = 0
    for x in range(-int(math.sqrt(n) - 1), int(math.sqrt(n) + 1)):
        for y in range(-int(math.sqrt(n/2) - 1), int(math.sqrt(n/2) + 1)):
            for z in range(-int(math.sqrt(n/8) - 1), int(math.sqrt(n/8) + 1)):
                if (x**2 + 2*(y**2) + 8*(z**2) == n):
                    count = count + 1
    return count

def gTest(n):
    count = 0
    for x in range(-int(math.sqrt(n) - 1), int(math.sqrt(n) + 1)):
        for y in range(-int(math.sqrt(n/2) - 1), int(math.sqrt(n/2) + 1)):
            for z in range(-int(math.sqrt(n/32) - 1), int(math.sqrt(n/32) + 1)):
                if (x**2 + 2*(y**2) + 32*(z**2) == n):
                    count = count + 1
    return count'''
