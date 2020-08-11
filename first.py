n=int(input("Enter number of elements "))
arr=[]
print("Enter elements :")
for i in range(0,n):
    z=int(input())
    arr.append(z)

sum=0
for i in arr:
    sum=sum+i

lsum=0
rsum=sum-arr[0]
flag=0

if n==1:
    flag=1
    print(f"Equilibrium point is {arr[n-1]} ")
elif n==2:
    flag=1
    print("No equlibrium point ")
else:
    for i in range(1,n-1):
        rsum=rsum-arr[i]
        lsum=lsum+arr[i-1]
        if(lsum==rsum):
            print(f"Equilibrium point is at {i+1} and value at that point is {arr[i]}")
            flag=1
            break
if flag==0:
    print("Equilibrium not possible ")
        

