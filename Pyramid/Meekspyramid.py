stacks = int(input("How tall is the pyramid? (1-8):"))
k = 2 * stacks - 2
if stacks > 8:
    quit('the pyramid is too tall')
if stacks < 1:
    quit('the pyramid is too short')
for i in range(0, stacks):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("# ", end="")
    print("")

