def fact(n):
    if n==0:
        return 0
    return n+fact(n-1)

inp = int(input("enter a number: "))
print(f"the summation of {inp} is {fact(inp)}")