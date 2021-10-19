import random
numbers = []
counter=int(input('enter the size of array :'))
i=0

while i<counter:
    num = random.randint(1, 1000)
    if not (num in numbers):
        numbers.append(num)
        i +=1
    else:
        print("repeated")

print(numbers)