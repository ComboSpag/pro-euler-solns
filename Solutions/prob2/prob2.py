print("Project Euler Problem 2")

def sumEvenFibs(limit):
    a = 1
    b = 2
    sum = 2
    while b < limit:
        a, b = b, a+b
        if b % 2 == 0:
            sum += b
    print(sum)

def main():
    sumEvenFibs(int(input("Enter limit: ")))

if __name__ == "__main__":
    main()
