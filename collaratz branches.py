def branch():
    x=int(input("x= "))
    for n in range(x):
        a=(2**n-1)/3
        if a%1==0:
            print("2^",n,"= ",2**n," has a BRANCH", a)
        else:
            print("2^",n,"= ",2**n,"has no branch")
branch()
        
