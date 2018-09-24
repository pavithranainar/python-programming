print ("CHECK WHETHER A NUMBER IS PRIME OR NOT")
N=int(input("enter the number"))
s=0
forx in range(1,N+1):
if(N%x==0):
if(s==2):
print("prime")
else:
   print("not")
