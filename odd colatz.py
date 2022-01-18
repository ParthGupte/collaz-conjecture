import matplotlib.pyplot as plt
def main():
    X=[]
    Y=[]
    for i in range(1,10000,2):
        X.append(i)
        n=(3*i)+1
        while n%2==0:
            n/=2
        Y.append(n)
    plt.scatter(X,Y,s=1)
    plt.xlabel("Odd numbers")
    plt.ylabel("Nxt odd in seq")
    plt.show()
            
main()
