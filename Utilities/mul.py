
import math
import numpy as np


def size_base10(x):
    count = 0
    while(x != 0):
        x /= 10
        count += 1
    return count

def karatsuba(x, y):
    if(x < 10 or y < 10):
        return x * y

    m = min(len(str(x)), len(str(y)))
    m2 = m // 2

    x_h = x // (10**m2) 
    x_l = x % (10**m2)
    y_h = y // (10**m2) 
    y_l = y % (10**m2)
    
    z0 = karatsuba(x_l, y_l)
    z2 = karatsuba(x_h, y_h)
    z1 = karatsuba(x_l - x_h, y_h - y_l) + z2 + z0 
    
    return (z2 * 10 ** (2 * m2)) + (z1 * 10 ** m2) + z0

def toomCook(m, n):
    b = 16384 #large multiple of 2
    i = max(int(math.log(b, m))//3, int(math.log(b, n)) // 3)
    B = b ** i
    
    m2 = m // B
    m1 = m % B // B
    m0 = m % B
    
    n2 = n // B
    n1 = n % B // B
    n0 = n % B
    # points = [0, 1, -1, -2, np.inf]
    p = m0 + m2
    q = n0 + n2
    p2 = p - m1
    q2 = q - n1
    pM = [m0, p + m1, p2, (p2 + m2)*2 - m0, m2]
    qN = [n0, q + n1, q2, (q2 + n2)*2 - n0, n2]
    PM = [pM[0]*qN[0], pM[1]*qN[1], pM[2]*qN[2], pM[3]*qN[3], pM[4]*qN[4]]
    
    r0 = PM[0]
    r4 = PM[4]
    r3 = (PM[3] - PM[1]) / 3
    r1 = (PM[1] - PM[2])/2
    r2 = PM[2] - PM[0]
    r3 = (r2 - r3)/2 + 2 * r4
    r2 = r2 + r1 - r4
    r1 = r1 - r3

    R = [r4, r3, r2, r1, r0]
    res = R[0]
    for x in range(len(R)):
        res = res*B + R[x]
    return  int(res / 2)

print(toomCook(12_3456_7890_1234_5678_9012, 9_8765_4321_9876_5432_1098))
print(toomCook(12345, 6789))
print(karatsuba(12345, 6789))




