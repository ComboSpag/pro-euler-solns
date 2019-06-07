import math

def findNthPrime(nth):
    count = 0
    currNum = 1
    isPrime = False
    
    while count < nth:
        isPrime = True
        currNum += 1
        if currNum == 2 or currNum = 3:
            count += 1
            continue
        if currNum != 2 and currNum % 2 == 0:
            continue
        k = math.ceil(math.sqrt(currNum))
        for i in range(3, k, 2):
            if currNum % i == 0:
                isPrime = False
                break
        if isPrime:
            count += 1

    return currNum 


def main():
    print("Prob 7: Find n-th Prime")
    num = input("Enter Numer: ") 
    ans = findNthPrime(num)
    print("Result:")
    print(num, "th prime is ", ans)

if __name__ == "__main__" : main()
