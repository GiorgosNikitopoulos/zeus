from random import randint, shuffle, choice
from datetime import datetime
import Crypto.Util.number as number
from Crypto import random

class PairShuffle:

    def __init__(self, modulus, k):
            self.modulus = modulus
            self.k = k
            self.Gamma = 0
            self.p1A = list([None]) * k
            self.p1C = list([None]) * k
            self.p1U = list([None]) * k
            self.p1W = list([None]) * k
            self.v2 = []
            self.v2Zrho = list([None]) * k
            self.p3 = []
            self.p3D = list([None]) * k
            self.p1 = []
            self.p1Lamda1 = 0

    def go_shuffle_prove(pi, modulus, generator, public, alpha, beta, neff_beta, random, context):
        if len(alpha) != len(pi) || len(alpha) != len(beta):
            print "Error happened"
        piinv = [None] * k
        for i in range (k):
            piinv[pi[i]] = i
        u = [None] * k
        w = [None] * k
        a = [None] * k
        tau0 = random##TODO
        nu = random ##TODO
        gamma = random ##TODO
        ##TODO: u w a random lists
        self.Gamma = (pow(generator, gamma, modulus)) % modulus
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
        


    def go_shuffle_verify(modulus, generator, public, alpha, beta, alphabar, betabar):



    def go_shuffle_verifier(modulus, generator, public, alpha, beta, alphabar, betabar, report_thresh=128):


    def go_shuffle_shuffle(modulus, generator, public, alpha, beta, report_thresh=128):
        random.seed(datetime.now())
        k = len(alpha)
    	if k != len(beta) {
    		print("alpha,beta vectors have inconsistent length")
    	}
        pi = range(k)

        for i in range(k -1, 1, -1):##Permutation array
            j = random.randint(0, i)
            if j != i:
                temporary_variable = pi[j]
                pi[j] = pi[i]
                pi[i] = temporary_variable
        neff_beta = [None] * k## Initializing BETA
        for i in range(0, k):
            beta[i] = get_random_int(0, modulus)
        XBar = [None] * k ##Initializing XBar
        YBar = [None] * k ##Initializing YBar

        for i in range(0, k):
            XBar[i] = pow(generator, neff_beta[pi[i]], modulus)
            XBar[i] = (XBar[i] * X[pi[i]]) % modulus
            YBar[i] = pow(public, neff_beta[pi[i]], modulus)
            YBar[i] = (YBar[i] * Y[pi[i]]) % modulus
    #TODO: prove_encryption
        return XBar, YBar
