string1 = "Standard"
singleQuotes = 'single quotes'
nestedQuotes = "'allows single quotes nesed easily in double quotes' 'hello I am another set of quotes'"
concatAdjacent = "concate me please " "done!"
multiline = """multiline strings"""
multiline2 = '''multiline strings single quotes'''
newLine = "create a newline after string \n"
multipleNewLines = "\nmultiple new lines wihtin a single string\nnewline\nnewline again\n"

backslashEscaping = "hello \\ I just esacped a single backslash\n"

rawStringsToHelpWithBackSlashes = r"/Users/michaelyau/personal_github/python/control_flow/forLoops.py"

alphabet = "abcdefghijklmnopqrstuvwxyz"
getTheLetterD = alphabet[4]
indexString = alphabet[3]



def createLotsOfNewLineStrings(number):
    for i in range(number):
        print(newLine)


def main():
    myStrings = [string1, singleQuotes, nestedQuotes, concatAdjacent, multiline, multiline2, newLine, multipleNewLines, backslashEscaping]
    [print(x) for x in myStrings]
    createLotsOfNewLineStrings(5)
    multipleNewLines
    print(rawStringsToHelpWithBackSlashes)
    print(alphabet[6])
    print(getTheLetterD)
    print(indexString)


if __name__ == "__main__":
    main()
