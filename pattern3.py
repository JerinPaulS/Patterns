# ****
# *  *
# *  *
# ****

def pattern(n):

    for i in range(n):
        if i in (0, n - 1):
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*")

def printSeparator():
    print("---------------------------------------------------------------------------------------------------")

pattern(1)
printSeparator()
pattern(2)
printSeparator()
pattern(3)
printSeparator()
pattern(4)
printSeparator()
pattern(5)
printSeparator()
pattern(10)
printSeparator()
    