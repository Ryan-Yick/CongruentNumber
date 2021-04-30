import math

def isCongruent(n):
    if n%2 == 1:
        a = fTest(n)
        b = gTest(n)
        return a == 2*b
    else:
        c = h_n(n)
        d = k_n(n)
        return c == 2*d

"""def isSqrt(n):
    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
        return True
    return False"""

    
def f_n(n): #finds the number of solutions to f(n)
    count = 0
    #check for x = 0
    for y in range(-int(math.sqrt(n/2) - 1), int(math.sqrt(n/2) + 1)):
        for z in range(-int(math.sqrt(n/8) - 1), int(math.sqrt(n/8) + 1)):
            if (2*y**2 + 8*z**2 == n):
                count = count + 1
    #check for all other x
    for x in range(-n, int(math.sqrt(n) + 1), 2): #x has to be odd
        for y in range(-int(math.sqrt(n/2) - 1), int(math.sqrt(n/2) + 1)):
            for z in range(-int(math.sqrt(n/8) - 1), int(math.sqrt(n/8) + 1)):
                if (x**2 + 2*y**2 + 8*z**2 == n):
                    count = count + 1
    return count
def g_n(n):
    count = 0
    #check for x = 0
    for y in range(-int(math.sqrt(n/2) - 1), int(math.sqrt(n/2) + 1)):
        for z in range(-int(math.sqrt(n/32) - 1), int(math.sqrt(n/32) + 1)):
            if (2*y**2 + 32*z**2 == n):
                count = count + 1
    #check for all other x
    for x in range(-n, int(math.sqrt(n) + 1), 2): #x has to be odd
        for y in range(-int(math.sqrt(n/2) - 1), int(math.sqrt(n/2) + 1)):
            for z in range(-int(math.sqrt(n/32) - 1), int(math.sqrt(n/32) + 1)):
                if (x**2 + 2*y**2 + 32*z**2 == n):
                    count = count + 1
    return count

def h_n(n):
    count = 0
    for x in range(-int(math.sqrt(n/2) - 1), int(math.sqrt(n/2) + 1)):
        for y in range(-int(math.sqrt(n/8) - 1), int(math.sqrt(n/8) + 1)):
            for z in range(-int(math.sqrt(n/16) - 1), int(math.sqrt(n/16) + 1)):
                if (x**2 + 4*y**2 + 8*z**2 == n/2):
                    count = count + 1
    return count

def k_n(n):
    count = 0
    for x in range(-int(math.sqrt(n/2) - 1), int(math.sqrt(n/2) + 1)):
        for y in range(-int(math.sqrt(n/8) - 1), int(math.sqrt(n/8) + 1)):
            for z in range(-int(math.sqrt(n/64) - 1), int(math.sqrt(n/64) + 1)):
                if (x**2 + 4*y**2 + 32*z**2 == n/2):
                    count = count + 1
    return count

def checkCongruentNumbers():
    congruentNumbers = [5, 6, 7, 13, 14, 15, 20, 21, 22, 23, 24, 28, 29, 30, 31, 34, 37, 38, \
                        39, 41, 45, 46, 47, 52, 53, 54, 55, 56, 60, 61, 62, 63, 65, 69, 70, \
                        71, 77, 78, 79, 80, 84, 85, 86, 87, 88, 92, 93, 94, 95, 96, 101, 102,\
                        103, 109, 110, 111, 112, 116, 117, 118, 119, 120, 124, 125, 126]
    nonSquareFree = []
    for n in range(0, 126):
        if isCongruent(n):
            if n not in congruentNumbers:
                nonSquareFree.append(n)
    return nonSquareFree

def f(n):
    count = 0
    for x in range(-n, n):
        for y in range(-n, n):
            for z in range(-n, n):
                if x**2 + 2*y**2 + 8*z**2 == n:
                    count = count + 1
    return count

def g(n):
    count = 0
    for x in range(-n, n):
        for y in range(-n, n):
            for z in range(-n, n):
                if x**2 + 2*y**2 + 32*z**2 == n:
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
    return count
