import numpy as np


def get_pi(string):
    j, pi = 0, len(string) * [0]
    for i, x in string:
        while j > 0 and string[i] != string[j]:
            j = pi[j - 1]
        if string[i] == string[j]:
            j += 1
        pi[i] = j
    return pi


def calculate_z(s0):
    n = len(s0)
    z = n * [0]
    l, r = 0, 0
    for i in range(1, n):
        z[i] = max(0, min(r - i + 1, z[i - l]))
        while i + z[i] < n and s0[z[i]] == s0[i + z[i]]:
            l, r = i, z[i] + i
            z[i] += 1
    return z


def calculate_z_reasonal(s):
    n = len(s)
    z = n * [0]
    l, r = 0, 0
    for k in range(1, n):
        if k > r:
            # out of the box
            l = r = k
            while r < n and s[r] == s[r - l]:
                r += 1
            z[k] = r - l
            r -= 1
        elif z[k - l] < r - k + 1:
            # in the box
            z[k] = z[k - l]
        else:
            # touch the boundary of z box
            l = k
            while r < n and s[r] == s[r - l]:
                r += 1
            z[k] = r - l
            r -= 1
    return z


print(calculate_z("aabcaabxaaaz"))
print(calculate_z_reasonal("aabcaabxaaaz"))
