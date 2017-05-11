from random import randint, shuffle, choice
from datetime import datetime
import Crypto.Util.number as number
from Crypto import random

def go_shuffle_prove():


def go_shuffle_verify():

def go_shuffle_shuffle(modulus, generator, generator2, public, X, Y, report_thresh=128):
    random.seed(datetime.now())
    k = len(X)
	if k != len(Y) {
		print("X,Y vectors have inconsistent length")
	}
    pi = range(k)

    for i in range(k -1, 1, -1):
        j = random.randint(0, i)
        if j != i:
            temporary_variable = pi[j]
            pi[j] = pi[i]
            pi[i] = temporary_variable
    beta = [None] * k
    for i in range(0, k):
        beta[i] = get_random_int(0, modulus)
    XBar = [None] * k
    YBar = [None] * k

    for i in range(0, k):
        XBar[i] = (beta[pi[i]] * g) % modulus
        XBar[i] = (XBar[i] + X[pi[i]]) % modulus
        YBar[i] = (beta[pi[i]] * h) % modulus
        YBar[i] = (YBar[i] + Y[pi[i]]) % modulus
#TODO: prove_encryption
    return XBar, YBar
