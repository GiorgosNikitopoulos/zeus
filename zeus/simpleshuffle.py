import random
import gmpy2
from datetime import datetime
from random import randint

class SimpleShuffle(object):
    def __init__(self, modulus, k):
        self.p0Y = [None] * k
        self.p0X = [None] * k
        self.p2Theta = [None] * (2 * k)
        self.p4Zalpha = [None] * (2 * k - 1)
        self.v1Zt = 0
        self.v3Zc = 0
        self.modulus = modulus
        self.k = k

    def Prove(self, modulus, order, G, gamma, x, y):
        """Prove function in Section 3 of Neff's paper"""
        k = self.k

        if k <= 1:
            raise Exception("Can't Shuffle length 1 vector")
        if k != len(y):
            raise Exception("Mismatched vector lengths")

        # Step 0: xi = logG(Xi), Xi = G^xi, same for yi.
        # Basically creates Yi and Xi
        for i in range(k):
            self.p0X[i] = pow(G, x[i], modulus)
            self.p0Y[i] = pow(G, y[i], modulus)

        # Verifier Step 1: create t in Zq
        self.v1Zt = randint(0, order - 1)
        t = self.v1Zt

        # Prover step 2
        gamma_t = (gamma * t) % order
        x_hat = [None] * k
        y_hat = [None] * k

        for i in range(k):
            x_hat[i] = (x[i] - t) % order
            y_hat[i] = (y[i] - gamma_t) % order

        #(7) theta and Theta vectors
        thlen = (2 * k) - 1
        theta = [None] * thlen
        Theta = [None] * (thlen + 1)
        for i in range((2 * k) - 1):
            theta[i] = randint(0, order - 1)
        Theta[0] = thenc(modulus, order, G, None, None, theta[0], y_hat[0])
        for i in range(1, k):
            Theta[i] = thenc(modulus, order, G, theta[i - 1],
                             x_hat[i], theta[i], y_hat[i])
        for i in range(k, thlen):
            Theta[i] = thenc(modulus, order, G, theta[i - 1],
                             gamma, theta[i], None)
        Theta[thlen] = thenc(
            modulus, order, G, theta[thlen - 1], gamma, None, None)
        self.p2Theta = Theta

        # Verifier Step 3
        self.v3Zc = randint(0, order - 1)
        c = self.v3Zc

        # Prover step 4
        alpha = [None] * thlen
        runprod = c
        # (8)
        for i in range(k):
            # The one multiplication Neff was reffering to
            runprod = (runprod * x_hat[i]) % order
            # The one division Neff was referring to
            runprod = (runprod * gmpy2.invert(y_hat[i], order)) % order
            alpha[i] = (theta[i] + runprod) % order
        gammainverse = gmpy2.invert(gamma, order)
        rungamma = c
        # That is the second part of (8)
        for i in range(1, k):
            rungamma = (rungamma * gammainverse) % order
            alpha[thlen - i] = (theta[thlen - i] + rungamma) % order

        # Verifier step 5
        self.p4Zalpha = alpha

        return 1

    def Verify(self, modulus, order, G, Gamma):
        """Verifier for Neff's SimpleShuffle"""
        X = self.p0X
        Y = self.p0Y
        Theta = self.p2Theta
        alpha = self.p4Zalpha
        # Validate vector lens
        k = len(Y)
        thlen = (2 * k) - 1
        if k <= 1 or len(Y) != k or len(Theta) != thlen + 1 or len(alpha) != thlen:
            raise Exception('Something went wrong')
            return 0
        # TODO: Check for null stuff
        t = self.v1Zt
        c = self.v3Zc

        # Verifier step 5
        negt = (-t) % order  ##Fix modulus
        U = pow(G, negt, modulus)
        W = pow(Gamma, negt, modulus)
        X_hat = [None] * k
        Y_hat = [None] * k
        for i in range(k):
            X_hat[i] = (X[i] * U) % modulus
            Y_hat[i] = (Y[i] * W) % modulus
        P = 0
        Q = 0
        s = 0
        b_good = True
        b_good = b_good and thver(
            X_hat[0], Y_hat[0], Theta[0], P, Q, c, alpha[0], modulus, order)
        for i in range(1, k):
            b_good = b_good and thver(X_hat[i], Y_hat[i], Theta[i], P, Q, alpha[i - 1], alpha[i], modulus, order)
        for i in range(k, thlen):
            b_good = b_good and thver(
                Gamma, G, Theta[i], P, Q, alpha[i - 1], alpha[i], modulus, order)
        b_good = b_good and thver(
            Gamma, G, Theta[thlen], P, Q, alpha[thlen - 1], c, modulus, order)
        if not b_good:
            raise Exception('Incorrect poof')
            return 0
        return 1


def thenc(modulus, order, G, a, b, c, d):
    """Helper function in order to compute G^(ab-cd)"""
    ab = 0
    cd = 0
    if a == None or a == 0:
        ab = 0
    else:
        ab = (a * b) % order
    if c == None or c == 0:
        cd = 0
    else:
        if d == None or d == 0:
            cd = c
        else:
            cd = (c * d) % order
    return pow(G, (ab - cd) % order, modulus)

def thver(A, B, T, P, Q, a, b, modulus, order):
    """Helper function in order to verify Theta elements"""
    P = pow(A, a, modulus)
    Q = pow(B, ((-b) % order), modulus)
    P = (P * Q) % modulus
    if P == T:
        return True
    else:
        return False
