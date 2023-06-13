
# Error Handling using Try/Except

def divideWithErrorHandling(a, b) -> float:
    try:
        print(f"trying to divide {a} by {b}")
        print(a / b)
    except ZeroDivisionError:
        print("you cannot divide by zero!!\n")


example1 = divideWithErrorHandling(100, 5)
example2 = divideWithErrorHandling(100, 0)


def main():
    tryCatchExamples = [example1, example2]
    [x for x in tryCatchExamples]   # funnily enough there is an effect due to print lol


if __name__ == "__main__":
    main()
