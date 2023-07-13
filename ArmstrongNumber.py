input_number = int(input('Enter the number : '))
number_temp = input_number
array = []
while input_number:
    array.append(int(input_number%10))
    input_number = int(input_number/10)    
n = len(array)
sum = 0
for number in a:
    sum += number ** n
if sum == number_temp:
    print('YES')
else:
    print('NO!')
