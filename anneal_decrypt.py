import random
import ngram_score2 as ns
import copy
fitness = ns.ngram_score('english_trigrams.txt')


crypted = "rbcfvbc ldgmdkbc ejbgb dgb cbobgds hejbg khofbc ejde bohqb ybbsfimc hy ihcedsmfd fi mbbqc cibdqbgc thgegduc d rdiv hy jdpqbgc kfccfhi fkthccfrsb fc d jfe eo cbgfbc engibv eh d jfe khofb cbgfbc cedggfim ehk pgnfcb rne ejb pghli zblbs fc kdegfx ru ejb ldpjhlcqfc fi ejb khofb khgtjbnc cbie ibh d kbccdmb ejde kbccdmb cdfv ldqb nt ibh ejb kdegfx jdc uhn pdi uhn gbkbkrbg ljde ldc ejb ibxe cbiebipb"

crypted_words = crypted.split(' ')

cipher = list(set(crypted.replace(' ', '')))
key = 'abcdefghijklmnopqrstuwvxyz'


def score(key):
    points = 0
    decr = dict(zip(cipher, key))
    for word in crypted_words:
        decrypted_word = "".join([decr.get(l, '') for l in word])
        points += fitness.score(decrypted_word)
    return points

def decrypt(cipher, key, crypted_words):
    decr = dict(zip(cipher, key))
    return " ".join(["".join([decr.get(l, '') for l in word]) for word in crypted_words])

def shuffle(key):
    a = random.randint(0, len(key)-1)
    b = random.randint(0, len(key)-1)
    a_v = key[a]
    b_v = key[b]
    am = list(key)
    am[b] = a_v
    am[a] = b_v
    return "".join(am)

points = -1000000

max_points = points

t = 1.0

freezing = 0.9997

while True:
    new_key = shuffle(key)

    p = score(new_key)
    if p > points:
        if p > max_points:
            max_points = p
            print("temperature", t)
            print("POINTS", p)
            print("KEY", new_key)
            print(decrypt(cipher, new_key, crypted_words))
        key = new_key
        points = p

    else:
        if random.random() < t:
            points = p
            key = new_key
    t *= freezing
