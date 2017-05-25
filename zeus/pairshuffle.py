import random
import gmpy2
from datetime import datetime
from core import get_random_int
from Crypto import random


class PairShuffle:
    def __init__(self, modulus, k):
        self.modulus = modulus
        self.k = k
        self.p1Gamma = 0
        self.p1A = list([None]) * k
        self.p1C = list([None]) * k
        self.p1U = list([None]) * k
        self.p1W = list([None]) * k
        self.v2Zrho = list([None]) * k
        self.p3D = list([None]) * k
        self.p1Lamda1 = 0
        self.v4Zlamda = list([None]) * k
        self.p5Zsigma = list([None]) * k
        self.p5Ztau = 0
        self.pv6 = SimpleShuffle(modulus, k)

    # Alpha and beta are respectively X and Y
    def go_shuffle_prove(self, pi, modulus, generator, public, alpha, beta, neff_beta):
        if len(alpha) != len(pi) or len(alpha) != len(beta):
            print "Error happened"
        piinv = [None] * k
        for i in range(k):
            piinv[pi[i]] = i
        # STEP 1
        u = [None] * k
        w = [None] * k
        a = [None] * k

        # u w a random lists
        for i in range(k):
            u[i] = get_random_int(0, order)
        for i in range(k):
            w[i] = get_random_int(0, order)
        tau0 = get_random_int(0, order)
        for i in range(k):
            self.v2Zrho = get_random_int(0, order)

        nu = get_random_int(1, order)
        gamma = get_random_int(1, order)

        self.p1Gamma = pow(generator, gamma, modulus)
        wbetasum = tau0
        self.p1Lamda1 = 0
        self.p1Lamda2 = 0
        for i in range(k):
            self.p1A[i] = pow(generator, a[i], modulus)
            temporary_variable = (gamma * a[pi[i]]) % modulus
            self.p1C[i] = pow(generator, temporary_variable, modulus)
            self.U[i] = pow(generator, u[i], modulus)
            temporary_variable = (gamma * w[i]) % modulus
            self.W[i] = pow(generator, temporary_variable)
            temporary_variable = (w[i] * neff_beta[pi[i]]) % modulus
            wbetasum = (wbetasum + temporary_variable) % modulus
            temporary_variable = (w[piinv[i]] - u[i]) % modulus
            temporary_variable_2 = pow(alpha[i], temporary_variable, modulus)
            self.p1Lamda1 = (self.p1Lamda1 * temporary_variable_2) % modulus
            temporary_variable_2 = pow(beta[i], temporary_variable, modulus)
            self.p1Lamda2 = (self.p1Lamda2 * temporary_variable_2) % modulus
        g_to_the_wbetasum = pow(generator, wbetasum, modulus)
        h_to_the_wbetasum = pow(public, wbetasum, modulus)
        self.p1Lamda1 = (g_to_the_wbetasum * self.p1Lamda1) % modulus
        self.p1Lamda2 = (h_to_the_wbetasum * self.p1Lamda2) % modulus

        # STEP 2
        B[i] = list([None]) * k
        for i in range(k):
            P[i] = pow(generator, self.v2Zrho[i], modulus)
            temporary_variable = gmpy2.invert(self.p1U[i], modulus)
            B[i] = (P[i] * temporary_variable) % modulus
        b = list([None]) * k
        for i in range(k):
            b[i] = (self.v2Zrho - u[i]) % modulus

        d = list([None]) * k
        for i in range(k):
            d[i] = (gamma * b[pi[i]]) % modulus
            self.p3D[i] = pow(generator, d[i], modulus)

        # Generate random Lamda for fourth step
        self.v4Zlamda = get_random_int(0, order)

        r = list([None]) * k
        for i in range(k):
            temporary_variable = (self.v4Zlamda * b[i]) % modulus
            r[i] = (temporary_variable + a[i]) % modulus

        s = list([None]) * k
        for i in range(k):
            s[i] = (gamma * r[pi[i]]) % modulus

        self.p5Ztau = (-tau0) % modulus
        for i in range(k):
            self.p5Zsigma = (w[i] + b[pi[i]]) % modulus
            self.p5Ztau = (
                self.p5Ztau + ((b[pi[i]] * neff_beta[pi[i]]) % modulus)) % modulus
        # Make the dictionary for p5
        return self.pv6.Prove(modulus, order, generator, gamma, r, s)

    def go_shuffle_verify(self, modulus, generator, public, alpha, beta, alphabar, betabar):
        k = self.k
        if len(alpha) != k or len(beta) != k or len(alphabar) != k or len(betabar) == k:
            print 'Error'
            return None

        # TODO: Check for error there if p1 is null
        # TODO: Check for error there if v2 is null

        B = list([None]) * k
        for i in range(k):
            P = pow(g, self.v2Zrho, modulus)
        # TODO: Check for error there if p3 is null
        # TODO: Check for error there if v4 is null

        error_variable = self.pv6.Verify(
            modulus, order, generator, self.p1Gamma)
        if error_variable == 0:
            return 0

        Phi1 = 0
        Phi2 = 0
        P = 0
        Q = 0
        for i in range(k):

            # (31)
            Phi1 = (Phi1 * pow(alphabar[i],
                               self.p5Zsigma[i], modulus)) % modulus
            Phi1 = (Phi1 * gmpy2.invert(pow(alpha[i], self.v2Zrho, modulus)) % modulus
            # (32)
            Phi2 = (Phi2 * pow(alphabar[i],self.p5Zsigma[i], modulus)) % modulus
            Phi2 = (Phi2 * gmpy2.invert(pow(beta[i], self.v2Zrho, modulus)) % modulus
            if pow(self.p1Gamma, self.p5Zsigma, modulus) != (self.p1W[i] * self.p3D[i]) % modulus:
                print "Verification not successful"
                return 0

        if (self.p1Lamda1 * pow(generator, self.p5Ztau, modulus)) % modulus != Phi1:
            print "Verification not successful"
            return 0
        if (self.p1Lamda2 * pow(public, self.p5Ztau, modulus)) % modulus != Phi2:
            print "Verification not successful"
            return 0
        return 1

    def go_shuffle_shuffle(self, modulus, order, generator, public, alpha, beta):
        k=len(alpha)
        if k != len(beta):
            print("alpha,beta vectors have inconsistent length")
        ps=PairShuffle(modulus, k)
        pi=range(k)

        for i in range(k - 1, 1, -1):  # Permutation array
            j=get_random_int(0, i)
            if j != i:
                temporary_variable=pi[j]
                pi[j]=pi[i]
                pi[i]=temporary_variable
        neff_beta=[None] * k  # Initializing BETA
        for i in range(0, k):
            neff_beta[i]=get_random_int(0, order)
        XBar=[None] * k  # Initializing XBar
        YBar=[None] * k  # Initializing YBar

        for i in range(0, k):
            XBar[i]=pow(generator, neff_beta[pi[i]], modulus)
            XBar[i]=(XBar[i] * X[pi[i]]) % modulus
            YBar[i]=pow(public, neff_beta[pi[i]], modulus)
            YBar[i]=(YBar[i] * Y[pi[i]]) % modulus

        prover_var=ps.go_shuffle_prove(
            pi, modulus, generator, public, alpha, beta, neff_beta)
        if prover_var == 0:
            # TODO Raise error

        return XBar, YBar, ps
