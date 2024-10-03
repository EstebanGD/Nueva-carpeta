"""for i in range(8):
    j=i
    while i > 0:
        print(" ", end="")
        i = i-1
    i=j
    for j in range(i,9,+1):
        print(j, end = " ")
    if i != 7:
        print(" ")

for i in range(8,-2,-1):
    j=i
    while i > -1:
        print(" ", end="")
        i = i-1
    i=j
    for j in range(8,i,-1):
        print(j, end = " ")
    print(" ")"""

for i in range(8):
    j=i
    while i > 0:
        print(" ", end="")
        i = i-1
    i=j
    for j in range(i,9,+1):
        print(j, end = " ")
    print(" ")

for i in range(8,-1,-1):
    j=i
    while i > 0:
        print(" ", end="")
        i = i-1
    i=j
    for j in range(i,9,+1):
        print(j, end = " ")
    print(" ")