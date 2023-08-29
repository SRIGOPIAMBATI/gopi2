#number pattern:
def m1(n):
    m=1
    for i in range (0,n):
        m=1
        for j in range(0,i+1):
            print(m,end=" ")
            m=m+1
        print("\r")
