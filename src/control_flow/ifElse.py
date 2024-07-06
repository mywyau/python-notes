def ifStatement(x):
    if x == 2:
        print(f"{x} == 2")

def elifExpression(x):
    if x == 2:
        print(f"{x} == 2")
    elif x == 3:
        print(f"{x} == 3 we are in the elif block")
    else:
        print(f"{x} != 2")


def ifElseExpression(x):
    if x == 2:
        print(f"{x} == 2")
    else:
        print(f"{x} != 2")


def main():
    # ifStatement(5)
    ifStatement(2)
    elifExpression(3)
    ifElseExpression(10)


if __name__ == "__main__":
    main()
