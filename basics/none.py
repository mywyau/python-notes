nothingButNotNull = None
something = 1


def noneChecker(none: None):
    if none is None:
        print("true None == None")
    else:
        print("something fishy is going on")


def main():
    listOfNothings = [noneChecker(nothingButNotNull), noneChecker(something)]
    [n for n in listOfNothings]  # seems to have no effects but we have prints so there are effects


if __name__ == "__main__":
    main()
