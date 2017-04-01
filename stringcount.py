stringDict = {}

text = input("Text: ").split()

for words in text:
    if words in stringDict:
        stringDict[words] += 1
    else:
        stringDict[words] = 1

longestString = 0
for key, value in stringDict.items():
    x = len(stringDict[value])
    if x > longestString:
        placeholderString = stringDict[key]


for key, value in range(len(stringDict)):
    print("{:{}} : {}".format(placeholderString, key, value))

