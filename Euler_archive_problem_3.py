# =============================================================================
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# 
# =============================================================================
def isprime(number):
    testlijst = [] 
    for idx in range(1,number+1):
        if number % idx == 0:
            testlijst.append(idx)        
    if len(testlijst) == 2:
        return True
    else:
        return False

getal = 10000       
prime = []


for counter in range(1,getal+1):
   if isprime(counter):
         prime.append(counter)
       
print(prime)
num_prime_factors = len(prime)
print(num_prime_factors)


test_getal = 600851475143 

highest_prime_factors = []

for counter in reversed(prime):
    if test_getal % counter == 0:
        highest_prime_factors.append(counter)

print(f' This are all primes: {highest_prime_factors}!')
print(f' This is the highest primefactor: {highest_prime_factors[0]}')
