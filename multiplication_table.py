#Abu HAsnat Hasib
#CIS 1051

def table(n):

    for c in range(1,n+1): #each column start from here
        print(c,end=" ")
        for r in range (c*2,n*c+1,c): #each row continues here
            print(r,end=" ")
        print("")


table(5)