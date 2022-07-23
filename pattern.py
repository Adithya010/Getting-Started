
print("1. Reverse Hill pattern:-")

n = 5

for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i, n-1):
        print("*", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()

print("2. The next pattern is as shown below:-")

n = 5

for i in range(n):
    for j in range(i, n):
        print("*", end='')
    print()
for i in range(n):
    for j in range(i+1):
        print(chr(65), end='')
    print()

print()
print()

print("3. Create patterns with ASCII characters:-")
print()

n = 5

for i in range(n):
    for j in range(i+1):
        print(chr(65), end='')
    print()

print()


print("4. Character pattern for increasing order of ASCII from A to E-- Doubled")
print()


for i in range(65, 70):
    for j in range(65, i+1):
        print(chr(i), end='')

    print()

print()
print()


print("5. Character pattern for increasing order of ASCII from A to E")
print()


for i in range(65, 70):
    k = i
    for j in range(65, i+1):
        print(chr(k), end='')
        k += 1

    print()

print()
print()

print("6. Character pattern for pyramid order of ASCII from A to E")
print()


m = 6
# Outer loop
for i in range(65, 70):
    m = m-1
    # Inner loop 1
    for j in range(m, 1, -1):
        print(" ", end="")
    # Inner loop 2
    for k in range(65, i+1):
        print(chr(k), end="")
    # Inner loop 3
    for n in range(65, i):
        print(chr(n), end="")
    print()

print()
print()

print("7. DCBA order at the end of ASCII:")
print()


for i in range(65, 70):
    for j in range(i, 64, -1):
        print(chr(j), end='')
    print()


print()
print("8. Starting from B to B in ASCII:")
print()


for i in range(65, 70):
    for j in range(i, 65, -1):
        print(chr(j), end='')
    print()

print("#")

print()
print("9. Only A and B in ASCII that to un even and odd ranges:")
print()

n = 5

for i in range(n):
    for j in range(i+1):
        if (i % 2 == 0):
            print("A", end='')
        else:
            print("B", end='')
    print()

print()
print("10. Other sided Z to 0 in ASCII")
print()

n = 5

for i in range(n):
    for j in range(i):
        print(" ", end='')
    for j in range(i, n):
        if (i % 2 == 0):
            print("Z", end='')
        else:
            print("0", end='')
    print()
print()
print("11. A in first and C in second ASCII")
print()

n = 5
p = 65

for i in range(n):
    for j in range(i+1):
        print(chr(p), end='')
    p += 2
    print()

print()
print("12. Hill shaped:")
print()

n = 5
p = 65

for i in range(n):
    for j in range(i, n):
        print(" ", end='')
    for j in range(i):
        print(chr(p), end='')
    for j in range(i+1):
        print(chr(p), end='')
    p += 1
    print()

print()
print("13. Print out a right triangle with the name CODER with C at the start:")
print()

s = "CODER"
n = len(s)
p = 0

for i in range(n):
    for j in range(i+1):
        print(s[p], end="")
    p += 1
    print()
