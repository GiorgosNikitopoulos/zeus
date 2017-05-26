from pairshuffle import PairShuffle
from Crypto.PublicKey import ElGamal
from Crypto.Random import random
from Crypto import Random
import binascii

def main():
    Resoolt3 = 0
    Resoolt1 = [None] * 5
    Resoolt2 = [None] * 5
    key = ElGamal.generate(256, Random.new().read)
    q = (key.p - 1) / 2
    alpha = [None] * 5
    beta = [None] * 5
    messages = [None] * 5
    messages = ['Text_for_one', 'Text_for_two', 'Text_for_three', 'Text_for_four', 'Text_for_five']
    for i in range(5):
        alpha[i], beta[i] = key.encrypt(messages[i], key.y)
    for i in range(5):
        alpha[i] = int(binascii.hexlify(alpha[i]), 16)
        beta[i] = int(binascii.hexlify(beta[i]), 16)
    pairshuffle_obj = PairShuffle(key.p, 5)
    print key.p
    print q
    print key.g
    print key.y
    print alpha
    print beta
    Resoolt1, Resoolt2, b_var = pairshuffle_obj.go_shuffle_shuffle(key.p, q, key.g, key.y, alpha, beta)
    print Resoolt1
    print Resoolt2
    print b_var

if __name__ == "__main__":
    main()
