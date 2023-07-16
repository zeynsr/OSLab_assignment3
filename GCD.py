num1 = int(input())
num2 = int(input())

if num1 > num2 :
    Min = num2
else:
    Min = num1    
for i in range(1, Min+1) :
    if((num1 % i == 0) and (num2 % i == 0)):
        gcd = i    
print('GCD : ', gcd)        
