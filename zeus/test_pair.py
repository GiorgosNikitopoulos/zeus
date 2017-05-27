from pairshuffle import PairShuffle
from Crypto.PublicKey import ElGamal
from Crypto.Random import random
from Crypto import Random
import binascii

def main():
    Result3 = 0
    Result1 = [None] * 5##Init Result1
    Result2 = [None] * 5##Init Result2
    key = ElGamal.generate(256, Random.new().read) ##Generate Elgamal key
    q = (key.p - 1) / 2 ##Get order
    alpha = [None] * 5
    beta = [None] * 5 ##Init ElGamal Pair
    messages = [None] * 5 ##Init message pair
    messages = ['Text_for_one', 'Text_for_two', 'Text_for_three', 'Text_for_four', 'Text_for_five']
    for i in range(5):
        alpha[i], beta[i] = key.encrypt(messages[i], key.y) ##Encrypt messages
    for i in range(5):
        alpha[i] = int(binascii.hexlify(alpha[i]), 16)
        beta[i] = int(binascii.hexlify(beta[i]), 16) ##Turn the messages into ints
    pairshuffle_obj = PairShuffle(key.p, 5) ##Init PairShuffle object
    Result1, Result2, b_var = pairshuffle_obj.go_shuffle_shuffle(key.p, q, key.g, key.y, alpha, beta)
    print Result1
    print Result2
    print b_var

if __name__ == "__main__":
    main()
