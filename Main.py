lijst = list(range(1, 1001))
print(lijst)

drietjes = []
vijfjes = []

for x in range(1,1001):
    if (x%3 == 0):
        drietjes.append(x)
    elif (x%5 == 0):
        vijfjes.append(x)
print(drietjes)
print(vijfjes)
