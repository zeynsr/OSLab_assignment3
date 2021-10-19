num=int(input('Enter the number : '))
num1=num
a=[]
while num:
    a.append(int(num%10))
    num=int(num/10)    
n=len(a)
sum=0
for number in a:
    sum+=number**n
if sum==num1 :
    print('YES')
else :
    print('NO !')