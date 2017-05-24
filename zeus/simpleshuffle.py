import random
import gmpy2
from datetime import datetime
from core import get_random_int
from Crypto import random

class SimpleShuffle:
    def __init__(self, modulus, k):
        self.p0Y = list([None]) * k
        self.p0X = list([None]) * k
        self.p2Theta = list([None]) * k
        self.p4Zalpha = list([None]) * k
        self.v1Zt = 0;
        self.v3Zc = 0;
        self.modulus = modulus
        self.k = k

    def thenc(modulus, order, G, a, b, c, d):
        """Helper function in order to compute G^(ab-cd)"""
        ab = 0
        cd = 0
        if a != None or a != 0:
            ab = (a * b) % modulus
        else:
            ab = 0
        if c != None or c != 0:
            if d != None or d != 0:
                cd = (c * d) % modulus
            else:
                cd = c
        else:
            cd = 0
        return     
