import sys
number=int(input('Enter the number : '))
cnt=r=1
while True:
    r=r*cnt
    if r==number :
        print('YES ')
        sys.exit(0)
    if r>number:
        print(' NO !') 
        break   
    else:
        cnt+=1    