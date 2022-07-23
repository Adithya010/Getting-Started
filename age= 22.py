n1 = []
for x in range(1500, 2700):
    if (x % 5 == 0) and (x % 7 == 0):
        n1.append(str(x))
print(n1)
# the difference in placing a join function to get a better output
print(','. join(n1))
