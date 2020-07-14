
import math
length = input("What is the length of your rectangle? ")
breadth = input("What is the breadth of your rectangle? ")
length = float(length)
breadth = float(breadth)
if length < 0:
    print("Wrong input!!")
elif breadth < 0:
    print("Wrong input!!")
elif length >= breadth:
    print("Area = ", (length * breadth))
    print("Perimeter = ", (2 * (length + breadth)))
    print("Diagonal = ", math.sqrt((length ** 2 + breadth ** 2)))

elif length < breadth:
    print("""Please enter correct values! 
Length should be greater than Breadth!!!""")
