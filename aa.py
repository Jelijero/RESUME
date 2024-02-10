a=[1,2,3,1]
for i in range(len(a)):
    for j in range(0,len(a)):
        if (i==j):
           j=j+1
        if a[i]==a[j]:
         print("true")
        else:
         print("false")