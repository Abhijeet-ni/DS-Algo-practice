# row = int(input("Enter the number:"))
# col = int(input("Enter the number:"))

# for i in range(0, row):
#     for j in range(col):
#         if (i == 0) or (i==(row-1)) or (j==0) or (j== col-1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

def printPat(n):
    #Code here
    for i in range(n,0,-1):
        t=n
        for j in range(n):
            print(str(t)*i,end=" ")
            t-=1
        print("$",end=" ")

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n= int(input())
        print (printPat(n))


26368 -4424