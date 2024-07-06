value1 = 1
value2 = "a"
value3 = True
value4 = False
value5 = ["a", "b", 1.5, -6]
value6 = {"mikey": "pineapple", "padric": "cars", "sean": "protein powder", "kurtis": "chinese food"}
value7: list[str] = ["a", "b", "c", "d"]
value8: list[int] = [1, 2, 3, 4]
value9: list[tuple[str, int]] = list(zip(value7, value8))

allValues = [value1, value2, value3, value4, value5, value6, value7, value8, value9]


def printUsingListComprehension():
    [print(v) for v in allValues]


def main():
    print(value1, value2, value3, value4, value5, value6, value7, value8, value9)


if __name__ == "__main__":
    main()