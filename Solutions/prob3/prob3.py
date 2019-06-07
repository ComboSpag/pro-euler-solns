print("Project Euler Problem 3")
import math

def largestPrimeFactor(num):
    lim = num
    max = 1
    primeArr = []
    while num % 2 == 0:
        max = 2
        primeArr.append(2)
        num //= 2

    for i in range(3, int(math.sqrt(lim)), 2):
        while num % i == 0:
            max = i
            primeArr.append(i)
            num //= i
    print(primeArr)
    print("Largest prime factor is", max)

def main():
    largestPrimeFactor(int(input("Enter number: ")))

if __name__ == "__main__":
    main()