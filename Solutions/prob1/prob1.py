def sum_of_mults(num):
    sum = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)

def main():
    sum_of_mults(int(input("Enter max number: ")))

if __name__ == "__main__":
    main()