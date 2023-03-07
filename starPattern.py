def upside_down_pyramide(n):
    for i in range(n,0,-1):
        print(" "*int(n-i)+"* "*i)

def pyramide(n):
    for i in range(n):
        print(" "*int(n-i)+"* "*i)


print("Star Program")
n = int(input("Enter the no of levels:"))
upside_down_pyramide(n)
print()
pyramide(n)