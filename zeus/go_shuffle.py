from random import randint, shuffle, choice
from datetime import datetime
import Crypto.Util.number as number
from Crypto import random

class PairShuffle:

    def __init__(modulus, k):
            ps.modulus = modulus
            ps.k = k
            ps.p1.A = list([None]) * k
            ps.p1.C = list([None]) * k
            ps.p1.U = list([None]) * k
            ps.p1.W = list([None]) * k
            ps.v2.Zrho = list([None]) * k
            ps.p3.D = list([None]) * k

    def go_shuffle_prove(pi, modulus, generator, public, alpha, beta, neff_beta, random, context):
        if len(alpha) != len(pi) || len(alpha) != len(beta):
            print "Error happened"
        piinv = [None] * k
        for i in range (k):
            piinv[pi[i]] = i
        p1 = ps.p1
        u = [None] * k
        w = [None] * k
        a = [None] * k
        tau0 = random##TODO
        nu = random ##TODO
        gamma = random ##TODO
        ##TODO: u w a random lists
        p1.Gamma = (pow(generator, gamma, modulus)) % modulus
        wbetasum = tau0
        p1.Lamda1 = 0
        p1.Lamda2 = 0
        for i in range(k):
            p1.A[i] = pow(generator, a[i], modulus)
            temporary_variable = (gamma * a[pi[i]]) % modulus
            p1.C[i] = pow(generator, temporary_variable, modulus)
            p1.U[i] = pow(generator, u[i], modulus)
            temporary_variable = (gamma * w[i]) % modulus
            p1.W[i] = pow(generator, temporary_variable)
            temporary_variable = (w[i] * neff_beta[pi[i]]) % modulus
            wbetasum = (wbetasum + temporary_variable) % modulus
            temporary_variable = (w[piinv[i]] - u[i]) % modulus
            temporary_variable_2 = (alpha[i] * temporary_variable) % modulus
            p1.Lamda1 = (p1.Lamda1 + temporary_variable_2) % modulus
            temporary_variable_2 = (beta[i] * temporary_variable) % modulus
            p1.Lamda2 = (p1.Lamda2 + temporary_variable_2) % modulus

        p1.Lamda1 = p1.Lamda1 +

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
