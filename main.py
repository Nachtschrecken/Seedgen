# Credits to @fermatslibrary on https://twitter.com/fermatslibrary/status/1667517252768333825/photo/1
# We modified the algorithm to remove zeros that may lead to a shorter number due to conversion
#
# Seeding algorithm to generate new random numbers
# (c) Ferris Kleier 2023
# on https://github.com/Nachtschrecken/Seedgen

import string


seed = 389382919291923
n = 14
k = 100

def seedgen(seed,n,k):
    for _ in range(k):
        print(seed)
        seed = seed ** 2
        # remove zeros, this step is necessary to prevent zeros in the first index
        seed = str(seed).replace("0","")
        seed = int(str(seed)[(len(str(seed)) // 2) - (n // 2 ) : (len(str(seed)) // 2) + (n // 2 )])

seedgen(seed,n,k)