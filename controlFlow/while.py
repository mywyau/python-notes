def whileLoop():
    c = 5
    while c != 0:
        print(f"current value of c is: {c}")
        c -= 1
    print(f"finally left the while loop, the value of c is: {c}")


def breakLoop(desiredDivisor: int):
    while True:
        print("Looping please input a number :p")
        response = input("Number please:")
        if (int(response) % desiredDivisor) == 0:
            break
    print(f"We made it out of the loop! {response} was divisible by {desiredDivisor}")


def infinityLoop():
    # to terminal press: ctrl + c
    while True:
        print("Help me, kill...me........")


def main():
    # whileLoop()
    # infinityLoop()
    breakLoop(10)


if __name__ == "__main__":
    main()
