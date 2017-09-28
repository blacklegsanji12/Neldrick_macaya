
sums = 0
fibonachi = 0
firstNumber = 1
secondNumer = 1

for index in range(0,1000):
    if index%3 == 0 or index%5 == 0:
        sums += index

print "Sum = ",sums

sums = 0

while(fibonachi < 4000000):
    fibonachi = firstNumber + secondNumer

    if (fibonachi > 4000000):
        break


    firstNumber = secondNumer
    secondNumer = fibonachi

    if (firstNumber % 2==0):
        sums += firstNumber

print "2nd sum = ",sums

n =600851475143
newNum = n
i=2
highest = 0
while (i * i <= newNum):
    if (newNum%i == 0):
        newNum /= i
        highest = i;

    else:
        i+=1

if (newNum > highest):
    highest = newNum

print "Highest prime number = ",highest
