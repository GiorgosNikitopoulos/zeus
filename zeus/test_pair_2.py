from pairshuffle_test import PairShuffle_test
from Crypto.PublicKey import ElGamal
from Crypto.Random import random
from Crypto import Random
import binascii
import random

def main():
    Resoolt3 = 0
    Resoolt1 = [None] * 5
    Resoolt2 = [None] * 5
    k = 5 ## Number in list
    ##key = ElGamal.generate(512, Random.new().read)
##    q = (key.p - 1) / 2
    p = 10198267722357351868598076141027380280417188309231803909918464305012113541414604537422741096561285049775792035177041672305646773132014126091142862443826263
    q = 50991338611786759342990380705136901402085941546159019549592321525060567707073022687113705482806425248878960175885208361528233865660070630455714312219131313
    g = 4
    h =  random.getrandbits(512)
    H = pow(g, h, p)
    ##Make client keys
    c = [None] * k
    C = [None] * k
    X = [None ] * k
    Y = [None] * k
    for i in range(0 , k):
        c[i] = random.getrandbits(512)
        C[i] = pow(g, c[i], p)
    ############
    for i in range(0, k):
        r = random.getrandbits(512)
        X[i] = pow(g, r, p)
        Y[i] = pow(H, r, p)
        Y[i] = (Y[i] * C[i]) % p
    pairshuffle_obj = PairShuffle_test(p, 5)
    print hex(p)
    print hex(q)
    print hex(g)
##    print hex(X)
##    print hex(Y)
    Resoolt1, Resoolt2, b_var = pairshuffle_obj.go_shuffle_shuffle(p, q, g, H, X, Y)
##    print hex(Resoolt1)
##    print hex(Resoolt2)
    print hex(b_var)

if __name__ == "__main__":
    main()
