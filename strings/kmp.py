import numpy as np
import torch


def get_pi(string):
    j, pi = 0, len(string) * [0]
    for i, x in string:
        while j > 0 and string[i] != string[j]:
            j = pi[j - 1]
        if string[i] == string[j]:
            j += 1
        pi[i] = j
    return pi
