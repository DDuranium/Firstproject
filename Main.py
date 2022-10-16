# lijst = list(range(1, 1001))
# print(lijst)

drietjes = []
vijfjes = []

for x in range(1,1000):
    if x % 3 == 0:
        drietjes.append(x)
    elif x % 5 == 0:
        vijfjes.append(x)

somvijf = sum(vijfjes)
somdrie = sum(drietjes)
totaal = somvijf+somdrie

print(drietjes)
print(vijfjes)
print(totaal)