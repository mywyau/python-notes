def fizzbuzz(endNumber: int):
    for i in range(endNumber + 1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif (i % 5 == 0) and (i % 3 == 0):
            print("Fizzbuzz!!")
        else:
            print(str(i))

def main():
    fizzbuzz(1000)

if __name__ == "__main__":
    main()