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

    def Prove(self, modulus, order, G, gamma, x, y):
        """Prove function in Section 3 of Neff's paper"""
        k = self.k

        if k <= 1:
            print "Can't Shuffle length 1 vector"
            ##TODO: Handle error
        if k != len(y):
            print "Mismatched vector lengths"
            ##TODO: Handle error

        ##Step 0: xi = logG(Xi), Xi = G^xi, same for yi.
        ##Basically creates Yi and Xi
        for i in range(k):
            self.p0X = pow(G, x[i], modulus)
            self.p0Y = pow(G, y[i], modulus)

        ##Verifier Step 1: create t in Zq
        self.v1Zt = get_random_int(0, order)
        t = self.v1Zt

        ##Prover step 2
        gamma_t = (gamma * t) % modulus
        x_hat = list([None]) * k
        y_hat = list([None]) * k

        for i in range(k):
            x_hat[i] = (x[i] - t) % modulus
            y_hat[i] = (y[i] - gamma_t) % modulus

        #(7) theta and Theta vectors
        thlen = (2 * k) - 1
        theta = list([None]) * thlen
        Theta = list([None]) * (thlen + 1)
        for i in range(2k - 1):
            theta = get_random_int(0, order)
        Theta[0] = thenc(modulus, order, G, None, None, theta[0], y_hat[0])
        for i in range(1, k,):
            Theta[i] = thenc(modulus, order, G, theta[i-1], x_hat[i], theta[i], y_hat[i])
        for i in range(k, thlen):
            Theta[i] = thenc(modulus, order, G, theta[i-1], gamma, theta[i], None)
        Theta[thlen] = thenc(modulus, order, G, theta[thlen-1], gamma, None, None)
        self.p2Theta = Theta

        ##Verifier Step 3
        self.v3Zc = get_random_int(0, k)
        c = self.v3Zc

        ##Prover step 4
        alpha = list([None]) * thlen
        runprod = c
        ##(8)
        for i in range(k):
            runprod = (runprod * x_hat[i]) % modulus
            runprod = (runprod * gmpy2.invert(y_hat[i], modulus)) % modulus
            alpha[i] = (theta[i] + runprod) % modulus
        gammainverse = gmpy2.invert(gamma, modulus)
        rungamma = c
        ##That is the second part of (8)
        for i in range(1, k):
            rungamma = (rungamma * gammainverse) % modulus
            alpha[thlen-i] = (theta[thlen - i] + rungamma) % modulus

        ##Verifier step 5
        self.p4Zalpha = alpha

        return None

    def Verify(self, modulus, order, G, Gamma):
            

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
    return pow(G, (ab - cd) % modulus, modulus)

def thver(A, B, T, P, Q, a, b, s):
    """Helper function in order to verify Theta elements"""
    ##TODO: Not implemented
