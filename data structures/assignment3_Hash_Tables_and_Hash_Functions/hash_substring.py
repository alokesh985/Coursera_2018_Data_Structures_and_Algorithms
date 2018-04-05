# python3
import random
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def PolyHash(S,p,x):
    hash = 0
    for char in reversed(S):
        hash = ((hash * x + ord(char)) % p+p) %p
    return hash

def PreComputeHashes(T,lp, p, x):
    lt = len(T)
    H = [None]*(lt-lp+1)
    S = T[lt-lp:lt]
    H[lt-lp] = PolyHash(S, p, x)
    y = 1
    for i in range(lp):
        y = (y * x) % p
    for i in range(lt-lp-1,-1,-1):
        H[i] = (x* H[i+1] + ord(T[i]) - y * ord(T[i+lp])) % p
    return H
def get_occurrences(pattern, text):
    lp , lt = len(pattern), len(text)
    p = 1000000007
    x = random.randint(1,p-1)
    result = []
    pHash = PolyHash(pattern, p , x)
    H = PreComputeHashes(text, lp, p, x)
    for i in range(lt-lp+1):
        if H[i] != pHash: continue
        if text[i:i+lp] == pattern:
            result.append(i)
    return result



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

