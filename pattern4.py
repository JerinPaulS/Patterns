# ****
#  ****
#   ****
#    ****

def pattern(n):

    for i in range(n + 1):
        print(" " * i, end="")
        print("*" * n)

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
    