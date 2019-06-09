print("Project Euler Problem #6")
import math

#finds the difference between the sum of the squares of num and square of sum
# natural nums only
def sumSquare(num):
    sumOfSq = 0
    sqOfSum = 0
    for i in range(1, num+1):
        sumOfSq += i**2
        sqOfSum += i
    sqOfSum = sqOfSum**2
    return sqOfSum - sumOfSq

def main():
    ans = sumSquare(int(input("Enter number: ")))
    print("Result: ", ans)

if __name__ == "__main__":
    main()