size=int(input('enter the size of array : '))
array=[]
i=0
while i< size:
    array.append(int(input()))
    i+=1
arr1=array
arr2=sorted(array)
if arr1==arr2 :
    print('The array is sorted')
else :
    print('The array is not sorted')