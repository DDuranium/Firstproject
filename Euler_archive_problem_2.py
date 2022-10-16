Fibonacci = [1,2]

for idx in range(1,200):
    
    number = Fibonacci[idx]+Fibonacci[idx-1]
    if number > 4000000: 
        break
    Fibonacci.append(number)
    


print(Fibonacci)

elementnummer = len(Fibonacci)
print(elementnummer)

fibo_even = []

for idx in range(0,31):
    if Fibonacci[idx]%2 == 0:
        fibo_even.append(Fibonacci[idx])
        
print(fibo_even)

fibo_even_sum = sum(fibo_even)

print(fibo_even_sum)

