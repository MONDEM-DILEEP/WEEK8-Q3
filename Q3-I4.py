tup1=tuple(x*2 for x in range (1,9))
print("tuple for squares in range (1 to 8)",tup1)

tup2=tuple(x for x in range(10) if x%2 == 0)
print("tuple for even numbers in range (0 to 9)",tup2)
