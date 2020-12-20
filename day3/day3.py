print("--------Question1-----------")
points = 7

if(points < 40):
    print("You are fail")
elif(points > 40 and points < 70):
    print("Good work")
elif(points > 70 and points < 80):
    print("Very good")
elif(points > 80 and points < 100):
    print("Excellent")
else:
    print("You are fail")

print("-------------Question 2-------------")
for i in range(1, 1000):
   # all prime numbers are greater than 1
   if i > 1:
       for num in range(2, i):
           if (i % num) == 0:
               break
       else:
           print(i)

print("-----------Question 3------------")
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j)
print("\n")

print("------------------Question 4----------------")
num = int(input("Enter max number"))
i = 2
while i < num:
    isPrime = True
    j = 2
    while j < i:
        if i % j == 0:
            isPrime = False
            break
        j += 1
    if isPrime:
        print(i)
    i += 1
