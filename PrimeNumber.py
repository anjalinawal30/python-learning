#Prime number

def findPrimes(m,n):
  primes=[]
  
  for x in range(m,n):
    i = 2
    isPrime = True
    
    while i<(x/i):
      if x%i == 0:
        isPrime = False
        break
      i += 1
      
    if isPrime:
      primes.append(x)
  
  return primes
  
m=5
n=25
result = findPrimes(m,n)
print(result)