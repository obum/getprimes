def getprimes ():
    n = int(input())
    a = int(n**(1/2) + 1)
    primes = []
    z= [0 for x in range (n)]
    odd = [i for i in range (2,n) if i%2 != 0]
    for j in range (3,a,2):
        odd[3*j:] = z[3*j:]
    for y in odd[3:]:
        if y != 0: 
           primes.append(y)
    return  (primes)

getprimes ()